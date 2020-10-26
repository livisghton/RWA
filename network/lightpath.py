class Lightpath():
    
    id = 0

    def __init__(self, serviceId, path):
        """
        Cria uma estrutura do lightpah.
        """
        self.setId(id)
        self.setServiceId(serviceId)
        self.setPath(path)
        self.waveLength = None


    def setId(self, id):
        """
        Seta o id do lightpah.
        """
        self.id = id

    def getId(self):
        """
        Retorna o id do lightpah.
        """
        return self.id
    
    def setServiceId(self, serviceId):
        """
        Seta o id do serviço no lightpah.
        """
        self.serviceId = serviceId
    
    def getServiceId(self):
        """
        Retorna o id do serviço que esta no lightpah.
        """
        return serviceId
    
    def setPath(self, path):
        """
        Seta o caminho do lightpah.
        """
        self.path = path
    
    def getPath(self):
        """
        Retorna o caminho do lightpah.
        """
        return self.path

    def setWaveLength(self, waveLength):
        """
        Seta um comprimento de onda no lightpah.
        """
        self.waveLength = waveLength
    
    def getWaveLength(self):
        """
        Retorna o comprimento de onda no lightpah.
        """
        return waveLength

    def str(self):
        print("Id: %s, Serviço: %s, Caminho: %s, Lambda: %s." % (self.getId, self.getServiceId, self.getPath, self.getWaveLength))