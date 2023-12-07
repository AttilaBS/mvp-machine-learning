from flask import jsonify, make_response

def response_product(product, code):
    show_product = [
        {'Nome': product.name},
        {'Quantidade': product.quantity},
        {'Preço': product.price}
    ]
    response = make_response(jsonify(show_product), code)
    response.headers['Content-Type'] = 'application/json'
    return response