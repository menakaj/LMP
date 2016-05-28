from __init__ import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Render_Index, '/')
api.add_resource(EnrollDevice, '/enroll-device/<device_type>')