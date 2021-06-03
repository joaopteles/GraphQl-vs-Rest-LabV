import os
import pandas as pd
import json

token = "INSERT_TOKEN"


def format_metric(tipo_de_api, tip_execucao, qtd_itens, query_size, res):
    return {
        "tipo_de_api": tipo_de_api,
        "tip_execucao": tip_execucao,
        "qtd_itens": qtd_itens,
        "tamanho_query": query_size,
        "tempo_de_resposta": res.elapsed.total_seconds(),
        "tamanho_body_resposta": len(res.content)
    }


def save(path, file_name, items):
    if len(items) == 0:
        return
    create_folder(path)
    path_file = "{}/{}.csv".format(path, file_name)
    df = pd.DataFrame(items)
    if os.path.isfile(path_file):
        df.to_csv(path_file, mode='a', header=False, index=False)
    else:
        df.to_csv(path_file, index=False)


def create_folder(basename):
    if not os.path.exists(basename):
        os.mkdir(basename)


def load_json(path):
    with open(path) as json_file:
        return json.load(json_file)
