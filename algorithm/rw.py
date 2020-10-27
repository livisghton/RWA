import random
import network.lightpath as lightpath
import util.generation

class Rw():
    def __init__(self):
        self.setNumChannel(80)        #foi definido o número de canais como 80 apenas para teste.

    def setNumChannel(self, numChannel):
        self.numChannel = numChannel

    def getNumChannel(self):
        return self.numChannel


    def creatLsp(self, lspList, algorithm, service, path, lspId):
        
        lsp = None

        if(algorithm == "RA"):
            #print("executa o algoritmo RANDOM")
            lsp = self.random(lspList, service, path, lspId)

        elif(algorithm == "FF"):
            # print("executa o algoritmo Fist Firt")
            lsp = self.firstFit(lspList, service, path, lspId)

        elif(algorithm == "LU"):
            print("executa o algoritmo Least Used")
        elif(algorithm == "MU"):
            print("executa o algoritmo Most Used")
        elif(algorithm == "MP"):
            print("executa o algoritmo Min Product")
        elif(algorithm == "LL"):
            print("executa o algoritmo Least Loaded")
        elif(algorithm == "MS"):
            print("executa o algoritmo Max Sun")
        elif(algorithm == "RCL"):
            print("executa o algoritmo Relative Capacity Loss")
        elif(algorithm == "WR"):
            print("executa o algoritmo Wavelength Reservation")
        else:
            print("executa o algoritmo Protecting threshold")

        return lsp

    
    def random(self, lspList, service, path, lspId):
        """
        Este método implementa o algoritmo random.
        """

        # generationId = util.generation.Generation()
        # lspId = generationId.generationIdLsp(lspId)

        lsp = lightpath.Lightpath( lspId, service.getId(), path )

        available = False
        while( not available ):
            _lambda =  random.randint(1, self.numChannel)

            dic = {}
            keyList = self.keyList(path)

            if(lspList == []):
                for j in keyList:
                    dic.update({j: _lambda})
                available = True
            else:
                if( self.lambdaAvailability(lspList, _lambda, keyList) ):
                    for j in keyList:
                        dic.update({j: _lambda})
                    available = True
                
        lsp.setWaveLength(dic)
        return lsp


    def firstFit(self, lspList, service, path, lspId):
        """
        Este método implementa o algoritmo First Fit.
        """

        lsp = lightpath.Lightpath( lspId, service.getId(), path )

        available = False
        _lambda = 0

        while( not available and _lambda < self.getNumChannel() ):
            _lambda += 1

            dic = {}
            keyList = self.keyList(path)

            if(lspList == []):
                for j in keyList:
                    dic.update({j: _lambda})
                available = True
            else:
                if( self.lambdaAvailability(lspList, _lambda, keyList) ):
                    for j in keyList:
                        dic.update({j: _lambda})
                    available = True
                
        lsp.setWaveLength(dic)
        return lsp


    def keyList(self, path):
        """
        Carrega a lista de chaves do caminho.
        """

        i = 0
        keyList = []
        while(i < len(path) and i+1 < len(path) ):
            key = None
            if(path[i] < path[i+1]):
                key = path[i] + path[i+1]
            else:
                key = path[i+1] + path[i]
            
            i += 1

            keyList.append(key)

        return keyList


    def lambdaAvailability(self, lspList, _lambda, keyList):
        """
        Verifica se o comprimento de onda já esta sendo utilizado.
        """
        
        available = True

        for lsp in lspList:
            for key in keyList:
                if( key in lsp.getWaveLength() ):
                    if( lsp.getWaveLength()[key] == _lambda):
                        return False
        return available

