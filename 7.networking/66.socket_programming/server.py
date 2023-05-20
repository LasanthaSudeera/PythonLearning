import socket

host = "localhost"
port = 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
print("Server listening on port: ", port)

c, address = s.accept()
print(c, address)

c.send(b"Hello how are you?")
c.close()