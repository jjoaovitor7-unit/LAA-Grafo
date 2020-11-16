from browser import document, html

# Abrindo arquivo
file = open('data/grafo-nao-valorado.txt', 'r', encoding='utf8')

# Inicializando grafo
grafo = {}

for linha in file:
    vInicial, vFinal = linha.split()
    grafo.setdefault(int(vInicial), []).append((int(vFinal)))
    # grafo.setdefault(int(vFinal), []).append((int(vInicial)))

document.attach(html.P("Representação do Grafo Não-Valorado"))
for i in grafo:
    document.attach(str(i) + " -> " + str(grafo[i]) + html.BR())
