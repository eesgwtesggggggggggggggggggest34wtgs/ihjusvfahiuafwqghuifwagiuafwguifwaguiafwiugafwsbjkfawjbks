from discord.ext import commands
import discord
import random
import datetime
import os
import requests

#made by ur boi geek couple things in here taken from public source gens and private ones that still aint leaked idk remeber what though

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all()) #define bot to use everwhere in dah code

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error ,commands.CommandOnCooldown):
      await ctx.reply("You have {:.2f}s".format(error.retry_after) + " on your cooldown")

def randomacc(filename): #simple function to randomly select sumthing in text file
    lin=open(filename).read().splitlines()
    return random.choice(lin)

@bot.command()
@commands.cooldown(1,10, commands.BucketType.member)
async def gen(ctx, type_account):
  if ctx.channel.id == int(1041515413969833994):
    if type_account == "2010":
        acc = ''
        acc += randomacc("accs.txt")
        acc += '\n'
        combined = acc.split(':')
        username = combined[0]
        password = combined[1]
        fixed_pass = password.rstrip()
        acc_embed = discord.Embed(color=0x77ff96) #define embed
        acc_embed.add_field(name=DMS, value=f"account has been sent to your DMs")
        acc_embed.set_footer(text="")
        
        #stuff to make look good
        acc_name = requests.get(f"https://api.roblox.com/users/get-by-username?username={str(username)}")
        account_avatar = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={acc_name.json()['Id']}&size=720x720&format=Png&isCircular=false")
        acc_avatar_data = account_avatar.json()['data']
        
        #account creation data
        acc_ceated = requests.get(f"https://users.roblox.com/v1/users/{acc_name.json()['Id']}")
        acc_created_time = acc_ceated.json()['created']
        acc_created_time = datetime.datetime.strptime(acc_created_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        
        #embed sent to dms
        dm_embed = discord.Embed(title="", description=f"", color=0xff2525)
        dm_embed.add_field(name='Username', value=f"```{str(username)}```")
        dm_embed.add_field(name='Combo', value=f"```{str(username)}:{str(fixed_pass)}```\n", inline=False)
        dm_embed.add_field(name='\nUser ID\n', value=f"{acc_name.json()['Id']}")
        dm_embed.set_thumbnail(url=acc_avatar_data[0]['imageUrl'])
        dm_embed.timestamp = datetime.datetime.now()
        dm_embed.set_footer(text="")

        #send everything
        await ctx.author.send(acc)
        try:
          await ctx.author.send(embed=dm_embed)
          await ctx.reply(embed=acc_embed)
        except:
          return 0

    elif type_account == 'random':
        acc = ''
        acc += randomacc("accs.txt")
        acc += '\n'
        combined = acc.split(':')
        username = combined[0]
        password = combined[1]
        fixed_pass = password.rstrip()
        acc_embed = discord.Embed(color=0x77ff96) #define embed
        acc_embed.add_field(name='<:yes_checkmark:1025641961966809148> **Account Generation Successful!**', value=f"``random``account combo has been sent to your DMs! __account is for roblox btw__")
        acc_embed.set_footer(text="geek made this")
        
        #stuff to make look good
        acc_name = requests.get(f"https://api.roblox.com/users/get-by-username?username={str(username)}")
        account_avatar = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={acc_name.json()['Id']}&size=720x720&format=Png&isCircular=false")
        acc_avatar_data = account_avatar.json()['data']
        
        #account creation data
        acc_ceated = requests.get(f"https://users.roblox.com/v1/users/{acc_name.json()['Id']}")
        acc_created_time = acc_ceated.json()['created']
        acc_created_time = datetime.datetime.strptime(acc_created_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        
        #embed sent to dms
        dm_embed = discord.Embed(title="🤖 ***Generated Account | geek made this***", description=f"Selling/trading these accounts is strictly prohibited! See our rules and terms for more information.", color=0xff2525)
        dm_embed.add_field(name='Username', value=f"```{str(username)}```")
        dm_embed.add_field(name='Password', value=f"```{str(password)}```\n")
        dm_embed.add_field(name='Combo', value=f"```{str(username)}:{str(fixed_pass)}```\n", inline=False)
        dm_embed.add_field(name='\nUser ID\n', value=f"{acc_name.json()['Id']}")
        dm_embed.add_field(name='\nLast Online\n', value=f"{acc_created_time.strftime('%B %d, %Y')}")
        dm_embed.add_field(name='\nJoin Date\n', value=f"{acc_created_time.strftime('%d/%m/%Y')}")
        dm_embed.set_thumbnail(url=acc_avatar_data[0]['imageUrl'])
        dm_embed.timestamp = datetime.datetime.now()
        dm_embed.set_footer(text="⚠️ If you intend to keep the account it's recommended that you change the account password! account is for roblox btw")

        #send everything
        await ctx.author.send(acc)
        try:
          await ctx.author.send(embed=dm_embed)
          await ctx.reply(embed=acc_embed)
        except:
          return 0

    elif type_account == 'bulk':
        accounts = ''
        em = discord.Embed(color=0x77ff96)
        em.add_field(name="<:yes_checkmark:1025641961966809148> ***Generating Accounts***", value='accounts are being generated!')
        message = await ctx.reply(embed=em)
        for x in range(50):
            accounts += randomacc("accs.txt")
            accounts += "\n"
        
        with open("accounts1.txt", "w") as file:
            file.write(accounts)
        with open("accounts1.txt", "rb") as file:
            em = discord.Embed(color=0xff2525)
            em.add_field(name="🤖 Generated Accounts | geek made this", value="Generating Accounts!")
            em.timestamp = datetime.datetime.now()
            em.set_footer(text="⚠️ If you intend to keep the account it's recommended that you change the account password!")
            await ctx.author.send(embed=em)
            await ctx.author.send(file=discord.File(file, "accounts1.txt"))
        await message.delete()
        em = discord.Embed(color=0x77ff96)
        em.add_field(name='<:yes_checkmark:1025641961966809148> **Account Generation Successful!**', value=f"Accounts have been sent to your DMs account is for roblox btw")
        await ctx.reply(embed=em)
  else:
    await ctx.reply("Wrong channel")
bot.remove_command("help")
@bot.command()
async def help(ctx):
  em = discord.Embed(color=0xff0000)
  em.add_field(name='**.gen**', value='you can do .gen bulk, .gen rare or .gen random\n all accounts are 2017/2018 and ready to have email added')
  await ctx.reply(embed=em)

@bot.command()
async def stock(ctx):
  with open("accs.txt", 'r') as fp:
    account_amount = len(fp.readlines())
    em = discord.Embed(color=0xff0000)
    em.add_field(name='Stock Amount', value=f"{account_amount} accounts are stocked")
    await ctx.send(embed=em)

my_secret = os.environ['token']
try:
  bot.run(my_secret)
except:
  os.system("kill 1")
