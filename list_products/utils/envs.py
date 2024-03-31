import os
from dataclasses import dataclass

@dataclass
class ENV:
  def OPENAI_API_KEY():
     return os.getenv("OPENAI_API_KEY")

  def DISCORD_BOT_TOKEN():
     return os.getenv("DISCORD_BOT_TOKEN")