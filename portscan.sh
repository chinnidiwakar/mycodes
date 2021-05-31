#!/bin/bash
echo  "Welcome to port scanner"
echo "  "
echo "Please enter IP adderss"
read input
echo "  "
echo "Scanning the ports Please wait!!!!!"
nc -nvz $input 1-65534 > /tmp/file.txt 2>&1
cat /tmp/file.txt |grep "UNKNOWN"|cut -d " " -f3,5|tac
