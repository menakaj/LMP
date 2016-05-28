import os
from app import *
from M2Crypto import SMIME, X509, BIO

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path_to_certificates = BASE_DIR + '/LMP/certificates/'

# configure the app
app.config.from_object(__name__)
app.secret_key = os.urandom(24)
app.debug = True
app.root = os.path.abspath(os.path.dirname(__file__))
#app.ssl_context = context



# Set up some smime objects to verify signed messages coming from devices
sm_obj = SMIME.SMIME()
x509 = X509.load_cert(path_to_certificates + 'identity.crt')
sk = X509.X509_Stack()
sk.push(x509)
sm_obj.set_x509_stack(sk)

st = X509.X509_Store()
st.load_info(path_to_certificates + 'CA.crt')
sm_obj.set_x509_store(st)