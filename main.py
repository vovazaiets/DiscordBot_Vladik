import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущений та готовий до роботи!')

@bot.command()
async def здоров(ctx):
    await ctx.reply("Здоров 🤖")

@bot.command()
async def розкажи_анекдот(ctx):
    await ctx.reply("Один хлопчик не вмів вимовляти слово шість. Прийшов якось одного разу в магазин і каже продавцеві:\n\n— Дайте мені сім пачок масла, одну не треба.")

bot.run(TOKEN)
