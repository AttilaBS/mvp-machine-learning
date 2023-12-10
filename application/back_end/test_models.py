from model.evaluator import Evaluator
from model.loader import Loader
from model.trained_model import TrainedModel

loader = Loader()
trained_model = TrainedModel()
evaluator = Evaluator()

url_data = 'golden_dataset/golden_dataset.csv'
columns = ['male', 'age', 'education', 'current_smoker', 'cigs_per_day', 'bp_meds', 'prevalent_stroke', 'prevalent_hyp', 'diabetes', 'tot_chol', 'sys_bp', 'dia_bp', 'bmi', 'heart_rate', 'glucose', 'ten_year_chd']

dataset = loader.load_data(url_data, columns)
entrance_array = dataset.values
X = entrance_array[:,0:15].astype(float)
Y = dataset.iloc[:, -1]

def test_trained_model():
    trained_model_path = 'trained_model/trained_model.pkl'
    model_lr = trained_model.load_pkl(trained_model_path)

    # Padronização nos dados de entrada usando o scaler utilizado em X
    scaler_path = 'trained_model/scaler.pkl'
    scaler = trained_model.load_pkl(scaler_path)
    X_scaled = scaler.transform(X)
    # Obtendo as métricas da Regressão Logística
    accuracy_lr, recall_lr, precision_lr, f_one_lr = evaluator.evaluate(model_lr, X_scaled, Y)

    assert accuracy_lr >= 0.75
    assert recall_lr >= 0.01
    assert precision_lr >= 0.5
    assert f_one_lr >= 0.05

def test_model_knn():
    knn_path = 'trained_model/trained_model.pkl'
    model_knn = trained_model.load_pkl(knn_path)

    # Obtendo as métricas do KNN
    acuracy_knn, recall_knn, precision_knn, f_one_knn = evaluator.evaluate(model_knn, X, Y)

    assert acuracy_knn >= 0.55
    assert recall_knn >= 0.5
    assert precision_knn >= 0.15
    assert f_one_knn >= 0.25
