from utils.load_env import load_env_variables

import discord
from utils.envs import ENV
from application.products.usecases.save_product.save_product_usecase import SaveProductUseCase
from application.products.usecases.save_product.save_product_dtos import SaveProductInput

from application.products.usecases.search_product.search_product_usecase import SearchProductUseCase

load_env_variables()

save_usecase = SaveProductUseCase()

inputs = [
    SaveProductInput(
        name="Azeite",
        creator_name="tu",
        description="Azeite natural"
    ),
    SaveProductInput(
        name="Picanha",
        creator_name="tu",
        description="Picanha, uma carne nobre "
    ),
    SaveProductInput(
        name="Carvao",
        creator_name="tu",
        description="Carvao de eucalipto"
    ),
    SaveProductInput(
        name="Notebook Aspire 5, intel i5 de nona geração",
        creator_name="tu",
        description="Ótimo para devs python"
    ),
      SaveProductInput(
        name="Torta de maçã",
        creator_name="tu",
        description="Uma torta de maçã (sem carne)"
    ),
      SaveProductInput(
        name="Salada de Frutas",
        creator_name="tu",
        description="Uma salada de frutas com muita diversidade"
    ),
      SaveProductInput(
        name="Cachorro quente",
        creator_name="tu",
        description="Um cachorrro quente com bacon e farofa"
    ),
    SaveProductInput(
        name="Monster",
        creator_name="tu",
        description="Energético para consumidores"
    )
]

save_usecase.execute_many(inputs)
search_usecase = SearchProductUseCase()

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    content = message.content.lower()

    if not content.startswith("!product"):
      return;

    clean_content = content.replace("!product", "")

    result = search_usecase.by_similiaritty(clean_content, "tu")

    response_msg = ""

    for res in result:
      product = res.data
      response_msg += f"{product.name} - {product.description}\n"

    await message.channel.send(response_msg)


client.run(ENV.DISCORD_BOT_TOKEN())
