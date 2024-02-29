from pystyle import Colorate, Colors, Center
import os
import requests
import time
import threading
import webbrowser

def send_msg(webhook_url):
    os.system('cls')
    ident()
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the Message to send ( Enter 0 to go back )'))
    headers = {'Content-Type': 'application/json'}
    def choice1():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '0':
            main_screen(webhook_url)
        try:
            response = requests.post(webhook_url, json={'content': choice})
        except:
            print(Colorate.Vertical(Colors.cyan_to_blue, 'Webhook not found...'))
        if response.status_code == 204:
            print(Colorate.Vertical(Colors.cyan_to_blue, f"Message sent..."))
        elif response.status_code == 429:
            print(Colorate.Vertical(Colors.cyan_to_blue, f"You Are Being Rate Limited ({response.json()['retry_after']}ms)"))
            time.sleep(response.json()["retry_after"] / 1000)
        else:
            print(Colorate.Vertical(Colors.cyan_to_blue, 'Message could not be sent...'))
        choice1()
    choice1()

def change_web(webhook_url):
    os.system('cls')
    ident()
    print(Colorate.Vertical(Colors.cyan_to_blue, '''
[ Webhook Change Menu ]
------------------------------------------------------------

-> 1 - Change Name
-> 2 - Go back

Note : For now you can only change the name of the webhook, more features will be added soon...

------------------------------------------------------------
    '''))
    def choice1():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '2':
            main_screen(webhook_url)
        if choice == '1':
            print(Colorate.Vertical(Colors.cyan_to_blue, 'Enter the new name of the webhook'))
            name = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))

            # create the JSON payload with new name and avatar URL
            payload = {
                'name': f'{name}',
            }

            # send the PATCH request with the payload
            response = requests.patch(webhook_url, json=payload)

            # check if the request was successful
            if response.status_code == 200:
                print(Colorate.Vertical(Colors.cyan_to_blue, 'Webhook updated succesfully...'))
            else:
                print(Colorate.Vertical(Colors.cyan_to_blue, 'Failed to update webhook name'))
            print(Colorate.Vertical(Colors.cyan_to_blue, f'Press enter to go back...'))
            input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
            change_web(webhook_url)
        else:
            change_web(webhook_url)
    choice1()

def ident():
    print(Colorate.Vertical(Colors.cyan_to_blue, '''                 /$$$$$$$              /$$           /$$   /$$                     /$$      
                | $$__  $$            | $$          | $$  | $$                    | $$      
                | $$  \ $$  /$$$$$$  /$$$$$$        | $$  | $$  /$$$$$$   /$$$$$$ | $$   /$$
                | $$$$$$$  /$$__  $$|_  $$_/        | $$$$$$$$ /$$__  $$ /$$__  $$| $$  /$$/
                | $$__  $$| $$  \ $$  | $$          | $$__  $$| $$  \ $$| $$  \ $$| $$$$$$/ 
                | $$  \ $$| $$  | $$  | $$ /$$      | $$  | $$| $$  | $$| $$  | $$| $$_  $$ 
                | $$$$$$$/|  $$$$$$/  |  $$$$/      | $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$
                |_______/  \______/    \___/        |__/  |__/ \______/  \______/ |__/  \__/    
                                              x,.-> made by r3xvert#0855
                                              x,.-> discord - https://discord.gg/WJGNdeQTCq
                                              
'''))

def spam_web(webhook_url):
    # Prompt user for message to spam
    message = input(Colorate.Vertical(Colors.cyan_to_blue, 'Enter the message to spam: '))

    # Prompt user for whether to use proxies
    use_proxies = input(Colorate.Vertical(Colors.cyan_to_blue, 'Use proxies? (y/n): ')).lower() == 'y'

    if use_proxies:
        # Load proxies from file
        with open('proxies.txt') as f:
            proxies = f.read().splitlines()
    else:
        proxies = [None]

    # Define function to send message with proxy
    def send_message(proxy):
        session = requests.Session()
        session.proxies = {'http': proxy, 'https': proxy}
        while True:
            message_data = {'content': message}
            try:
                response = session.post(webhook_url, json=message_data)
                print(Colorate.Vertical(Colors.cyan_to_blue, f'Sent message with proxy {proxy}.'))
            except:
                print(Colorate.Vertical(Colors.red_to_yellow, f'Could not send message with proxy {proxy}. Removing proxy from list.'))
                proxies.remove(proxy)
                break

    # Create threads for each proxy
    threads = []
    for proxy in proxies:
        thread = threading.Thread(target=send_message, args=(proxy,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


def main_screen(webhook_url):
    os.system('cls')
    ident()
    print(Colorate.Vertical(Colors.cyan_to_blue, '''
[ Webhook Menu ]
------------------------------------------------------------

-> 1 - Send message on webhook
-> 2 - Edit webhook ( Name and avatar )
-> 3 - Delete webhook
-> 4 - Spam webhook
-> 5 - Join Discord
-> 6 - Exit

------------------------------------------------------------
    '''))
    def choice1():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '1':
            send_msg(webhook_url)
        if choice == '2':
            change_web(webhook_url)
        if choice == '3':
            # send the DELETE request to delete the webhook
            response = requests.delete(webhook_url)

            # check if the request was successful
            if response.status_code == 204:
                print(Colorate.Vertical(Colors.cyan_to_blue, 'Webhook deleted successfully!'))
                input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
                ask4web()
            else:
                print(Colorate.Vertical(Colors.cyan_to_blue, 'Failed to delete webhook'))
        if choice == '4':
            spam_web(webhook_url)
        if choice == '5':
            url = "https://discord.gg/rWfZeqrtYR"
            webbrowser.open(url, new=0, autoraise=True)
        if choice == '6':
            exit()
        else:
            choice1()
    choice1()

def ask4web():
    os.system('cls')
    ident()
    def webhook():
        print(Colorate.Vertical(Colors.cyan_to_blue, 'Enter your webhook URL ( Note : Enter 0 to exit )'))
        webhook_url = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if webhook_url == '0':
            exit()
        if webhook_url.startswith('https://'):
            webhook_url = webhook_url
        else:
            webhook_url = f'https://{webhook_url}'
        try:
            response = requests.get(webhook_url)
            if response.status_code == 200:
                main_screen(webhook_url)
            else:
                print(Colorate.Vertical(Colors.cyan_to_blue, 'Your Webhook is Invalid, Please press enter and try again.'))
                input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
                webhook()
        except:
            print(Colorate.Vertical(Colors.cyan_to_blue, 'Your Webhook is Invalid, Please try again.'))
            webhook()
    webhook()

ask4web()