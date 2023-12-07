from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Prediction
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title = 'Sistema Preditor de Doenças Cardíacas', version = '1.0.0')
app = OpenAPI(__name__, info = info)
CORS(app)

#definindo tags
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
    prediction = Prediction(
        name = form.name,
        quantity = form.quantity,
        price = form.price)
    logger.debug(f'Adicionando predição de nome: {prediction.name}')
    try:
        # criando conexão com a base
        session = Session()
        # adicionando predição
        session.add(prediction)
        # efetivando o chamado de adição de novo item na tabela
        session.commit()
        logger.debug(f'Adicionado predição de nome: {prediction.name}')
        return show_prediction(prediction), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = 'predição de mesmo nome já salvo na base :/'
        logger.warning(f'Erro ao adicionar predição {prediction.name}, {error_msg}')
        return {'mensagem': error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
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
    logger.debug(f'Coletando predições ')
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    predictions = session.query(Prediction).all()

    if not predictions:
        # se não há prediçãos cadastrados
        return {'predictions': []}, 200
    else:
        logger.debug(f'%d prediçãos econtrados' % len(predictions))
        # retorna a representação de predição
        print(predictions)
        return show_predictions(predictions), 200

@app.get('/prediction', tags = [predictor_tag],
         responses = {'200': PredictionViewSchema, '404': ErrorSchema})
def get_prediction(query: PredictionSearchSchema):
    '''
        Faz a busca por uma predição a partir do id da predição
        Retorna uma representação das predições.
    '''
    prediction_id = query.id
    logger.debug(f'Coletando dados sobre predição #{prediction_id}')
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    prediction = session.query(prediction).filter(prediction.id == prediction_id).first()

    if not prediction:
        # se o predição não foi encontrado
        error_msg = 'predição não encontrado na base :/'
        logger.warning(f'Erro ao buscar predição {prediction_id}, {error_msg}')
        return {'mensagem': error_msg}, 404
    else:
        logger.debug(f'predição econtrado: {prediction.name}')
        # retorna a representação de predição
        return show_prediction(prediction), 200

@app.delete('/prediction', tags = [predictor_tag],
            responses = {'200': PredictionDelSchema, '404': ErrorSchema})
def del_prediction(query: PredictionSearchSchema):
    '''
        Deleta um predição a partir do nome de predição informado
        Retorna uma mensagem de confirmação da remoção.
    '''
    prediction_name = unquote(unquote(query.name))
    logger.debug(f'Deletando dados sobre predição #{prediction_name}')
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(prediction).filter(prediction.name == prediction_name).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f'Deletado predição #{prediction_name}')
        return {'mensagem': 'Predição removida', 'id': prediction_name}
    else:
        # se a predição não foi encontrada
        error_msg = 'Predição não encontrada na base :/'
        logger.warning(f'Erro ao deletar predição #{prediction_name}, {error_msg}')
        return {'mensagem': error_msg}, 404
