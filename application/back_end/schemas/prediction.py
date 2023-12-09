from pydantic import BaseModel
from typing import List
from model.prediction import Prediction
from datetime import datetime

class PredictionSchema(BaseModel):
    '''
        Define como uma nova predição a ser inserida deve ser representada
    '''
    name: str = 'Eduardo'
    male: int = 0
    age: int = 35
    education: float = 3.0
    current_smoker: int = 1
    cigs_per_day: float = 10.0
    bp_meds: float = 1.0
    prevalent_stroke: int = 1
    prevalent_hyp: int = 0
    diabetes: int = 1
    tot_chol: float = 145.0
    sys_bp: float = 106.0
    dia_bp: float = 80.0
    bmi: float = 26.45
    heart_rate: float = 80.0
    glucose: float = 79.0
    ten_year_chd: int = 1

class ListingPredictionsSchema(BaseModel):
    '''
        Define como uma listagem de predições será retornada.
    '''
    predictions: List[PredictionSchema]

def show_predictions(predictions: List[Prediction]):
    '''
        Retorna um representação da predição seguindo o esquema definido
        em PredictionViewSchema.
    '''
    result = []
    for prediction in predictions:
        result.append({
            'name': prediction.name,
            'male': prediction.male,
            'age': prediction.age,
            'education': prediction.education,
            'current_smoker': prediction.current_smoker,
            'cigs_per_day': prediction.cigs_per_day,
            'bp_meds': prediction.bp_meds,
            'prevalent_stroke': prediction.prevalent_stroke,
            'prevalent_hyp': prediction.prevalent_hyp,
            'diabetes': prediction.diabetes,
            'tot_chol': prediction.tot_chol,
            'sys_bp': prediction.sys_bp,
            'dia_bp': prediction.dia_bp,
            'bmi': prediction.bmi,
            'heart_rate': prediction.heart_rate,
            'glucose': prediction.glucose,
            'date_insertion': prediction.date_insertion,
            'ten_year_chd': prediction.ten_year_chd,
        })
    return {'predictions': result}

class PredictionDelSchema(BaseModel):
    '''Define como os dados de uma predição para deleção serão representados
    '''
    name: str = 'Otávio'

class PredictionNameSearchSchema(BaseModel):
    '''
        Define como será a busca de uma predição apenas pelo nome.
    '''
    name: str = 'Otávio'

class PredictionSearchSchema(BaseModel):
    '''
        Define como será a busca de uma predição pelo nome.
    '''
    name: str = 'João'

class PredictionViewSchema(BaseModel):
    '''
        Define como será a visualização de uma predição.
    '''
    name: str
    male: int
    age: int
    education: float
    current_smoker: int
    cigs_per_day: float
    bp_meds: float
    prevalent_stroke: int
    prevalent_hyp: int
    diabetes: int
    tot_chol: float
    sys_bp: float
    dia_bp: float 
    bmi: float
    heart_rate: float
    glucose: float
    date_insertion: datetime
    ten_year_chd: int

class PredictionDelSchema(BaseModel):
    '''
        Define como deve ser a estrutura do dado retornado após uma
        requisição de remoção.
    '''
    message: str
    nome: str

def show_prediction(prediction: Prediction):
    '''
        Retorna uma representação da predição seguindo o esquema definido
        em PredictionViewSchema.
    '''
    return {
        'name': prediction.name,
        'male': prediction.male,
        'age': prediction.age,
        'education': prediction.education,
        'current_smoker': prediction.current_smoker,
        'cigs_per_day': prediction.cigs_per_day,
        'bp_meds': prediction.bp_meds,
        'prevalent_stroke': prediction.prevalent_stroke,
        'prevalent_hyp': prediction.prevalent_hyp,
        'diabetes': prediction.diabetes,
        'tot_chol': prediction.tot_chol,
        'sys_bp': prediction.sys_bp,
        'dia_bp': prediction.dia_bp,
        'bmi': prediction.bmi,
        'heart_rate': prediction.heart_rate,
        'glucose': prediction.glucose,
        'date_insertion': prediction.date_insertion,
        'ten_year_chd': prediction.ten_year_chd
    }
