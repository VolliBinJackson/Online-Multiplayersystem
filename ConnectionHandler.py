import socket

class ConnectionHandler:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.address = (self.server, self.port)
        self.id = self.connect()
        print(self.id)


    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass


    def send(self, information):
        try:
            self.client.send(str.encode(information))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


n = ConnectionHandler()
print(n.send("hello"))
print(n.send("working"))