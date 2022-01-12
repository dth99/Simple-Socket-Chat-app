
#client program

#client program create socket with server address and connect


from socket import *
def main():
    host=gethostname()
    portno=8088

    #mediator
    s=socket()
    

    #connection

    s.connect((host,portno))
    s.send(b"hello server")


    msg=s.recv(1024)
    print(msg)
    s.close()
main()