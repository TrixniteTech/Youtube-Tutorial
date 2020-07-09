import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')
 

@client.event
async def on_ready():
    print("Ready")
    


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong{round(client.latency*1000)}")

#hello guys welcome back to my channel and welcome to another video of our discord bot dev series..
#today we are gonna deal with avatar command and embed
#so lets 

@client.command()
async def avatar(ctx, *, member: discord.Member = None):#here our usual syntax and we use member: discord.Member to mention some user
    member = ctx.author if not member else member#this line choose who's avatar is to be displayed.. like if you din't mention someone. it will give back your avatar
    embed = discord.Embed(title = f"{member.name}'s avatar", color = member.color , timestamp= ctx.message.created_at)
    #in the above line we define embed or the embed is introduced to our code , title gives the title to our bot, color gives the embed colour and timestamp displays when this was created
    embed.set_image(url=member.avatar_url)#in this line we set a image to our embed and we get this as same as in the avatar we recieved previously, but this is neat
    embed.set_footer(text=f"Requested by : {ctx.author}",icon_url=ctx.author.avatar_url) #this line sets our footer.. you can do the footer and all other things as your wish  
    await ctx.send(embed=embed)#and at last we print the embed, lets try running and see how it works
#lets try running the bot
# 
# yes so here it worked sucessfully so next we can deal with embed as this link shown here makes the avatar look bad so we can make a embed next    
client.run('NzI0MjE3NzgzMzMxNTg2MTAx.XwYPyA.gh9WLBn-ovOn47F-nmuOk9fgOXU') 