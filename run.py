import socket

from config import *

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))
    ipAddress = s.getsockname()[0]
    context = (path_to_certificates + 'Server.crt', path_to_certificates + 'Server.key')
    app.run(host=ipAddress, port=8080, ssl_context=context)
