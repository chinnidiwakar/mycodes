#/bin/bash
echo "Enter First Three Octets ex: 192.168.0. finish with a dot"
read iprange
for host in $(seq 1 254);
do arping -c 1 $iprange$host |grep "bytes from" |cut -d " " -f5;
done;



#!/bin/bash
echo "Please enter ipaddress range: "
read firstpart
for lastpart in $(seq 1 254);
do ping -c 1 $firstpart$lastpart|grep "bytes from"|cut -d " " -f4|cut -d ":" -f1;
done;

#!/bin/bash
echo  "Welcome to network scanner"
echo "  "
echo "Please enter one IP adderss from the range:"
read input
first=$(echo $input|cut -d "." -f1,2,3)
echo "  "
echo "Scanning the network please wait!!!"
echo "  "
for last in $(seq 1 254);
do
ping -c 1 $first.$last|grep "bytes from"|cut -d " " -f4;
done;


#FASTER CODE
#!/bin/bash
echo  "Welcome to network scanner"
echo "  "
echo "Please enter one IP adderss from the range:"
read input
first=$(echo $input|cut -d "." -f1,2,3)
echo "  "
echo "Scanning the network please wait!!!"
echo "  "
for last in $(seq 1 254);
do
ping -c 1 $first.$last|grep 'bytes from'|cut -d ' ' -f4 &
done;
