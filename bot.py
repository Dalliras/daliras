import discord
from discord.ext import commands
import os

Bot = commands.Bot(command_prefix = "!" )

@Bot.event
async def on_ready ():
    print("Bot is online")

@Bot.command(pass_context= True)
async def Привет(ctx):
    await ctx.send("Привет, ты что то хотел?")

# Kick
@Bot.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick ( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason = reason )
    await ctx.send( f'{ member.mention } был успешно кикнут!' )

# Ban
@Bot.command()
async def ban(ctx, member:discord.Member, day:int):
  await ctx.send(f'Пользователь {member.name} получил бан на {day} день/дней')
  await member.ban()
  await asyncio.sleep(day)
  await member.unban()

# Unban    
@Bot.command( pass_context = True )

async def unban( ctx, *, member ):
    await ctx.channel.purge( limit = 1 )

    banned_useres = await ctx.guild.band()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban( user )
        await ctx.send( f'{ user.mention } был успешно разбанен!')

        return

import asyncio

await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = f"на {servers} серверов"))
   await asyncio.sleep(20)

@Bot.command()
async def info(ctx):
   await ctx.send(f'>Привет! { ctx.author.mention }\nЯ бот DA&A. Мой префикс "!".\nСписок моих команд: !kick "Имя Пользователя"\n!ban "Имя Пользователя" "Кол-во дней"\n!unban "Имя Пользователя"')

token = os.environ.get("BOT_TOKEN")