#Task : Firewall verification(Ping, Traceroute) to 10 servers
#Stack to use: Python, Jenkins

import subprocess

servers = ['google.com', 'facebook.com']

for i in range(2):
    #ping_result = subprocess.getoutput('ping ' + servers[i])
    ping_result = 'ping ' + servers[i]
    print(ping_result)
