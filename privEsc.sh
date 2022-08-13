#!/bin/bash

IP=`hostname -I | awk '{print $2}'` 
read -p "PORT: " PORT 
echo $IP

cd ~/scripts/privesc
echo "Please connect to http://$IP:$PORT/ to download one of these files: "
ls

python2 -m  SimpleHTTPServer $PORT
