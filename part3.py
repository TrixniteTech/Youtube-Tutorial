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
async def avatar(ctx, *, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(title = f"{member.name}'s avatar", color = member.color , timestamp= ctx.message.created_at)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requested by : {ctx.author}",icon_url=ctx.author.avatar_url)  
    await ctx.send(embed=embed)
   
client.run('TOKEN') 
