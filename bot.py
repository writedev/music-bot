from discord.ext import commands
import discord
import os 
import dotenv

dotenv.load_dotenv()

token = os.getenv('TOKEN')

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())
        
    async def on_ready(self):
        print(f'Logged in as {self.user.global_name} (ID: {self.user.id})')
        print('------')


bot = Bot()

bot.run(token)