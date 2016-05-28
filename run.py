from config import *

if __name__ == '__main__':
    context = (path_to_certificates + 'Server.crt', path_to_certificates + 'Server.key')
    app.run(host="172.22.111.214", port=8080, ssl_context=context)
