from application.products.usecases.save_product.save_product_usecase import SaveProductUseCase
from application.products.usecases.save_product.save_product_dtos import SaveProductInput
import json
from flask import Flask, jsonify, request

from application.products.usecases.search_product.search_product_usecase import SearchProductUseCase

save_usecase = SaveProductUseCase()

inputs = [
    SaveProductInput(
        name="Azeite",
        creator_name="tu",
        description="Azeite natural"
    ),
    SaveProductInput(
        name="Monster",
        creator_name="tu",
        description="Energético para consumidores"
    )
]

save_usecase.execute_many(inputs)

App = Flask(__name__)

@App.route('/products/<name>', methods=['GET'])
def update_employee(name: str):
    search_usecase = SearchProductUseCase()

    products = search_usecase.by_similiaritty(name, "tu")

    return jsonify(products)

if __name__ == '__main__':
    App.run(debug=True)
