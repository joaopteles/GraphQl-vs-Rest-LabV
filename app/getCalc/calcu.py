
def calcularMiliSegundos(r):
    return r.elapsed.total_seconds()*1000


def calcularTamanho(r):
    return len(r.content)
