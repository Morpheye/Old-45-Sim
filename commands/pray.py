import discord
from discord.ext import commands
from db_functions import add_kriddytoo_shrine_boost, get_level
import random

@commands.command(name = "pray", aliases = ["kriddytooshrine"], description = "Pray to the KRiddytoo shrine")
@commands.bot_has_permissions(send_messages=True)
@commands.guild_only()
@commands.cooldown(1, 300, commands.BucketType.user)
async def pray(ctx):

    if await get_level(ctx.author.id) < 10:
        return await ctx.send(f"**{ctx.author}**, praying to the KRiddytoo shrine requires **level 10**")

    amount = random.randint(5,10)

    await add_kriddytoo_shrine_boost(ctx.author.id, amount)

    em = discord.Embed(title = "KRiddytoo Shrine", description = f"{ctx.author}, you prayed to the KRiddytoo shrine.", color = ctx.author.color)

    em.add_field(name = "**Precision Boost**", value = f"Your next **{amount}** double or triple 45s will be slightly boosted in precision.")

    await ctx.send(embed = em)


def setup(bot):
    bot.add_command(pray)