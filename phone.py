#!/bin/python
#coding: utf-8
#salam: Admin & Member N.C.T
#author: Mage Tersakiti // PewXloit_41

"""		    HAI !^_^
Hehe ^_^! Maaf, Bukannya Saya Ingin Menipu tapi
saya hanya ingin memberikan pelajaran saja. dan
bukannya saya menggurui, tetapi saya ingin berbagi
sedikit informasi :(

Not Reporting and need to spread things that cause
people to H4te me and my team!
"""


import socket, time, sys, os

if sys.version[0] != '3':
	print("""______________________________________________
        REQUIRED PYTHON 3.x
        use: python phone.py
______________________________________________""")
	exit()

try:
	import requests
except ImportError:
	print("[x] requests not found: please wait for installing modul!")
	os.system("pip install requests")
except KeyboardInterrupt:
	print("\033[31;1m[!] Stop\033[0m")
os.system("clear || cls")

def log():
	try:
		print("""\033[32;1m
    [ INDONESIAN PHONE NUMBER ATTACK ]\033[0m
╔════════════════════════════════════════╗
║ \033[31;1mAuthor  : \033[0mMage Tersakiti               \033[0m║
║ \033[31;1mTeam    : \033[0mNewbie Cyber Team            \033[0m║
║ \033[31;1mGithub  : \033[0mgithub.com/PewXloit41        \033[0m║
╚════════════════════════════════════════╝
\033[0m""")

		print("\033[35;1m[+] \033[0m(example: +6282335441574)")
		target = str(int(input("\033[35;1m[+] \033[0mNumber : ")))
		if target == "" or target is None:
			print("\033[31;1m[!] Target is Empty, Failed to Continue the Attack \033[0m")
			exit()
		while len(target) != 14 and len(target)!= 15 and len(target) != 14 and len(target) != 12 and len(target) != 13:
			print("\033[31;1m[!] Target Fail\033[0m")
			target = int(input("\033[35;1m[+] \033[0mNumber : "))
		print("\033[32;1m[+] \033[0mTarget Number : \033[32;1m"+str(target))
	except EOFError:
		print("\n\033[31;1m[!] CTRL_D Detected\033[0m")
		exit()
	except KeyboardInterrupt:
		print("\033[31;1m[!] \Exit\033[0m")
		exit()
	except ValueError:
		print("\033[31;1m[!] Isi Dengan Benar\033[0m")
		time.sleep(2)
		os.system("clear || cls")
		log()


def attack():
	count = 0
	awal = time.time()
	while True:
		try:
			count += 1
			print("\033[31;1mPacket Virus Sent!  \033[32;1m {0}".format(count))
			time.sleep(2. / 100)
		except KeyboardInterrupt:
			print("\033[31;1m[!] \033[0mExit")
			print("\033[32;1m[✔] \033[0mEnd Attack at ", time.ctime(time.time()))
			akhir = time.time()
			print("\033[32;1m[+] \033[0mTotal Attack : ", akhir - awal," Detik")
			exit()



if __name__ == "__main__":
	log()

	try:
		time.sleep(3)
		url = "https://www.google.com"
		requests.get(url)
		print("\033[32;1m[✔] \033[0mStarting Attack at ", time.ctime(time.time()))
		attack()
	except requests.exceptions.ConnectionError:
		print("\n\033[31;1m[!] \033[0mNot Internet Connection.\n    Cek Your Connection And Try Again^_^")
		exit()
