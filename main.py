from discord.ext import commands
import discord, os, json, time

from messageHandlers.small_talk_handler import SmallTalkHandler
from messageHandlers.greetings_handler import Greetings
from messageHandlers.generate_offense import generateOffense

intents = discord.Intents.all()

bender = commands.Bot(command_prefix='!!', description='A Rewrite Cog Example', intents=intents)

def write_data(authors: dict):
    with open("blacklist.json", "w") as outfile:
        json.dump(authors, outfile)

def verify_black_list():
    f = open('blacklist.json')
    last_authors = json.load(f)
    authors = last_authors.keys()
    to_delete = []
    for author in authors:
        this_time = time.time()
        if this_time - last_authors[author]['msgTimeStamp'] >= 1800: #1800
            to_delete.append(author)
            #last_authors.pop(author, None)
    
    for a in to_delete:
        last_authors.pop(a, None)
    write_data(last_authors)

@bender.command()
async def offense_me(ctx):
    verify_black_list()
    f = open('blacklist.json')
    last_authors = json.load(f)
    if ctx.author.name not in last_authors:
        await ctx.send(generateOffense())
        last_authors[ctx.author.name] = {'msgCount': 1, 'msgTimeStamp': time.time()}
        write_data(last_authors)
    
    elif (ctx.author.name in last_authors) and (last_authors[ctx.author.name]['msgCount'] == 1) :
        await ctx.send("Seu degenerado! Pare de ficar spamando o server só por causa da sua síndrome de Estocolmo!")
        last_authors[ctx.author.name]['msgCount'] += 1
        write_data(last_authors)


@bender.event
async def on_ready():
    if not os.path.isfile('blacklist.json'):
        last_authors = {}
        write_data(last_authors)
    print('Done!')

bender.add_cog(SmallTalkHandler(bender))
bender.add_cog(Greetings(bender))

bender.run(os.getenv('TOKEN'))