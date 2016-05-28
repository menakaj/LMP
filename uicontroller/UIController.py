from __init__ import *

class Render_Index(Resource):
    def get(self):
        return make_response(
            render_template("home.html")
        )

class EnrollDevice(Resource):
    def get(self, device_type):
        print 'Request to enroll a ' + device_type + ' device'
        return  make_response(
            render_template("enrollDevice.html")
        )