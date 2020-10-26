class Service():

    def __init__(self, id, source, destiny):
        """
        Cria uma estrutura do serviço.
        """
        self.setId(id)
        self.setSource(source)
        self.setDestiny(destiny)

    def setId(self, id):
        """
        Seta o Id do serviço.
        """
        self.id = id
    
    def getId(self):
        """
        Retorna o Id do serviço.
        """
        return self.id

    def setSource(self, source):
        """
        Seta a origem do serviço.
        """
        self.source = source
    
    def getSource(self):
        """
        Retorna a origem do serviço.
        """
        return self.source

    def setDestiny(self, destiny):
        """
        Seta a destino do serviço.
        """
        self.destiny = destiny
    
    def getDestiny(self):
        """
        Retorna o destino do serviço
        """
        return self.destiny