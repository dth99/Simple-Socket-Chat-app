from socket import *
def main():
    host = gethostname() #it given hostname / ip address
    
    port=8088
    s=socket()
    
    #bind the socket with port on host
    s.bind((host,port))
    
    print("server is running ...")
    
    #to connect with a system we need host and 
    # to connect server program on system we need port number
    
    
    #no of connection appect by server  #lister
    s.listen(5) 
    #it listen or appect on 5 connection
    #if 6th host want to connect server, it refueses
    c,add=s.accept() 
    print("connection established....")#print(host)
    #two variable c is client socket and add is address of client
    #accpet method accept the conncetion the client
    #it return a tuple (information of client)
    #it has client socket(port) and address
        #receive
    msg=c.recv(1024)  #c is client
    #1024 means 1kb data it can be receive
    print(str(msg))

    #C IS variable store client ip
    c.send(b'Hello client')
    
    


   
main() 