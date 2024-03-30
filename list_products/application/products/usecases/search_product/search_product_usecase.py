from typing import List
from application.products.usecases.save_product.save_product_dtos import SaveProductInput
from application.products.data.ProductRepository import ProductRepository
from domain.products.entities.product import Product
from infra.databases.chroma.repositories.chroma_products_repository import ChromaProductRepository


class SearchProductUseCase:

    def __init__(self, productRepository: ProductRepository = ChromaProductRepository()):
        self.productRepository = productRepository

    def by_similiaritty(self, name: str, creator: str):
      return self.productRepository.search_by_similiarity([name], creator)