
class Generation():

    def __init__(self):    
        """
        Geração de id's para o projeto
        """
        self.lspId = 0 
                

    def generationIdLsp(self, lspId):
        """
        Gera um id para um lsp.
        """
        return lspId + 1