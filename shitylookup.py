from sys import argv, requests

ip = argv[1]

results = requests.get(f"http://ip-api.com/line/{ip}").text
print(results)
                                             
