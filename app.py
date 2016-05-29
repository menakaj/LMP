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

from __init__ import *
import socket
from config import *
app = Flask(__name__)
api = Api(app)

api.add_resource(Render_Index, '/')
api.add_resource(enroll_profile, '/Enroll')
api.add_resource(lmp_ca, '/ca')
api.add_resource(do_mdm_server, '/server')
api.add_resource(do_mdm_checkin, '/checkin')
api.add_resource(messageHandler, '/sendMessage')

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))
    ipAddress = s.getsockname()[0]
    context = (path_to_certificates + 'Server.crt', path_to_certificates + 'Server.key')
    app.run(host=ipAddress, port=8080, ssl_context=context)