import query_rest
import query_graphql
import utils
import time


def collect_metrics(queries, itens, tipo_api, query_func):
    metrics = []
    for q in queries:
        for i in itens:
            res, query_size = query_func(q, i)
            if res.status_code != 200:
                raise Exception("Requests error: {}".format(res.status_code))
            metrics.append(utils.format_metric(tipo_api, "sequencial", i, query_size, res))
            time.sleep(2)
    return metrics

def exec_measurement(queries, itens):
    metrics = collect_metrics(queries, itens, "rest", query_rest.execute_query)
    metrics = metrics + collect_metrics(queries, itens, "graphql", query_graphql.execute_query)
    utils.save('dataset', 'metrics', metrics)

