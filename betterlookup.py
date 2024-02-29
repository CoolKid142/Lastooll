import json, requests


def lookup(ip ):
    with requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query,") as result:
        info = result.json()
        return print(json.dumps(info, indent=4))

while True:
    print("")
    print("Made By Decryption / Critical")
    print("")
    ip = input("Enter IP Here  ")
    lookup(ip)
    question = input("Look up again y/n: ")
    if question.lower() == "n":
        break
