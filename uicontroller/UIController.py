from __init__ import *

class Render_Index(Resource):
    def get(self):
        return make_response(
            render_template("index.html")
        )