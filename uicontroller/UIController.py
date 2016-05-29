from __init__ import *


class Login_Page(Resource):
    def get(self):
        if 'email' in session:
            return make_response(
                redirect('/')
            )
        else:
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
                session['tenant'] = loginInfo['tenantName']
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
                render_template("home.html"
                                ,tenantName = session['tenant']
                                )

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
                render_template("enrollDevice.html",tenantName = session['tenant'])

            )
        else:
            return make_response(
                redirect('/login')
            )


class GetEnrolledDevices(Resource):
    def get(self, device_type):
        if 'email' in session:
            print 'Sent Device Data about ' + ' devies'
            if device_type == 'all':
                devices = DeviceDAO().getDevices(session['email'])
                session['last_device_look'] = 'all'
                return  make_response(
                    render_template("enrolled-device-data.html", devices=devices,tenantName = session['tenant'])

                )

            elif device_type == 'apple':
                devices = DeviceDAO().getAppleDevices(session['email'])
                session['last_device_look'] = 'apple'
                return  make_response(
                    render_template("enrolled-device-data.html", devices=devices,tenantName = session['tenant'])

                )

            elif device_type == 'windows':
                devices = DeviceDAO().getWindowsDevices(session['email'])
                session['last_device_look'] = 'windows'
                return  make_response(
                    render_template("enrolled-device-data.html", devices=devices,tenantName = session['tenant'])

                )
        else:
            return make_response(
                redirect('/login')
            )


class DeleteDevice(Resource):
    def get(self, device_id):
        if 'email' in session:
            print 'Request to enroll a ' + device_id
            DeviceDAO().deleteDevice(device_id)
            return  make_response(
                redirect('/enrolled-devices/'+session['last_device_look'])
            )
        else:
            return make_response(
                redirect('/login')
            )

class ViewDeviceData(Resource):
    def get(self, device_id):
        if 'email' in session:
            device_data = DeviceDAO().getDevice(device_id, session['email'])
            print device_data[0]
            return make_response(
                render_template(
                    'deviceProfile.html',
                    device_data=device_data[0]
                ,tenantName = session['tenant']
                )
            )
        else:
            return make_response(
                redirect('/login')
            )


class RendetClientEnroll(Resource):
    def get(self):
        return make_response(
            render_template('enroll-me-page.html')

        )

class RenderDownloadCertificated(Resource):
    def get(self):
        return make_response(
            render_template('enroll-downloads.html')

        )

