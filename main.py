import sequential_tratment
import parallel_tratment
import utils

def main():
    tratamentos = utils.load_json("tratamentos/tratamentos.json")
    interacoes = tratamentos['interacoes']
    itens = tratamentos['quantidade_itens']
    queries = tratamentos['tamanho_query']

    i = 0
    while i < interacoes:
        print("Interação: {}".format(i + 1))
        print("Processing sequencial")
        sequential_tratment.exec_measurement(queries, itens)
        print("Processing Parallel")
        parallel_tratment.exec_measurement(queries, itens)
        i+=1



main()