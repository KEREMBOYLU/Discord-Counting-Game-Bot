from sqlite3.dbapi2 import Error
from discord.ext.commands import cog
import math
from os import name
import sqlite3
import asyncio
import discord
from discord import client
from discord.ext import commands
import os



class ayarlar(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command(name="kanal_ayarla")
    @commands.has_permissions(administrator=True)
    async def kayarla(self, ctx, channel_id):
        try:
                chnl = int(channel_id[2:-1])
        except:
            await ctx.send(f"Girdiğiniz kanal yanlış, Girmeniz gereken kanal şu şekilde olmalı: `{ctx.channel.mention}`")
            return

        channel = self.bot.get_channel(chnl)

        db = sqlite3.connect("counting.db")
        cursor = db.cursor()
        tuple = [0,channel.id,ctx.guild.id,None]
        cursor.execute(f"INSERT INTO sayi VALUES (?,?,?,?)",tuple)
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("✅ Başarılı bir şekilde tamamlanmıştır.")

    @commands.command(name="kanal_kaldır")
    @commands.has_permissions(administrator=True)
    async def kkaldır(self, ctx, channel_id):
        try:
                chnl = int(channel_id[2:-1])
        except:
            await ctx.send(f"Girdiğiniz kanal yanlış, Girmeniz gereken kanal şu şekilde olmalı: `{ctx.channel.mention}`")
            return

        channel = self.bot.get_channel(chnl)

        db = sqlite3.connect("counting.db")
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM sayi WHERE Kanal = {channel.id}")
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("✅ Başarılı bir şekilde tamamlanmıştır.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("🔒 Bu komutu çalıştırmak için gerekli izinlere sahip değilsiniz")


def setup(bot:commands.Bot):
    bot.add_cog(ayarlar(bot))