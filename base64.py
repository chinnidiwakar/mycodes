#!/usr/bin/python
import base64

print "Welcome To Base64 Converter By Chinni"

def encode():
	data = raw_input("\nEnter the data you want to encode: ")
	encoded = base64.b64encode(data)
	print "\nYour Encoded Text Is: "+str(encoded)
	print "\nThanks For Using"
def decode():
	data = raw_input("\nEnter the data you want to encode: ")
	decoded = base64.b64decode(data)
	print "\nYour Decoded Text Is: "+str(decoded)
	print "\nThanks For Using"
prompt = raw_input("\nGive 'E' to encode or 'D' to decode or any other to quit: ")
if prompt == 'E':
	encode()
	quit()
if prompt == 'D':
	decode()
	quit()
else:
	print "\nQuitting"
	quit()
