import socket
import clipboard
import threading

def sendclipboard():
    clipboard.copy("sample")
    a=(clipboard.paste())
    while True:
        b=(clipboard.paste())
        if(len(b)==0):
            clipboard.copy(a)
            b=a
        
        if (a!=b): 
            s.send(bytes(b ,"UTF-8"))
            a=b

def receiveclipboard():
    msg=0
    while(True):
        msg = s.recv(port).decode("UTF-8")  
        clipboard.copy(msg)

def syncclipboard():

    x = threading.Thread(target=sendclipboard)
    x.start()

    y = threading.Thread(target=receiveclipboard)
    y.start()
    
    
    if( input("Do you want to stop the program ? <y/n> :").lower() == "y" ):
        x.join()
        y.join()

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip=input("Enter ip address : ")
    port=int(input("Enter port number : "))

    s.connect((ip, port))
        
    syncclipboard()

    s.close()
    print("Connection Closed...")