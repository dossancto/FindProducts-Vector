from dataclasses import dataclass

from domain.products.entities.product import Product

@dataclass
class SaveProductInput:
  name: str
  description:str

  creator_name: str

  def to_product(self):
    return Product(
      id="",
      name=self.name,
      description=self.description,
      creator_name=self.creator_name,
      search_field=(self.name + self.description)
    )