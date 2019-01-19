import socket

def send_msg(txt = ""):
    client = socket.socket()
    host = "DESKTOP-12OV957"
    port = 60000
    client.connect((host,port))
    msg = text.encode("utf-8")
    client.sendall(msg)
    client.close()
