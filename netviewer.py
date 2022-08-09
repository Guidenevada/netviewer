import time,socket
from termcolor import colored
def main():
    print("HELLO TO MY FIRST TEST\n\nHELLO, WORLD\n\n")
    listen(4444)


def listen(port):
    n = 0
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if n == 0:
            print(colored("[+] Listening on port %s" % port, "green"))
        s.bind(('', port))
        s.listen(10)
        conn, addr = s.accept()
        if n == 0:
                
            print(colored("[+] potential attack from "+addr[0]+","+addr[1]+"", "green"))
                
        n = n+1
        data = conn.recv(2048)
        while True:
            print(data.decode())
        
          
    except Exception as e:
        print(e)
        time.sleep(1)
        main()
