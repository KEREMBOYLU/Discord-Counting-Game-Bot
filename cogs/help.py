import discord
from discord.abc import User
from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

     

    @commands.command(name="help", aliases=["yardım"])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def help(self, ctx:commands.Context):
        user = (f"{ctx.author.name}#{ctx.author.discriminator}")
        embed=discord.Embed(title="SAYI SAYMA BOTU YARDIM PANELİ", color=0x00FFFF)
        embed.set_author(name=f"{user}", icon_url= ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/860895495774011402/dabcf6b15dbecf22663cf41f4ce44152.webp?size=1024")
        embed.add_field(name="!kanal_ayarla <kanal>", value="Sayı Sayma oyunu kurulumunu yapar", inline=False)
        embed.add_field(name="!kanal_kaldır <kanal>", value="Sayı Sayma oyunu kurulumunu kaldırır", inline=False)
        embed.set_footer(text="Made by Kensens", icon_url="https://cdn.discordapp.com/avatars/860895495774011402/dabcf6b15dbecf22663cf41f4ce44152.webp?size=1024")
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))