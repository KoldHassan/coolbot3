import os
import random
import discord
import asyncio
import keep_alive
from discord.ext import commands
from makedictionaries import make_dictionaries

client = commands.Bot(command_prefix="3")

wisdom = make_dictionaries()

# change status
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(activity=discord.Game("3help"))


@client.command()
async def Hello(ctx):
    await ctx.send("Hi")



# all of the wisdoms

@client.command(name='karenwisdom', help="Valuable wisdom from Karen Hunnicutt herself")
async def karenwisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Karen"])
        await ctx.send(response)
        i += 1


keep_alive.keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
