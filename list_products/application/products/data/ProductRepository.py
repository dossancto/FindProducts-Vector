from typing import List
from zope.interface import Interface 

from domain.products.entities.product import Product
from domain.general.SimiliarityData import SimiliarittyData

class ProductRepository(Interface):
  def save(entity: Product):
    "Save a new Product into database"
    pass

  def save_batch(entities: List[Product]) -> List[str]:
    "Save a list of Products at once in database"
    pass

  def search_by_similiarity(self, name: List[str], creator: str) -> List[SimiliarittyData[Product]]:
    "Search by similar products products"
    pass