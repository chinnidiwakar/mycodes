#ssh setup
sudo su
useradd -m administrator
passwd -d administrator
echo -e "secret\nsecret" |passwd administrator
echo "Welcome and thanks for using ssh which is way better than other unsecured protocol\n Thanks and Regards, admin" > /etc/issue.net
sed -i '/Banner/s/^#//g' /etc/ssh/sshd_config
sed -i '/PermitRootLogin/s/prohibit-password/yes/g' /etc/ssh/sshd_config
systemctl restart sshd
systemctl restart ssh


#database setup
apt-get install –y apt-transport-https gnupg ca-certificates
apt-get install couchdb
