from sqlalchemy import Column, Integer, DateTime, Float, Boolean
from datetime import datetime
from typing import Union

from model import Base

class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column('pk_prediction', Integer, primary_key = True)
    male = Column(Boolean, unique=False, default=False)
    age =  Column(Integer)
    education = Column(Float)
    current_smoker = Column(Boolean, unique=False, default=False)
    cigs_per_day = Column(Float)
    bp_meds = Column(Float)
    prevalent_stroke =  Column(Boolean, unique=False, default=False)
    prevalent_hyp = Column(Boolean, unique=False, default=False)
    diabetes = Column(Boolean, unique=False, default=False)
    tot_chol = Column(Float)
    sys_bp = Column(Float)
    dia_bp = Column(Float)
    bmi = Column(Float)
    heart_rate = Column(Float)
    glucose = Column(Float)
    ten_year_chd = Column(Boolean, unique=False, default=False)
    date_insertion = Column(DateTime, default = datetime.now())

    def __init__(self, male:bool, age:int, education:float,
                 current_smoker:bool, cigs_per_day:float, bp_meds:float,
                 prevalent_stroke:bool, prevalent_hyp:bool, diabetes:bool,
                 tot_chol:float, sys_bp:float, dia_bp:float, bmi:float,
                 heart_rate:float, glucose:float, ten_year_chd:bool,
                 created_at:Union[DateTime, None] = None):
        '''
            Cria uma predição
            Arguments:
            male: se a pessoa é do sexo masculino (1) ou feminino (0);
            age: idade;
            education: nível de educação, quanto maior, significa que a 
                pessoa tem um nível mais elevado de educação formal;
            current_smoker: fumante no momento da coleta dos dados;
            cigs_per_day: cigarros consumidos por dia, caso fumante;
            bp_meds: se a pessoa estava usando ou não medicamento para
                regulação da pressão sanguínea;
            prevalent_stroke: se a pessoa teve ou não um ataque cardíaco
                anteriormente;
            prevalent_hyp: se a pessoa possuía, na data, hipertensão;
            diabetes: se a pessoa era diabética ou não na data;
            tot_chol: nível total de colesterol;
            sys_bp: pressão arterial sistólica;
            dia_bp: pressão arterial diastólica;
            bmi: índice de massa corporal;
            heart_rate: batimentos cardíacos;
            glucose: nível de glicose no sangue;
            ten_year_chd: coluna de saída, risco de a pessoa ter doença 
                cardíaca em 10 anos, sim (1) ou não (0);
            created_at: data na qual foi realizada a predição e
                adicionada ao banco de dados.
        '''
        self.male = male
        self.age = age
        self.education = education
        self.current_smoker = current_smoker
        self.cigs_per_day = cigs_per_day
        self.bp_meds = bp_meds
        self.prevalent_stroke = prevalent_stroke
        self.prevalent_hyp = prevalent_hyp
        self.diabetes = diabetes
        self.tot_chol = tot_chol
        self.sys_bp = sys_bp
        self.dia_bp = dia_bp
        self.bmi = bmi
        self.heart_rate = heart_rate
        self.glucose = glucose
        self.ten_year_chd = ten_year_chd
        self.created_at = created_at
