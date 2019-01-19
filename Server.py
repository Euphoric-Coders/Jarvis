import socket, select

def recieve_txt():
    serv = socket.socket()
    host = socket.gethostname()
    port = 60000
    serv.bind((host,port))
    print("Waiting for connection at {0} Port: {1}".format(host, port))
    serv.listen(5)
    conn, client = serv.accept()
    print("Connected to {0} at Port: {1}".format(client[0], client[1]))
    msg = conn.recv(1024).decode()
    print("Message Recieved:", msg)
    conn.close()
    serv.close()
    return msg
