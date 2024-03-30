from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass
class SimiliarittyData(Generic[T]):
  data: T
  distance: float
  