import os
from dataclasses import dataclass

@dataclass
class ENV:
  def OPENAI_API_KEY():
     return os.getenv("OPENAI_API_KEY")