import routing_algorithm.dijkstra as dijkstra
import network.lightpath as lightpath
import network.metricEnum as metric
import network.service as service
import algorithm.rw
import json

def loadService(requestList):
    """
    Carrega a lista de serviços da rede.
    """

    serviceList = []

    for i in range( len( requestList ) ):
        request = requestList[i]
        s = service.Service(request['id'], request['source'], request['destiny'])
        serviceList.append(s)

    return serviceList


def creatLsp(service, lspList, path, _algorithm, lspId, useLambda):
    """
    Cria um lsp para o serviço, conforme a metrica escolhida.
    """
    lsp = None

    rw = algorithm.rw.Rw()
    lsp = rw.creatLsp(lspList, _algorithm, service, path, lspId, useLambda)

    return lsp

def createVectorLambdaUse(numChannel=80):
    """
    Cria um dicionário para checar contabilizar os lambdas.
    """
    useLambda = {}

    i = 1
    while( i <= numChannel ):
        useLambda.update({i: 0})
        i += 1
    
    return useLambda


def run():

    # Carrega as entradas para do projeto
    data = None
    with open("test/test1.json", "r") as json_file:
        data = json.load(json_file)
    
    #lista de lsp no projeto
    lspList = []

    #seleciona o algortmo que será utilizado para alocação do comprimento de onda
    m = metric.Metric()
    _algorithm =  m.selectMestric(data['metric'])

    #Carrega a lista de serviço e encontra e um comprimento de onda conforme a metrica escolhida
    requestList = data['request_list']
    serviceList = loadService(requestList)

    dj =  dijkstra.Dijkstra(data['grafo'])
    
    lspId = 0
    useLambda = createVectorLambdaUse()      #armazena a utilização dos lambdas da rede.

    for s in serviceList:
        s.toString()
        
        path = dj.dijkstra_path(s.getSource() , s.getDestiny())
        
        lsp = creatLsp(s, lspList, path, _algorithm, lspId, useLambda)
        lspId += 1
        lsp.toString()

        lspList.append(lsp)
        print()




if __name__ == "__main__":
    run()