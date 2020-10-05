import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Ready")
    


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong{round(client.latency*1000)}")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send("You don't have permission to access this command!")    
        


client.run('TOKEN') 
