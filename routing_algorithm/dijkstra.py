
class Dijkstra():

    def __init__(self, grafo):
        """
        Inicializa o construtor do Dijkstra.
        """
        self.grafo = grafo

    def dijkstra_path(self, origem, fim):
        """
        retorna a menor distancia de um No origem até um No destino e o caminho até ele
        """

        controle = {}
        distanciaAtual = {}
        noAtual = {}
        naoVisitados = []
        atual = origem
        noAtual[atual] = 0

        for vertice in self.grafo.keys():
            # inclui os vertices nos não visitados
            naoVisitados.append(vertice)
            # inicia os vertices como infinito
            distanciaAtual[vertice] = float('inf')

        distanciaAtual[atual] = [0, origem]

        naoVisitados.remove(atual)

        while naoVisitados:
            for vizinho, peso in self.grafo[atual].items():
                pesoCalc = peso + noAtual[atual]
                if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                    distanciaAtual[vizinho] = [pesoCalc, atual]
                    controle[vizinho] = pesoCalc
                    # print(controle)

            if controle == {}:
                break
            # seleciona o menor vizinho
            minVizinho = min(controle.items(), key=lambda x: x[1])
            atual = minVizinho[0]
            noAtual[atual] = minVizinho[1]
            naoVisitados.remove(atual)
            del controle[atual]

        print("A menor distância de %s atá %s é: %s" % (origem, fim, distanciaAtual[fim][0]))
        path = self.printPath(distanciaAtual, origem, fim)
        print("O menor caminho é: %s" % path)
        
        return path

    # retorna a menor distancia de um dado nó para todos os outros possíveis.
    def dijkstra(self, origem):

        controle = {}
        distanciaAtual = {}
        noAtual = {}
        naoVisitados = []
        atual = origem
        noAtual[atual] = 0

        for vertice in self.grafo.keys():
            # inclui os vertices nos não visitados
            naoVisitados.append(vertice)
            # inicia os vertices como infinito
            distanciaAtual[vertice] = float('inf')

        distanciaAtual[atual] = 0

        naoVisitados.remove(atual)

        while naoVisitados:
            for vizinho, peso in self.grafo[atual].items():
                pesoCalc = peso + noAtual[atual]
                if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho] > pesoCalc:
                    distanciaAtual[vizinho] = pesoCalc
                    controle[vizinho] = distanciaAtual[vizinho]

            if controle == {}:
                break
            # seleciona o menor vizinho
            minVizinho = min(controle.items(), key=lambda x: x[1])
            atual = minVizinho[0]
            noAtual[atual] = minVizinho[1]
            naoVisitados.remove(atual)
            del controle[atual]

        print(distanciaAtual)


    def printPath(self, distancias, inicio, fim):
        """
        Imprime o caminho encontrado no Dijkstra.
        """
        path = []

        atual = fim
        path.append(fim)
        flag = True
        while(flag):
            p = distancias[atual][1]
            if(p == inicio):
                flag = False
                path.append(p)
            else:
                path.append(p)
                atual = p

        return path[::-1]
