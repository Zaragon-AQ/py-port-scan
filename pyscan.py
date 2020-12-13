import socket
import argparse

def scan(ip, port):
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     result = s.connect_ex((ip, port))

     if result == 0:
         print('Port '+ ip +':' +str(port)+ ' is open') 
     else: 
         print('Port '+ ip +':' +str(port)+ ' is closed') 


if __name__ == '__main__':

    ap = argparse.ArgumentParser()

    ap.add_argument("-i", "--ip", required=True, help= "host or ip")
    ap.add_argument("-p", "--port", required=True, help= "port")
    args = vars(ap.parse_args())
    ip = args["ip"]
    port = int(args["port"])
 
    scan(ip, port)
