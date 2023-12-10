import pandas as pd

class Loader:

    def load_data(self, url: str, attributes: list):
        ''' Carrega e retorna um DataFrame. Há diversos parâmetros
            no read_csv que poderiam ser utilizados para dar opções
            adicionais.
        '''
        return pd.read_csv(url, names=attributes,
                           skiprows=1, delimiter=',')
