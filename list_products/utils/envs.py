import os
from dataclasses import dataclass

@dataclass
class ENV:

  @staticmethod
  def OPENAI_API_KEY() -> str:
     return __handle_env__("OPENAI_API_KEY")

  @staticmethod
  def DISCORD_BOT_TOKEN() -> str:
     return __handle_env__("DISCORD_BOT_TOKEN")

def __handle_env__(envname: str):
 env = os.getenv(envname)

 if env: return env

 raise Exception(f"<{envname}> environment variable not found")

