import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event                                                      
async def on_ready():
    print('Ready')


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong!{round(client.latency*1000)}")



@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned{member.mention} sucessfully for {reason}")
 


@ban.error
async def ban_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention} You does not have the permission to ban someone!')

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention} Please mention the user to be banned!")

    else:
        raise(error)

        

client.run('TOKEN')    
