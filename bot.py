import discord
from discord.ext import commands
from config import DISCORD_TOKEN
from triggers import triggers
import random
from utils.gemini import generate_response

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Lunn te Vajj")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    for trigger in triggers:
        if trigger.match(message):
            await trigger.handle(message, bot)
            break  # respond to only one trigger per message

    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if random.randint(1,10) != 1: #respond to only 10% of the messages.
        return
    response = await generate_response(message.content)
    await message.reply(response)

bot.run(DISCORD_TOKEN)
