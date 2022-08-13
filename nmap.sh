#!/bin/bash

read -p "Target: " TARGET

read -p "Filename: " FILENAME

nmap -sC -sV -vv -oA $FILENAME $TARGET
