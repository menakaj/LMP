from __init__ import *


class Login_Page(Resource):
    def get(self):
        return make_response(
            render_template('login-page.html')
        )

class LoginConfirmation(Resource):
    def post(self):
        email = request.form['email']
        password = request.form['password']
        tenant =  TenantDAO()
        loginInfo = tenant.getTenant(email)
        if loginInfo:
            print loginInfo
            if password == loginInfo['password']:
                session['email'] = email
                return make_response(
                    redirect('/')
                )
            else:
                return make_response(
                    redirect('/login')
                )
        else:
            return make_response(
                redirect('/login')
            )



class Render_Index(Resource):
    def get(self):
        if 'email' in session:
            return make_response(
                render_template("home.html")
            )
        else:
            return make_response(
                redirect('/login')
            )

class EnrollDevice(Resource):
    def get(self, device_type):
        if 'email' in session:
            print 'Request to enroll a ' + device_type + ' device'
            return  make_response(
                render_template("enrollDevice.html")
            )
        else:
            return make_response(
                redirect('/login')
            )


class GetEnrolledDevices(Resource):
    def get(self, device_type):
        if 'email' in session:
            print 'Sent Device Data about ' + ' devies'
            return  make_response(
                render_template("enrolled-device-data.html")
            )
        else:
            return make_response(
                redirect('/login')
            )
