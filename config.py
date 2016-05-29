# Copyright 2016 Team - LMP, University Of Peradeniya
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
from run_config import *
from M2Crypto import SMIME, X509, BIO

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path_to_certificates = BASE_DIR + '/LMP/certificates/'

# configure the app
app.config.from_object(__name__)
app.secret_key = os.urandom(24)
app.debug = True
app.root = os.path.abspath(os.path.dirname(__file__))
app.config['SESSION_TYPE'] = 'filesystem'
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