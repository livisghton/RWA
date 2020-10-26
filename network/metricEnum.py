
class Metric():

    def __init__(self):
        self.metric = {
            'RANDOM': "RA",
            'FIST_FIT': "FF",
            'LEAST_USED': "LU",
            'MOST_USED': "MU",
            'MIN_PRODUCT': "MP",
            'LEAST_LOADED': "LL",
            'MAX_SUM': "MS",
            'RELATIVE_CAPACITY_LOSS': "RCL",
            'WAVELENGTH_RESERVATION': "WR",
            'PROTECTING_THRESHOLD': "PT"
        }

    def selectMestric(self, metric):
        try:
            return self.metric[metric]
        except:
            print("A métrica %s não existe." % (metric))
            quit()

    
    