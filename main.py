import app.getRepo.query_rest as queryRest
import app.getRepo.query_graph as queryGraph
import app.getCalc.calcu as calcular
import os

timeRest = []
sizeRest = []
timeGraph = []
sizeGraph = []


def main():
    if not os.path.exists('tmp'):
        os.mkdir('tmp')

    # ApiRest
    rr = queryRest.executeQuery()
    timeRest.append(calcular.calcularMiliSegundos(rr))
    sizeRest.append(calcular.calcularTamanho(rr))
    # ApiGraph
    rq = queryGraph.get_repository()
    timeGraph.append(calcular.calcularMiliSegundos(rq))
    sizeGraph.append(calcular.calcularTamanho(rq))
    print(timeRest, sizeRest, timeGraph, sizeGraph)


if __name__ == "__main__":
    main()
