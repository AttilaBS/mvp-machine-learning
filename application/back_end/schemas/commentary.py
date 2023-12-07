from pydantic import BaseModel

class CommentarySchema(BaseModel):
    '''
        Define como um novo comentário a ser inserido deve ser representado
    '''
    product_id: int = 1
    text: str = 'Só comprar se o preço realmente estiver bom!'