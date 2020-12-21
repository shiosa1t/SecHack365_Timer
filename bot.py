import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from asyncio import sleep
import datetime

bot = Bot("!")

@loop(seconds=10)
async def name_change():
    dt = datetime.datetime(year=2021, month=1, day=26, hour=18)
    delta = dt - datetime.datetime.now()
    activity = discord.Activity(name=str(delta)[:-10], type=discord.ActivityType.streaming)
    await bot.change_presence(activity=activity)

name_change.before_loop(bot.wait_until_ready)    
name_change.start()
bot.run('NzkwNTY0MzA4NDg0NDg5MjE3.X-CcYw.-jRqniryKL0_2zK5qZsK72M94a4')