# Copyright Pamekasancode
# Gunakan dengan bijak
import hashlib, os, sys
m = "\033[91m"
p = "\033[97m"
h = "\033[92m"
def clear():
	try:
		os.system("clear")
	except OSError:
		os.system("cls")
def banner():
	clear()
	print (f"""{m}
   ______
  (, /    )               /)          /)
    /---(  __     _/_  _ (/   _   _  (/
 ) / ____)/ (_(_(_(___(/_/ )_(_(_/_)_/ )_
(_/ (
{p}Author	: Firmansyahken
ketik help untuk menampilkan command
""")
banner()
def help():
	clear()
	print (f"""
{m}Command Brutehash{p}
-------------------------------------
clear	: membersihkan Command Line
exit	: keluar
banner	: menampilkan banner

{m}Cara Penggunaan{p}
-------------------------------------
ketik type hash codehash
example: md5 dcb76da384ae3028d6aa9b2

type hash yang tersedia di tool ini:
- md5
- sha1
- sha224
- sha256
- sha384
- sha512
""")
def brutehash():
	while True:
		namefile = "wordlist.txt"
		cmd = input(f"{m}brutehash {p}>  ")
		if "md5" in cmd:
			clear()
			md5 = cmd.split()[-1]
			file = open(namefile, "r")
			for wordlist in file:
				wordlist = wordlist.strip()
				hash = hashlib.md5(wordlist.encode("utf-8")).hexdigest()
				if md5 == hash:
					print (f"{p}[*]found ~> {h}"+wordlist)
					break
				else:
					print (f"{p}[x]crack ~> {m}"+wordlist)
		elif "sha1" in cmd:
			clear()
			sha1 = cmd.split()[-1]
			file = open(namefile, "r")
			for wordlist in file:
				wordlist = wordlist.strip()
				hash = hashlib.sha1(wordlist.encode("utf-8")).hexdigest()
				if sha1 == hash:
					print (f"{p}[*]found ~> {h}"+wordlist)
					break
				else:
					print (f"{p}[x]Crack ~> {m}"+wordlist)
		elif "sha224" in cmd:
			clear()
			sha224 = cmd.split()[-1]
			file = open(namefile, "r")
			for wordlist in file:
				wordlist = wordlist.strip()
				hash = hashlib.sha224(wordlist.encode("utf-8")).hexdigest()
				if sha224 == hash:
					print (f"{p}found ~> {h}"+wordlist)
					break
				else:
					print (f"{p}crack ~> {m}"+wordlist)
		elif "sha256" in cmd:
			clear()
			sha256 = cmd.split()[-1]
			file = open(namefile, "r")
			for wordlist in file:
				wordlist  = wordlist.strip()
				hash = hashlib.sha256(wordlist.encode("utf-8")).hexdigest()
				if sha256 == hash:
					print (f"{p}found ~> {h}"+wordlist)
					break
				else:
					print (f"{p}crack ~> {m}"+wordlist)
		elif "sha384" in cmd:
			clear()
			sha384 = cmd.split()[-1]
			file = open(namefile, "r")
			for wordlist in file:
				wordlist = wordlist.strip()
				hash = hashlib.sha384(wordlist.encode("utf-8")).hexdigest()
				if sha384 == hash:
					print (f"{p}found ~> {h}"+wordlist)
					break
				else:
					print (f"{p}crack ~> {m}"+wordlist)
		elif "sha512" in cmd:
			clear()
			sha512 = cmd.split()[-1]
			file = open(namefile, "r")
			for wordlist in file:
				wordlist = wordlist.strip()
				hash = hashlib.sha512(wordlist.encode("utf-8")).hexdigest()
				if sha512 == hash:
					print (f"{p}found ~> {h}"+wordlist)
					break
				else:
					print (f"{p}crack ~> {m}"+wordlist)
		elif cmd == "clear":
			clear()
		elif cmd == "help":
			help()
		elif cmd == "banner":
			banner()
		else:
			print (f"{cmd} tidak tersedia dalam command")
try:
	brutehash()
except KeyboardInterrupt:
	print ("Ctrl + C = keluar")
	sys.exit()
