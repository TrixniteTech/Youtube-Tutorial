
#Snipe command

import discord
import asyncio
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Ready")
    


snipe_message_content = None
snipe_message_author = None

@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author


    snipe_message_content = message.content
    snipe_message_author = message.author.name 
    await asyncio.sleep(60)  
    snipe_message_author = None 
    snipe_message_content = None

@client.command()
async def snipe(message):
    if snipe_message_content==None:
        
        await message.channel.send("Nothing to snipe is found here!")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"Requested By {message.author.name}#{message.author.discriminator}")
        embed.set_author(name = f"Sniped the message deleted by : {snipe_message_author}")
        await message.channel.send(embed=embed)
        return



@client.command()
async def ping(ctx):
    await ctx.send(f"Pong{round(client.latency*1000)}")



client.run('TOKEN') 
