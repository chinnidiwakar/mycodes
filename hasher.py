#!/usr/bin/python3

import hashlib
import subprocess
from subprocess import check_output
def Data():
	data = input("\nPlease input the data you want to Hash: ")
	print("\nMD5 Hash for the given data is:    ", hashlib.md5(data.encode('utf-8')).hexdigest())
	print("SHA1 Hash for the given data is:   ", hashlib.sha1(data.encode('utf-8')).hexdigest())
	print("SHA224 Hash for the given data is: ", hashlib.sha224(data.encode('utf-8')).hexdigest())
	print("SHA256 Hash for the given data is: ", hashlib.sha256(data.encode('utf-8')).hexdigest())
	print("SHA384 Hash for the given data is: ", hashlib.sha384(data.encode('utf-8')).hexdigest())
	print("SHA512 Hash for the given data is: ", hashlib.sha512(data.encode('utf-8')).hexdigest())

def File():
	file = input("\nPlease input the file name with complete path (ex:/root/Desktop/example.txt): ")
	md5 = check_output(["md5sum", file])
	sha = check_output(["shasum", file])
	sha224 = check_output(["sha224sum", file])
	sha256 = check_output(["sha256sum", file])
	sha384 = check_output(["sha384sum", file])
	sha512 = check_output(["sha512sum", file])
	print("\nMD5 Hash for the given file is:    ", md5.decode("utf-8")[:33])
	print("SHA Hash for the given file is:    ", sha.decode("utf-8")[:41])
	print("SHA224 Hash for the given file is: ", sha224.decode("utf-8")[:58])
	print("SHA256 Hash for the given file is: ", sha256.decode("utf-8")[:65])
	print("SHA384 Hash for the given file is: ", sha384.decode("utf-8")[:97])
	print("SHA512 Hash for the given file is: ", sha512.decode("utf-8")[:130])

print("\nWelcome To Chinni Diwakar's 6 In 1 Hasher\n")

prompt = input("What would you like to Hash(FILE or DATA)? Give 'F' for File or 'D' for Data or any other to Quit: ")

if prompt == "F":
	File()
elif prompt == "D":
	Data()
else:
	print("\nThanks for Dropping By!")
	quit()
