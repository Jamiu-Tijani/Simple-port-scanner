import sys
import socket
from datetime import datetime

#Define our target
print("_"*50)
print("WELCOME TO JAY PORT SCANNER 1.0")
print("_"*50)

print("")

IP = input("Please input IP")
if  len(IP) > 5:
        target = socket.gethostbyname(IP)
else:
        print("Please Check your ip if it's correct.")
        print("")
        sys.exit()
    #add a pretty banner
print("-"*50)
print("Scanning Target" + target)
print("time started" +str(datetime.now()))
print("-"*50)
try:
        for port in range(0,9000):
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port)) #returns error indicator
                if result == 0:
                        print('port {} is open'.format(port))
                
                s.close()
except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
except socket.error:
        print("Could not connect to server")        