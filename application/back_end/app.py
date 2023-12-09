from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from unidecode import unidecode
from urllib.parse import unquote
import logging

from sqlalchemy.exc import IntegrityError

from model import Session, Prediction, TrainedModel
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title = 'Sistema Preditor de Doenças Cardíacas', version = '1.0.0')
app = OpenAPI(__name__, info = info)
CORS(app)

home_tag = Tag(name = 'Documentação', description = 'Seleção de documentação: Swagger, Redoc ou RapiDoc')
predictor_tag = Tag(name = 'Predição', description = 'Adição, visualização e remoção de casos de predição de doenças coronárias')

@app.get('/', tags = [home_tag])
def home():
    '''
        Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    '''

    return redirect('/openapi')

@app.post('/add_prediction', tags = [predictor_tag],
          responses = {'200': PredictionViewSchema, '409': ErrorSchema, '400': ErrorSchema})
def add_prediction(form: PredictionSchema):
    '''
        Adiciona uma nova predição à base de dados
        Retorna uma representação das predições.
    '''
    trained_model = TrainedModel
    trained_model_path = 'trained_model/trained_model.pkl'
    model = trained_model.load_trained_model(trained_model_path)

    logger.debug(f'the form: {form}')

    prediction = Prediction(
        name = form.name.strip(),
        male = form.male,
        age = form.age,
        education = form.education,
        current_smoker = form.current_smoker,
        cigs_per_day = form.cigs_per_day,
        bp_meds = form.bp_meds,
        prevalent_stroke = form.prevalent_stroke,
        prevalent_hyp = form.prevalent_hyp,
        diabetes = form.diabetes,
        tot_chol = form.tot_chol,
        sys_bp = form.sys_bp,
        dia_bp = form.dia_bp,
        bmi = form.bmi,
        heart_rate = form.heart_rate,
        glucose = form.glucose,
        ten_year_chd = trained_model.predictor(model, form)
    )
    logger.debug(f'Adicionando predição de nome: {prediction.name}')
    try:
        session = Session()
        session.add(prediction)
        session.commit()
        logger.debug(f'Adicionado predição de nome: {prediction.name}')

        return show_prediction(prediction), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = 'predição de mesmo nome já salvo na base :/'
        logger.warning(f'Erro ao adicionar predição {prediction.name}, {error_msg}')
        return {'mensagem': error_msg}, 409

    except Exception as e:
        error_msg = 'Não foi possível salvar novo item :/'
        logger.warning(f'Erro ao adicionar predição {prediction.name}, {error_msg}')
        return {'mensagem': error_msg}, 400

@app.get('/get_predictions', tags = [predictor_tag],
         responses = {'200': ListingPredictionsSchema, '404': ErrorSchema})
def get_predictions():
    '''
        Faz a busca por todas as predições cadastradas
        Retorna uma representação da listagem de predições.
    '''
    logging.getLogger('flask_cors').level = logging.DEBUG
    logger.debug(f'Coletando predições ')
    session = Session()
    predictions = session.query(Prediction).all()
    logger.debug(predictions)

    if not predictions:
        return {'predictions': []}, 200
    else:
        logger.debug(f'%d predições econtradas' % len(predictions))

        return show_predictions(predictions), 200

@app.get('/get_prediction', tags = [predictor_tag],
         responses = {'200': PredictionViewSchema, '404': ErrorSchema})
def get_prediction(query: PredictionNameSearchSchema):
    '''
        Faz a busca por uma predição a partir do nome do paciente.
        Retorna uma representação das predições.
    '''
    prediction_name = query.name
    logger.debug(f'Coletando dados sobre predição de paciente#{prediction_name}')
    session = Session()
    name_normalized = unidecode(prediction_name.lower())
    prediction = session.query(Prediction).filter(Prediction.name_normalized == name_normalized).first()

    if not prediction:
        error_msg = 'predição não encontrada na base :/'
        logger.warning(f'Erro ao buscar predição {prediction_name}, {error_msg}')
        return {'mensagem': error_msg}, 404
    else:
        logger.debug(f'predição econtrada: {prediction.name}')

        return show_prediction(prediction), 200

@app.delete('/del_prediction', tags = [predictor_tag],
            responses = {'200': PredictionDelSchema, '404': ErrorSchema})
def del_prediction(query: PredictionSearchSchema):
    '''
        Deleta um predição a partir do nome informado.
        Em razão de o nome do paciente ser único, a deleção pelo nome
        funcionará sem conflitos.
        Retorna uma mensagem de confirmação da remoção.
    '''
    prediction_name = query.name
    logger.debug(f'Deletando dados sobre predição #{prediction_name}')
    session = Session()
    count = session.query(Prediction).filter(Prediction.name == prediction_name).delete()
    session.commit()

    if count:
        logger.debug(f'Deletado predição #{prediction_name}')

        return {'mensagem': 'Predição removida', 'id': prediction_name}
    else:
        error_msg = 'Predição não encontrada na base :/'
        logger.warning(f'Erro ao deletar predição #{prediction_name}, {error_msg}')

        return {'mensagem': error_msg}, 404
