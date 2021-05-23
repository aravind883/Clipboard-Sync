import socket
import clipboard
import threading

stopflag = 0

def sendclipboard():
    clipboard.copy("sample")
    a=(clipboard.paste())
    while stopflag == 0:
        b=(clipboard.paste())
        
        
        if (a!=b): 
            clt.send(bytes(b ,"UTF-8"))
            a = b

        if stopflag == 1 :
            break

def receiveclipboard():
    msg = 0
    while stopflag == 0: 
        msg = clt.recv(port).decode("UTF-8") 
        clipboard.copy(msg)
        if stopflag == 1 :
            break

def syncclipboard():

    x = threading.Thread( target = sendclipboard )
    x.setDaemon(True)
    x.start()

    y = threading.Thread( target = receiveclipboard )
    y.setDaemon(True)
    y.start()

    if( input("Do you want to stop the program? <y/n> : ").lower() == "y" ):
        stopflag = 1
        x.join()
        y.join()

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("The IP address is ",socket.gethostbyname(socket.gethostname()))
    port=int(input("Enter port number : "))

    s.bind((socket.gethostname(),port))

    print("Waiting for connection...")
    s.listen(1)

    clt, adr = s.accept()
    print("Connection Established to Client")

    syncclipboard()

    s.close()
    print("Connection Closed...")




