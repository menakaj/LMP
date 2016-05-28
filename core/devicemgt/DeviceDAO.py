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
from common.Constants import DatabaseCollections
from core.devicemgt.Device import Device


class DeviceDAO:

    def __init__(self):
        pass

    def createDevice(self, device):
        """
        Create a new device and store in database
        :param device: Device object
        """
        if DatabaseCollections.deviceCollectionName.find({"deviceId": device.id}).count() > 0:
            return "Already Enrolled"

        DatabaseCollections.deviceCollectionName.insert_one(
                {
                    "deviceId": device.id,
                    "deviceName": device.name,
                    "deviceType": device.type,
                    "deviceOwner": device.owner,
                    "deviceOrg": device.org
                }
        )

    def updateDevice(self, deviceId, device):
        """
        Update a given device
        :param deviceId: Id of the device that need to be updated.
        :param device: New device details
        :return: Success or not
        """
        try:
            DatabaseCollections.deviceCollectionName.update_one(
                    {
                        "deviceId": deviceId
                    },
                    {
                        "deviceId": device.id,
                        "deviceName": device.name,
                        "deviceOwner": device.owner,
                        "deviceType": device.type,
                    })
            return "Update Device Successful"
        except IOError:
            return "Update Device Failed"

    def deleteDevice(self, deviceId):
        """
        Delete the given device
        :param deviceId: Id of the device that need to be deleted.
        :return:
        """
        try:
            DatabaseCollections.deviceCollectionName.remove({"deviceId": deviceId})
            return "Device Deleted Successfully"
        except IOError:
            return "Device Deletion Failed"

    def getDevice(self, deviceId):
        """
        Get the device details
        :param deviceId: Id of the device
        :return:
        """
        device = DatabaseCollections.deviceCollectionName.find({"deviceId": deviceId})
        if device is None:
            return None
        else:
            return device

    def getDevices(self, owner):
        """
        Return the list of the all devices enrolled.
        :param owner: Tenant Id
        :return:
        """
        deviceList = []
        try:
            devices = DatabaseCollections.deviceCollectionName.find({"deviceOrg": owner})
            for device in devices:
                dev = Device(device["deviceId"], device["deviceName"], device["deviceType"], device["deviceOwner"],
                             device["deviceOrg"])
                deviceList.append(dev)
            return deviceList
        except IOError:
            return "Finding devices failed."

    def getAppleDevices(self, deviceOrg):
        """
        Get all the apple devices enrolled for a tenant.
        :param deviceOwner: tenantID
        :return:
        """
        deviceList = []
        try:
            devices = DatabaseCollections.deviceCollectionName.find({"deviceOrg": deviceOrg, "deviceType": "Apple"})
            for device in devices:
                dev = Device(device["deviceId"], device["deviceName"], device["deviceType"], device["deviceOwner"],
                             device["deviceOrg"])
                deviceList.append(dev)
            return deviceList
        except IOError:
            return "Finding devices failed."

    def getWindowsDevices(self, deviceOrg):
        """
        Get all the windows devices enrolled for a tenant.
        :param deviceOwner: tenantID
        :return:
        """
        deviceList = []
        try:
            devices = DatabaseCollections.deviceCollectionName.find({"deviceOrg": deviceOrg, "deviceType": "Windows"})
            for device in devices:
                dev = Device(device["deviceId"], device["deviceName"], device["deviceType"], device["deviceOwner"],
                             device["deviceOrg"])
                deviceList.append(dev)
            return deviceList
        except IOError:
            return "Finding devices failed."