from dataclasses import dataclass

@dataclass
class Product:
  id: str
  name: str
  description: str

  search_field: str

  creator_name: str
  