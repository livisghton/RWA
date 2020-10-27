import routing_algorithm.dijkstra as dijkstra
import network.lightpath as lightpath
import network.metricEnum as metric
import network.service as service
import json

lspId = 0

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


def creatLsp(service, lspList, path, metric):
    """
    Cria um lsp para o serviço, conforme a metrica escolhida.
    """

    lsp = lightpath.Lightpath(lspId, service.getId(), path )
    lspId += 1

    if(metric == "RA"):
        print("executa o algoritmo RANDOM")
    elif(metric == "FF"):
        print("executa o algoritmo Fist Firt")
    elif(metric == "LU"):
        print("executa o algoritmo Least Used")
    elif(metric == "MU"):
        print("executa o algoritmo Most Used")
    elif(metric == "MP"):
        print("executa o algoritmo Min Product")
    elif(metric == "LL"):
        print("executa o algoritmo Least Loaded")
    elif(metric == "MS"):
        print("executa o algoritmo Max Sun")
    elif(metric == "RCL"):
        print("executa o algoritmo Relative Capacity Loss")
    elif(metric == "WR"):
        print("executa o algoritmo Wavelength Reservation")
    else:
        print("executa o algoritmo Protecting threshold")

    return lsp


def run():

    # Carrega as entradas para do projeto
    data = None
    with open("test/test1.json", "r") as json_file:
        data = json.load(json_file)
    
    #lista de lsp no projeto
    lspList = []

    #seleciona o algortmo que será utilizado para alocação do comprimento de onda
    m = metric.Metric()
    algorithm =  m.selectMestric(data['metric'])

    #Carrega a lista de serviço e encontra e um comprimento de onda conforme a metrica escolhida
    requestList = data['request_list']
    serviceList = loadService(requestList)

    dj =  dijkstra.Dijkstra(data['grafo'])

    for s in serviceList:
        s.toString()
        path = dj.dijkstra_path(s.getSource() , s.getDestiny())
        lsp = creatLsp(s, lspList, path, m)
        lsp.getId()
        lspList.append(lsp)


    # for i in range( len( requestList ) ):
    #     request = requestList[i]

    #     print("Serviço: %s, origem: %s, destino: %s :" % (request['id'], request['source'], request['destiny']) )
    #     path = dj.dijkstra_path(request['source'], request['destiny'])

    #     lsp = lightpath.Lightpath()
    #     print()



if __name__ == "__main__":
    run()