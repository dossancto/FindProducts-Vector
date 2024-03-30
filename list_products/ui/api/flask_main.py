import json
from flask import Flask, jsonify, request

from application.products.usecases.search_product.search_product_usecase import SearchProductUseCase

App = Flask(__name__)

@App.route('/products/<name>', methods=['GET'])
def update_employee(name: str):
    search_usecase = SearchProductUseCase()

    products = search_usecase.by_similiaritty(name, "tu")

    return jsonify(products)
