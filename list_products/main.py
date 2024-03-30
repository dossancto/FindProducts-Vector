from infra.databases.chroma.repositories.chroma_products_repository import ChromaProductRepository
from domain.products.entities.product import Product
from application.products.usecases.save_product.save_product_usecase import SaveProductUseCase
from application.products.usecases.save_product.save_product_dtos import SaveProductInput
from application.products.usecases.search_product.search_product_usecase import SearchProductUseCase
from utils.load_env import load_env_variables

import ui.api.flask_main

load_env_variables()

save_usecase = SaveProductUseCase()
search_usecase = SearchProductUseCase()

inputs = [
    SaveProductInput(
        name="Azeite",
        creator_name="tu"
    ),
    SaveProductInput(
        name="Monster",
        creator_name="tu"
    )
]

saved_product = save_usecase.execute_many(inputs)

# print(saved_product)

searched_product = search_usecase.by_similiaritty("Monstro", "tu")

for prod in searched_product:
    product = prod.data
    print(product.name, prod.distance)

if __name__ == '__main__':
    ui.api.flask_main.App.run(debug=True)