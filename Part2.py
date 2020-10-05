import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')
 

@client.event
async def on_ready():
    print("Ready")
    
@client.event
async def on_message():
    user = message.author.name
    msg = message.content
    print(f"{user} has send {msg}")
    
    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong{round(client.latency*1000)}")
    
client.run('TOKEN')    
