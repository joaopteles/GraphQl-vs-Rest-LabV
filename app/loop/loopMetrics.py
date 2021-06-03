import app.getRepo.query_rest as queryRest
import app.getRepo.query_graph as queryGraph
from statistics import mean, median


qRest1 = "q=stars:>100+language:JavaScript"
qRest2 = "q=stars:>100+language:Java"
qRest3 = "q=stars:<10+language:Dart"
qRest4 = "q=stars:>100+language:Python"
qRest5 = "q=stars:<50+language:JavaScript"
querysRest = [qRest1, qRest2, qRest3, qRest4, qRest5]
qGraphQl1 = "stars:>100 language:JavaScript"
qGraphQl2 = "stars:>100 language:Java"
qGraphQl3 = "stars:<10 language:Dart"
qGraphQl4 = "stars:>100 language:Python"
qGraphQl5 = "stars:<50 language:JavaScript"
querysGraphQl = [qGraphQl1, qGraphQl2, qGraphQl3, qGraphQl4, qGraphQl5]

timeRest = []
sizeRest = []
timeGraph = []
sizeGraph = []


def executeParalela():
    for x in querysRest:
        r = queryRest.executeQuery(x)
        timeRest.append(r.elapsed.total_seconds() * 1000)
        sizeRest.append(len(r.content))

    for y in querysGraphQl:
        r = queryGraph.get_repository(y)
        timeGraph.append(r.elapsed.total_seconds() * 1000)
        sizeGraph.append(len(r.content))

    print("PARALELA:")
    print("Tempo Rest:{}".format(int(mean(timeRest))))
    print("Tamanho Rest:{}".format(median(sizeRest)))
    print("Tempo GraphQl:{}".format(int(mean(timeGraph))))
    print("Tamanho GraphQl:{}".format(median(sizeGraph)))


def executeSequencial():
    for x in querysRest:
        r = queryRest.executeQuery(x)
        timeRest.append(r.elapsed.total_seconds() * 1000)
        sizeRest.append(len(r.content))

    for y in querysGraphQl:
        r = queryGraph.get_repository(y)
        timeGraph.append(r.elapsed.total_seconds() * 1000)
        sizeGraph.append(len(r.content))

    print("SEQUENCIAL:")
    print("Tempo Rest:{}".format(int(mean(timeRest))))
    print("Tamanho Rest:{}".format(median(sizeRest)))
    print("Tempo GraphQl:{}".format(int(mean(timeGraph))))
    print("Tamanho GraphQl:{}".format(median(sizeGraph)))
