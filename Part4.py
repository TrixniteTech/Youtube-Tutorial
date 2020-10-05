import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event                                                      
async def on_ready():
    print('Ready')



@client.command()
async def ping(ctx):#here we takes the input
    await ctx.send(f"Pong!{round(client.latency*1000)}")



@client.command()
@commands.has_permissions(administrator=True) #this line checks if the user who uses the kick command has permission to kick a member from the server
async def kick(ctx, member : discord.Member, *, reason=None):  #here as usual we use the ctx and member: discord.Member is used for mentioning some user and storing it
    await member.kick(reason=reason)  #now , this statement performs the actions ie. kicking the user from the server 
    await ctx.send(f"Kicked {member.mention} sucessfully for {reason}") #and at last here we display the person who was kicked and the reason he was kicked for

    





client.run(TOKEN)    
