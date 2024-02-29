import discord
import configparser
import asyncio
from concurrent.futures import ThreadPoolExecutor
from pystyle import Center, Colorate, Colors
import os
import time

config = configparser.ConfigParser()
config.read('config.txt')

prefix = variable_value = config.get('config', 'prefix')

client = discord.Client()

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

async def show_acc_info():
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
                                                    x,.-> logged in as {client.user}
                                                    x,.-> serving {len(client.guilds)} guild(s)
        """,
                1,
            )
        )
    )
    print((Colorate.Vertical(Colors.cyan_to_blue,   f"""x,.-> Clouds Nuker v6.9
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program""",1,)))
    print((Colorate.Vertical(Colors.cyan_to_blue,   f"""
[ Showing account info of {client.user} ]
------------------------------------------------------------

-> User - {client.user}
-> Servers - {len(client.guilds)}
-> Dm's - {len(client.private_channels)}
-> Avatar - {client.user.avatar_url}
-> Friends - {len(client.user.friends)}
-> Ping - {round(client.latency * 1000 , 2)}

------------------------------------------------------------
""",1,)))
    input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    await main_screen()

async def spam_dm():
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
                                                    x,.-> logged in as {client.user}
                                                    x,.-> serving {len(client.guilds)} guild(s)
        """,
                1,
            )
        )
    )
    print((Colorate.Vertical(Colors.cyan_to_blue,   f"""x,.-> Clouds Nuker v6.9
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program""",1,)))
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the message to send to everyone ( Enter 0 to go back )'))
    message = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    i = 0
    if message == '0':
        await main_screen()
    else:
        for dm in client.private_channels:
            try:
                await dm.send(message)
                i = i + 1
                print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Messaged {dm.recipient.name}'))
            except:
                print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Could not message {dm.recipient.name}'))
    print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Messaged {i} people'))
    input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    await main_screen()

async def rename_usr():
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the new name of the account ( Enter 0 to go back )'))
    old_name = str(client.user)
    new_name = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the password of the account ( Enter 0 to go back )'))
    password = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    if password == '0':
        await main_screen()
    if new_name == '0':
        await main_screen()
    try:
        await client.user.edit(username=new_name, password=password)
        print(Colorate.Vertical(Colors.cyan_to_blue, f'Renamed user from {old_name} to {client.user}'))
        input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        await main_screen()
    except:
        print(Colorate.Vertical(Colors.cyan_to_blue, f'Could not rename user, please try again. - {Exception}'))
        input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        await main_screen()

async def leave_all():
    i = 0
    print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Are you sure you want to leave {len(client.guilds)} guilds? [Y/n]'))
    choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    if choice != 'Y':
        time.sleep(2)
        await main_screen()
    else:
        for guild in client.guilds:
            try:
                await guild.leave()
                i = i + 1
                print(Colorate.Vertical(Colors.cyan_to_blue, f'Left guild {guild.name}'))
            except:
                print(Colorate.Vertical(Colors.cyan_to_blue, f'Could not leave guild {guild.name}'))
        print(Colorate.Vertical(Colors.cyan_to_blue, f'{i} Servers left on account {client.user}'))
        input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        await main_screen()

async def spam_create_servers():
    i = 0
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the name of servers to create'))
    name = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the amount of servers to create'))
    amount = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    for i in range(int(amount)):
        try:
            guild = await client.create_guild(name=name)
            i = i + 1
            print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Created server {guild.name}'))
        except:
            print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Could not create server {name}'))
    print(Colorate.Vertical(Colors.cyan_to_blue, f'Created {i} guilds with name {name}'))
    input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    await main_screen()

async def block_all():
    print(Colorate.Vertical(Colors.cyan_to_blue, f'Are you sure you want to block {len(client.user.friends)} friends? [Y/n]'))
    choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    if choice != 'Y':
        time.sleep(2)
        await main_screen()
    else:
        i = 1
        for friend in client.user.friends:
            try:
                await friend.block()
                print(Colorate.Vertical(Colors.cyan_to_blue, f'Blocked {friend.name}'))
                i = i + 1
            except:
                print(Colorate.Vertical(Colors.cyan_to_blue, f'Could not block {friend.name}'))
        print(Colorate.Vertical(Colors.cyan_to_blue, f'{i} Friends blocked for {client.user}'))
        input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        await main_screen()

async def spam_all():
    i = 0
    print(Colorate.Vertical(Colors.cyan_to_blue, f'Enter the message you want to send in all channels of all servers.'))
    message = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    for guild in client.guilds:
        for channel in guild.channels:
            try:
                await channel.send(message)
                print(f'Sent message in channel {channel.name} - {guild.name}')
                i += 1
            except:
                print(f'Could not send message in channel {channel.name} - {guild.name}')
    print(Colorate.Vertical(Colors.cyan_to_blue, f'Sent message in {i} channels.'))
    input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    await main_screen()

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
                                                    x,.-> logged in as {client.user}
                                                    x,.-> serving {len(client.guilds)} guild(s)
        """,
                1,
            )
        )
    )
    print((Colorate.Vertical(Colors.cyan_to_blue,   f"""x,.-> Clouds Nuker v6.9
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program""",1,)))
    print((Colorate.Vertical(Colors.cyan_to_blue,   f"""
[ Account nuker / Select a 0ption ]
------------------------------------------------------------

-> 0 - Go back to main menu
-> 1 - See account info
-> 2 - Mass DM
-> 3 - Rename User
-> 4 - Leave all servers
-> 5 - Create Servers
-> 6 - Block all friends
-> 7 - Send a message in all servers

------------------------------------------------------------
""",1,)))
    async def choice1():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '0':
            os.system('python launcher.py')
        if choice == '1':
            await show_acc_info()
        if choice == '2':
            await spam_dm()
        if choice == '3':
            await rename_usr()
        if choice == '4':
            await leave_all()
        if choice == '5':
            await spam_create_servers()
        if choice == '6':
            await block_all()
        if choice == '7':
            await spam_all()
        else:
            await choice1()
    await choice1()


@client.event
async def on_ready():
    await main_screen()

def start_account_nuker():
    print(Colorate.Vertical(Colors.cyan_to_blue, 'x,.-> Enter your Account Token :'))
    token = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    loading_screen()
    try:
        client.run(token, bot=False)
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
                            x,.- made by r3xvert#0855
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
    x,.- contact r3xvert#0855 or join https://discord.gg/WJGNdeQTCq for help
    """,
                1,
            )
        )
    )
        input(Colorate.Vertical(Colors.red_to_yellow, 'x,.->'))
        time.sleep(2)