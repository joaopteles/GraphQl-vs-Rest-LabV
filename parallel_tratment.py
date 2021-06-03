
import asyncio
import utils
import query_rest
import query_graphql

def get_permutation(queries, itens):
    permutation = []
    for q in queries:
        for i in itens:
            permutation.append({ "query": q, "item": i})
    return permutation

def get_slice(start, end, queries, itens):
    group = []
    for i in range(start, end):
        for item in itens:
            group.append({ "query": queries[i], "item": item})
    return item

def group_treatments_by(queries, itens, max_size):
    size = len(queries) * len(itens)
    remainder =  size % max_size
    max_groups = int(size / max_size) + (1 if remainder > 0 else 0)
    permutation = get_permutation(queries, itens)
    group_size = int(len(permutation) / max_groups)
    groups = []

    for i in range(0, max_groups):
        start = i * group_size
        end = start + group_size
        if end > len(permutation):
            groups.append(permutation[start:])
        else:
            groups.append(permutation[start:end])
    return groups

async def collect_metric(tipo_api, batch, query_func):
    res, query_size = query_func(batch['query'], batch['item'])
    if res.status_code != 200:
        raise Exception("Requests error: {}".format(res.status_code))
    return utils.format_metric(tipo_api, "paralelo",  batch['item'], query_size, res)

def collect_group_of_metrics(groups, query_func, tipo_api):
    metrics = []
    for batch in groups:
        loop = asyncio.get_event_loop()
        futures = [asyncio.ensure_future(collect_metric(tipo_api, b, query_func)) for b in batch]
        metrics = metrics + loop.run_until_complete(asyncio.gather(*futures))
        asyncio.sleep(3)
    return metrics

def exec_measurement(queries, itens):
    groups = group_treatments_by(queries, itens, 10)
    metrics = collect_group_of_metrics(groups, query_rest.execute_query, "rest")
    metrics = metrics + collect_group_of_metrics(groups, query_graphql.execute_query, "graphql")
    utils.save('dataset', 'metrics', metrics)

