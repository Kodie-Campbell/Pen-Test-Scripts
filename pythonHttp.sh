#!/bin/bash

echo What Port:

read PORT

python2 -m SimpleHTTPServer $PORT
