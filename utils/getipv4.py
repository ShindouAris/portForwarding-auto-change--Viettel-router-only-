import socket

def getipv4():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))

    ip_address = s.getsockname()[0]

    s.close()

    return ip_address

