from infra.databases.chroma.repositories.chroma_products_repository import ChromaProductRepository
from domain.products.entities.product import Product
from application.products.usecases.save_product.save_product_usecase import SaveProductUseCase
from application.products.usecases.save_product.save_product_dtos import SaveProductInput
from utils.load_env import load_env_variables

load_env_variables()

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
