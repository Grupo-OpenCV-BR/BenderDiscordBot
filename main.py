from discord.ext import commands
import discord
import os

from messageHandlers.small_talk_handler import SmallTalkHandler
from messageHandlers.greetings_handler import Greetings


intents = discord.Intents.all()

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['>?', 'lol ', '!?']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

bender = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example', intents=intents)

@bender.event
async def on_ready():
    print('Foi')

bender.add_cog(SmallTalkHandler(bender))
bender.add_cog(Greetings(bender))

bender.run(os.getenv('TOKEN'))