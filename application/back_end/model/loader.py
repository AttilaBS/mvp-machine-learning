import pandas as pd

class Loader:

    def load_data(self, url: str, attributes: list):
        ''' Carrega e retorna um DataFrame. Há diversos parâmetros
            no read_csv que poderiam ser utilizados para dar opções
            adicionais.
        '''
        url_heart = 'https://raw.githubusercontent.com/AttilaBS/mvp-machine-learning/main/datasets/heart_dataset.csv'
        url_golden = 'https://raw.githubusercontent.com/AttilaBS/mvp-machine-learning/main/datasets/golden_dataset.csv'

        return pd.read_csv(url, names=attributes,
                           skiprows=1, delimiter=',') # Esses dois parâmetros são próprios para uso deste dataset. Talvez você não precise utilizar
