import os

import web

from __init__ import *


class enroll_profile(Resource):
    def get(self):
        # Enroll an iPad/iPhone/iPod when requested
        path = config.path_to_certificates + 'Enroll.mobileconfig'
        if os.path.exists(path):
            response = make_response(send_file(path))
            response.headers['Content-Type'] = 'application/x-apple-aspen-config;charset=utf-8'
            response.headers['Content-Disposition'] = 'attachment;filename="Enroll.mobileconfig'
            return response
        else:
            return "File not found"


class lmp_ca(Resource):
    def get(self):
        path = config.path_to_certificates + 'CA.crt'
        if os.path.exists(path):
            response = make_response(send_file(path))
            response.headers['Content-Type'] = 'application/octet-stream;charset=utf-8'
            response.headers['Content-Disposition'] = 'attachment;filename="CA.crt'
            return response
        else:
            return "File not found"


class do_mdm_server(Resource):
    def put(self):
        print request

class do_mdm_checkin(Resource):
    def put(self):
        print request