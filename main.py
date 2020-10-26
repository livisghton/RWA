import routing_algorithm.dijkstra as dijkstra
import network.lightpath as lightpath
import json
import network.metricEnum as metric


def run():

    # Carrega as entradas para do projeto
    data = None
    with open("test/test1.json", "r") as json_file:
        data = json.load(json_file)


    #seleciona o algortmo que será utilizado para alocação do comprimento de onda
    m = metric.Metric()
    algorithm =  m.selectMestric(data['metric'])

    #Carrega a lista de serviço e encontra e um comprimento de onda conforme a metrica escolhida
    requestList = data['request_list']

    dj =  dijkstra.Dijkstra(data['grafo'])

    for i in range( len( requestList ) ):
        request = requestList[i]

        print("Serviço: %s, origem: %s, destino: %s :" % (request['id'], request['source'], request['destiny']) )
        path = dj.dijkstra_path(request['source'], request['destiny'])

        lsp = lightpath.Lightpath()
        print()



if __name__ == "__main__":
    run()