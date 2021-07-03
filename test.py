from asyncio.tasks import sleep
import math
from os import name, stat
from random import choice, random
import sqlite3
import asyncio
import discord
from discord import client
from discord.enums import ActivityType
from discord.ext import commands
import os
import random


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")
TOKEN = open("token.txt", "r").read()

async def status():
    while True:
        await bot.wait_until_ready()
        await bot.change_presence(activity=discord.Game(name=f"{len(bot.guilds)} sunucu | !help"))
        await sleep(5)
        await bot.change_presence(activity=discord.Streaming(name=f"Twitch Erm00n", url=("https://www.twitch.tv/erm00n")))
        await sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=(f"Kensens")))
        await sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(f"Youtube Erm00n")))
        await sleep(5)
@bot.event
async def on_ready():
    db = sqlite3.connect("counting.db")
    print("bağlantı oluşturuldu")
    cursor = db.cursor()
    print("cursor oluşturuldu")
    cursor.execute("CREATE TABLE IF NOT EXISTS sayi(Sayı integer, Kanal TEXT, GuildID integer, LastUserID integer)")
    print("tablo oluşturuldu")
    db.commit()
    cursor.close()
    db.close()
    print(bot.user.name + " hazır.")
bot.loop.create_task(status())

    

@bot.command()
async def reload(ctx, extension):
    if not ctx.author.id == (459710185804660736):
        return
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('başarılı')

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)
