from pydantic import BaseModel
from typing import Optional, List
from model.prediction import Prediction

from schemas import CommentarySchema

class PredictionSchema(BaseModel):
    '''
        Define como uma nova predição a ser inserida deve ser representada
    '''
    male: bool = 0
    age: int = 35
    education: float = 3.0
    current_smoker: bool = 1
    cigs_per_day: float = 10.0
    bp_meds: float = 0.0
    prevalent_stroke: bool = 1
    prevalent_hyp: bool = 0
    diabetes: bool = 1
    tot_chol: float = 145.0
    sys_bp: float = 106.0
    dia_bp: float = 80.0
    bmi: float = 26.45
    heart_rate: bool = 80.0
    glucose: bool = 79.0
    ten_year_chd: bool = 1

class ListingPredictionsSchema(BaseModel):
    '''
        Define como uma listagem de predições será retornada.
    '''
    get_Predictions: List[PredictionSchema]

def show_Predictions(Predictions: List[Prediction]):
    '''
        Retorna um representação da predição seguindo o esquema definido
        em PredictionViewSchema.
    '''
    result = []
    for Prediction in Predictions:
        result.append({
            'name': Prediction.name,
            'quantity': Prediction.quantity,
            'price': Prediction.price,
        })
    return {'Predictions': result}

class PredictionViewSchema(BaseModel):
    '''
        Define como uma predição será retornada.
    '''
    id: int = 1
    name: str = 'Banana Prata'
    quantity: Optional[int] = 12
    price: float = 12.50
    total_commentaries: int = 1
    commentaries: List[CommentarySchema]

class PredictionDelSchema(BaseModel):
    '''
        Define como deve ser a estrutura do dado retornado após uma
        requisição de remoção.
    '''
    message: str
    name: str

def show_Prediction(Prediction: Prediction):
    '''
        Retorna uma representação da predição seguindo o esquema definido
        em PredictionViewSchema.
    '''
    return {
        'id': Prediction.id,
        'name': Prediction.name,
        'quantity': Prediction.quantity,
        'price': Prediction.price,
        'total_commentaries': len(Prediction.commentaries),
        'commentary': [{'texto': c.texto} for c in Prediction.commentaries]
    }