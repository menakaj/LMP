from __init__ import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Render_Index, '/')
api.add_resource(enroll_profile, '/Enroll')
api.add_resource(lmp_ca, '/ca')
api.add_resource(do_mdm_server, '/server')
api.add_resource(do_mdm_checkin, '/checkin')
api.add_resource(messageHandler, '/sendMessage')
