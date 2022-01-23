from discord.ext import commands
import discord, os

from messageHandlers.small_talk_handler import SmallTalkHandler
from messageHandlers.greetings_handler import Greetings
from messageHandlers.generate_offense import generateOffense

last_authors = {}
intents = discord.Intents.all()

bender = commands.Bot(command_prefix='!!', description='A Rewrite Cog Example', intents=intents)

@bender.command()
async def offense_me(ctx):
    if ctx.author not in last_authors:
        await ctx.send(generateOffense())
        last_authors[ctx.author] = 1
    elif ctx.author in last_authors and last_authors[ctx.author] == 1 :
        await ctx.send("Seu degenerado! Pare de ficar spamando o server só por causa da sua síndrome de Estocolmo!")
        last_authors[ctx.author] += 1


@bender.event
async def on_ready():
    print('Foi')

bender.add_cog(SmallTalkHandler(bender))
bender.add_cog(Greetings(bender))

bender.run(os.getenv('TOKEN'))