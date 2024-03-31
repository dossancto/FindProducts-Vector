from infra.databases.chroma.repositories.chroma_products_repository import ChromaProductRepository
from domain.products.entities.product import Product
from application.products.usecases.save_product.save_product_usecase import SaveProductUseCase
from application.products.usecases.search_product.search_product_usecase import SearchProductUseCase
from application.products.usecases.save_product.save_product_dtos import SaveProductInput
from utils.load_env import load_env_variables

load_env_variables()

save_usecase = SaveProductUseCase()

inputs = [
    SaveProductInput(
        name="Azeite",
        creator_name="tu",
        description="Azeite natural, tempero"
    ),
    SaveProductInput(
        name="Monster",
        creator_name="tu",
        description="Energético para consumidores"
    )
]

product_ids = save_usecase.execute_many(inputs)

print(product_ids)

search_product = SearchProductUseCase()

products = search_product.by_similiaritty("Tempero para comida", "tu")

for res in products:
    prod = res.data

    print(f"{prod.name} - {res.distance}")