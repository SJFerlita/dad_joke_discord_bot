import os

import requests
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='joke', help='Tells a dad joke!')
async def joke_cmd(ctx):

    url = "https://www.icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "application/json"})
    joke_data = response.json()

    dad_joke = joke_data.get('joke')
    await ctx.send(dad_joke)

bot.run(TOKEN)