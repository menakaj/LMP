import socket

from config import *

if __name__ == '__main__':
    context = (path_to_certificates + 'Server.crt', path_to_certificates + 'Server.key')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))
    ipAddress = s.getsockname()[0]
    app.run(host=ipAddress, port=8080, ssl_context=context)
