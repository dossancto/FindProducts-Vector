from typing import List
from application.products.usecases.save_product.save_product_dtos import SaveProductInput
from application.products.data.ProductRepository import ProductRepository
from domain.products.entities.product import Product
from infra.databases.chroma.repositories.chroma_products_repository import ChromaProductRepository


class SaveProductUseCase:

    def __init__(self, productRepository: ProductRepository = ChromaProductRepository()):
        self.productRepository = productRepository

    def execute(self, input: SaveProductInput):
        return self.productRepository.save(
            entity=input.to_product())

    def execute_many(self, input: List[SaveProductInput]):
        products = list(map(lambda x: x.to_product(), input))

        return self.productRepository.save_batch(products)
