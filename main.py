import sys
from colorama import Fore
import requests
import time
import os 

os.system('cls')
username = input(f"[?] username : ")

instagram = f'https://www.instagram.com/{username}'
facebook = f'https://www.facebook.com/{username}'
twitter = f'https://www.twitter.com/{username}'
youtube = f'https://www.youtube.com/{username}'
blogger = f'https://{username}.blogspot.com'
google_plus = f'https://plus.google.com/s/{username}/top'
reddit = f'https://www.reddit.com/user/{username}'
wordpress = f'https://{username}.wordpress.com'
pinterest = f'https://www.pinterest.com/{username}'
github = f'https://www.github.com/{username}'
tumblr = f'https://{username}.tumblr.com'
flickr = f'https://www.flickr.com/people/{username}'
steam = f'https://steamcommunity.com/id/{username}'
vimeo = f'https://vimeo.com/{username}'
soundcloud = f'https://soundcloud.com/{username}'
disqus = f'https://disqus.com/by/{username}'
medium = f'https://medium.com/@{username}'
deviantart = f'https://{username}.deviantart.com'
vk = f'https://vk.com/{username}'
aboutme = f'https://about.me/{username}'
imgur = f'https://imgur.com/user/{username}'
flipboard = f'https://flipboard.com/@{username}'
slideshare = f'https://slideshare.net/{username}'
fotolog = f'https://fotolog.com/{username}'
spotify = f'https://open.spotify.com/user/{username}'
mixcloud = f'https://www.mixcloud.com/{username}'
scribd = f'https://www.scribd.com/{username}'
badoo = f'https://www.badoo.com/en/{username}'
patreon = f'https://www.patreon.com/{username}'
bitbucket = f'https://bitbucket.org/{username}'
dailymotion = f'https://www.dailymotion.com/{username}'
etsy = f'https://www.etsy.com/shop/{username}'
cashme = f'https://cash.me/{username}'
behance = f'https://www.behance.net/{username}'
goodreads = f'https://www.goodreads.com/{username}'
instructables = f'https://www.instructables.com/member/{username}'
keybase = f'https://keybase.io/{username}'
kongregate = f'https://kongregate.com/accounts/{username}'
livejournal = f'https://{username}.livejournal.com'
angellist = f'https://angel.co/{username}'
last_fm = f'https://last.fm/user/{username}'
dribbble = f'https://dribbble.com/{username}'
codecademy = f'https://www.codecademy.com/{username}'
gravatar = f'https://en.gravatar.com/{username}'
pastebin = f'https://pastebin.com/u/{username}'
foursquare = f'https://foursquare.com/{username}'
roblox = f'https://www.roblox.com/user.aspx?username={username}'
gumroad = f'https://www.gumroad.com/{username}'
newsground = f'https://{username}.newgrounds.com'
wattpad = f'https://www.wattpad.com/user/{username}'
canva = f'https://www.canva.com/{username}'
creative_market = f'https://creativemarket.com/{username}'
trakt = f'https://www.trakt.tv/users/{username}'
five_hundred_px = f'https://500px.com/{username}'
buzzfeed = f'https://buzzfeed.com/{username}'
tripadvisor = f'https://tripadvisor.com/members/{username}'
hubpages = f'https://{username}.hubpages.com'
contently = f'https://{username}.contently.com'
houzz = f'https://houzz.com/user/{username}'
blipfm = f'https://blip.fm/{username}'
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'
hackernews = f'https://news.ycombinator.com/user?id={username}'
codementor = f'https://www.codementor.io/{username}'
reverb_nation = f'https://www.reverbnation.com/{username}'
designspiration = f'https://www.designspiration.net/{username}'
bandcamp = f'https://www.bandcamp.com/{username}'
colourlovers = f'https://www.colourlovers.com/love/{username}'
ifttt = f'https://www.ifttt.com/p/{username}'
ebay = f'https://www.ebay.com/usr/{username}'
slack = f'https://{username}.slack.com'
okcupid = f'https://www.okcupid.com/profile/{username}'
trip = f'https://www.trip.skyscanner.com/user/{username}'
ello = f'https://ello.co/{username}'
tracky = f'https://tracky.com/user/~{username}'
basecamp = f'https://{username}.basecamphq.com/login'

def load():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"\r{Fore.LIGHTCYAN_EX}[+]{Fore.RESET} Loading... [{i}]")
		sys.stdout.flush()
		time.sleep(0.1)

def banner():
    global Fore
    os.system('cls')

    print(f"")
    print(f"{Fore.LIGHTCYAN_EX}                                                ██████  ██ ▄█▀▄▄▄     ▄▄▄█████▓{Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}                                              ▒██    ▒  ██▄█▒▒████▄   ▓  ██▒ ▓▒{Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}                                              ░ ▓██▄   ▓███▄░▒██  ▀█▄ ▒ ▓██░ ▒░{Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}                                                ▒   ██▒▓██ █▄░██▄▄▄▄██░ ▓██▓ ░ {Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}                                              ▒██████▒▒▒██▒ █▄▓█   ▓██▒ ▒██▒ ░ {Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}                                              ▒ ▒▓▒ ▒ ░▒ ▒▒ ▓▒▒▒   ▓▒█░ ▒ ░░   {Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}                                              ░ ░▒  ░ ░░ ░▒ ▒░ ▒   ▒▒ ░   ░    {Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}                                              ░  ░  ░  ░ ░░ ░  ░   ▒    ░      {Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}                                                    ░  ░  ░        ░  ░        {Fore.RESET}")
    print(f"")                                
    print(f"") 
    print(f"                                                   {Fore.WHITE}whit{Fore.RESET} {Fore.LIGHTRED_EX}<3{Fore.RESET} {Fore.WHITE}by kl3ssydra{Fore.RESET}")
    print(f"")
    print(f"                                               {Fore.LIGHTCYAN_EX}https://github.com/kl3ssydra{Fore.RESET}                \n\n\n\n")


web = [
instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
]

def search():
    print(f'{Fore.LIGHTCYAN_EX}[+]{Fore.RESET} searching for username : {username}')
    os.system('cls')
    load()
    banner()

    print(f'{Fore.LIGHTCYAN_EX}[+]{Fore.RESET} SKAT v1.0 is working\n')
    
    load()

    time.sleep(1)

    count = 0
    match = True
    for url in web:
        r = requests.get(url)

        if r.status_code == 200:
            if match == True:
                print(f'\n \n{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} found matches')
                match = False
            print(f'\n{Fore.LIGHTBLUE_EX}[-]{Fore.RESET} link : {url} \n{Fore.LIGHTBLUE_EX}[-]{Fore.RESET} status : {r.status_code}')
            if username in r.text:
                print(f'{Fore.CYAN}[PM]{Fore.RESET} Username:{username} - {Fore.LIGHTGREEN_EX}text has been detected in url.{Fore.RESET}')
            else:
                print(f'{Fore.CYAN}[PM]{Fore.RESET} Username:{username} - {Fore.LIGHTRED_EX}text has not been detected in url, could be a false positive.{Fore.RESET}')#
        count += 1

    total = len(web)
    print(f'{Fore.LIGHTYELLOW_EX}a total of{Fore.RESET} {Fore.LIGHTBLUE_EX} {count} {Fore.RESET} {Fore.LIGHTYELLOW_EX}matches found out of{Fore.RESET} {Fore.LIGHTBLUE_EX} {total} {Fore.RESET} {Fore.LIGHTYELLOW_EX}websites.{Fore.RESET}')



if __name__=='__main__':
    banner()
    search()