import discord
from config import TOKEN
from randompassword import gen_pass
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.bot(command_prefix="$", intens=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Selam! Ben {bot.user}, bir Discord sohbet botuyum)
                   
@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def password(ctx):
    await ctx.send("Rastgele Şifreniz:" + gen_pass(10))


bot.run(TOKEN)
