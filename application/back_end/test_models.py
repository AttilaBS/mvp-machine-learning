from model.evaluator import Evaluator
from model.loader import Loader
from model.trained_model import TrainedModel

# To run: pytest -v test_modelos.py

# Instanciação das Classes
loader = Loader()
trained_model = TrainedModel()
evaluator = Evaluator()

# Parâmetros
url_data = "database/diabetes_golden.csv"
columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# Carga dos dados
dataset = loader.load_data(url_data, columns)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_trained_model():  
    # Importando o modelo de regressão logística
    model_path = 'trained_model/trained_model.pkl'
    model_lr = trained_model.load_trained_model(model_path)

    # Obtendo as métricas da Regressão Logística
    accuracy_lr, recall_lr, precision_lr, f_one_lr = evaluator.evaluate(model_lr, X, Y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert accuracy_lr >= 0.75 
    assert recall_lr >= 0.5 
    assert precision_lr >= 0.5 
    assert f_one_lr >= 0.5 
 
# Método para testar modelo KNN a partir do arquivo correspondente
def test_model_knn():
    # Importando modelo de KNN
    knn_path = 'trained_model/trained_model.pkl'
    model_knn = trained_model.load_trained_model(knn_path)

    # Obtendo as métricas do KNN
    acuracy_knn, recall_knn, precision_knn, f_one_knn = evaluator.evaluate(model_knn, X, Y)
    
    # Testando as métricas do KNN
    # Modifique as métricas de acordo com seus requisitos
    assert acuracy_knn >= 0.75
    assert recall_knn >= 0.5 
    assert precision_knn >= 0.5 
    assert f_one_knn >= 0.5 
