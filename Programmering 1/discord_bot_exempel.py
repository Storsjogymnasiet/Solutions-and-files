import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

# Här sätter vi prefixet till komma (,)
bot = commands.Bot(command_prefix=',', intents=intents)

@bot.event
async def on_ready():
    print(f'Inloggad som {bot.user}')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Ditt nya kommando ,hej
@bot.command()
async def hej(ctx):
    await ctx.send('Hallå där! Hur kan jag hjälpa dig?')

# Kommandot ,namn
@bot.command()
async def namn(ctx):
    await ctx.send('Jag heter bot')

# Kommandot ,ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

bot.run('tokenhär')
