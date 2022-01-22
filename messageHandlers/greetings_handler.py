from discord.ext import commands
from .generateOffensePerson import set_xing

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(934531783037423636)
        if channel is not None:
            await channel.send('Olá {0.mention}! Seja bem vindo(a) ao Grupo OpenCV Brasil!.'.format(member) +
                               '\n\nLeia as regras do grupo em #regras (Se levar ban, não diga que eu não avisei, hein!)'+
                               '\n\nConheça nosso repositório de conteúdo gratuito: https://github.com/Grupo-OpenCV-BR/tutoriais-tecnologia' +
                               f'\n\n{set_xing(member.name)}')