from flask import *
from flask_restful import *
from core.tenantmgt.TenantDAO import *
from werkzeug.datastructures import ImmutableMultiDict
from core.devicemgt.DeviceDAO import DeviceDAO