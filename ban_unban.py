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

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#') 

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned{user.mention}"
            return    




client.run('TOKEN')    
