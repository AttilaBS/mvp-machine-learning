from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base

class Commentary(Base):
    __tablename__ = 'commentary'

    id = Column(Integer, primary_key = True)
    text = Column(String(4000))
    author = Column(String(400))
    n_stars = Column(Integer)
    date_insertion = Column(DateTime, default = datetime.now())

    # Definição do relacionamento entre o comentário e um produto.
    # Aqui está sendo definido a coluna 'product' que vai guardar
    # a referencia ao produto, a chave estrangeira que relaciona
    # um produto ao comentário.
    product = Column(Integer, ForeignKey("product.pk_product"), nullable = False)

    def __init__(self, author:str, text:str, n_stars:int = 0, date_insertion:Union[DateTime, None] = None):
        """
        Cria um Comentário
        Arguments:
            texto: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.author = author
        self.text = text
        self.n_stars = n_stars
        if date_insertion:
            self.date_insertion = date_insertion
