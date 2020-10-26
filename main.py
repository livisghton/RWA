import routing_algorithm.dijkstra as dijkstra
import json

# grafo = {
#     "A" : { "B": 1, "C": 2 },
#     "B" : { "A": 1, "D": 2, "E": 4 },
#     "C" : { "A": 2, "E": 2 },
#     "D" : { "B": 2, "F": 6 },
#     "E" : { "B": 4, "C": 2, "F": 7 },
#     "F" : { "E": 7}
#     }

def run():
    # Carrega as entradas para do projeto
    data = None
    with open("test/test1.json", "r") as json_file:
        data = json.load(json_file)


    dj =  dijkstra.Dijkstra(data['grafo'])
    # dj =  dijkstra.Dijkstra(grafo)

    requestList = data['request_list']

    for i in range (len(requestList)):
        request = requestList[i]
        # print(request['source'])
        print("Serviço: %s, origem: %s, destino: %s :" % (request['id'], request['source'], request['destiny']) )
        dj.dijkstra_path(request['source'], request['destiny'])
        # dj.dijkstra(request['source'])

        # print(requestList[1])


if __name__ == "__main__":
    run()