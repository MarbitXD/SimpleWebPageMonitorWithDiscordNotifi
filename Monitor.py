import discord
import asyncio
from discord.ext import commands, tasks
from asyncio import coroutine
import urllib
import urllib.request
import time
import os
from selenium import webdriver
from dhooks import Webhook, Embed

url = str("YOUR WEBSITE")
hook = Webhook('YOUR DISCORD WEBHOOK')
driver = webdriver.Chrome('chromedriver.exe')
bot = commands.Bot(command_prefix="!")
client = discord.Client()


@client.event
async def on_ready():
    print('Bot is ready!')
    update_check.start()

async def on_webUpdate():
    embed = Embed(color=14177041,)
    embed.set_author("Change")
    hook.send(embed=embed)
    quit()

@tasks.loop()
async def update_check():
    try:
        a = urllib.request.urlopen(url)
        await asyncio.sleep(15)
        webpage = a.read().decode('utf-8')
        await asyncio.sleep(30)
        ab = urllib.request.urlopen(url)
        await asyncio.sleep(15)
        webpage2 = ab.read().decode('utf-8')
        if (webpage2 != webpage) :
            print('update')           
            asyncio.create_task(on_webUpdate())
        else:
            print('not_changed')
    except:
        print('error')


client.run('YOUR DISCORD TOKEN')
