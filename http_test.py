from socket import *

# 创建好监听套接字
s = socket()
s.bind(('0.0.0.0', 6789))
s.listen(5)

c, addr = s.accept()
data = c.recv(1024 * 10)
print(data.decode())
# c.send("牛逼".encode())

# html = """HTTP/1.1 200 OK
# Content-Type:text/html
#
# This is a test
# """

html = "HTTP/1.1 200 OK\r\n"
html += "Content-Type:text/html\r\n"
html += "\r\n"
with open("1.html") as f:
    html += f.read()

c.send(html.encode())

c.close()
s.close()
