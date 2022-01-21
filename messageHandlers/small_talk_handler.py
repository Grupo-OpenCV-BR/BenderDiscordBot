from discord.ext import commands

class SmallTalkHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
   
    @commands.Cog.listener()
    async def on_message(self, message):
        text = message.content.lower()
        if message.author == self.bot.user:
            return

        elif "oi bender" in text:
            await message.channel.send("Oi, vamos tomar um Velho Fortran?")
        
        elif "boa noite" in text:
            await message.channel.send("Vai, humano!")
        
        elif "bom dia" in text:
            await message.channel.send("Tá com tempo, humano?")
        
        elif "boa tarde" in text:
            await message.channel.send("É, tá com muito tempo mesmo ?!?!")

        elif "delphi" in text:
            await message.channel.send("Delphi, tá de sacanagem né ?!?!")
        
        elif "muito bom" in text:
            await message.channel.send("Qualquer coisa abaixo da imortalidade é uma perda de tempo completa!")
        
        elif "ajuda" in text:
            await message.channel.send("Humanos... Sempre precisando de ajuda.. tsc.. tsc...")
        
        elif "obrigado" in text:
            await message.channel.send("Como posso ser tão ruim em tudo que tento e ainda ser melhor que vocês?")
        
        elif "java" in text:
            await message.channel.send("Java? Esse grupo já foi melhor, hein!")
        
        elif "php" in text:
            await message.channel.send("PHP? Você acordou de um coma?")

        elif "teoria" in text:
            await message.channel.send("Teoria? Tá brincando com a minha cara? "
                    + "Bora meter a mão na porra do código!")

        elif "excelente" in text:
            await message.channel.send("Excelente? Eu sei que sou, humanos...")

        elif "maquina" in text or "pc" in text or "computador" in text:
            await message.channel.send("Sendo sincero, se teu PC fosse um microondas, "
                    + "não rodava nem o prato.")

        elif "c++" in text:
            await message.channel.send("Vocês sabem o que o C++ disse para o C?"
                                        + "\n\n"
                                        + "Resposta: Você não tem classe!")

        elif "windows" in text:
            await message.channel.send("Herege, usando ruindows ...")

        elif "assembly" in text:
            await message.channel.send("Assembly? De qual período da pré-história é você?")

        elif "fortran" in text:
            await message.channel.send("Fortran ? É uma brasa mora!")

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')