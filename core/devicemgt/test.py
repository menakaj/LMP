from core.devicemgt.Device import Device
from core.devicemgt.DeviceDAO import DeviceDAO

# ids = [("d1", "MacAir","Saman", "Apple"), ("d2", "Windows_Abc", "Kamal", "Windows"), ("d3", "MacBookPro1", "Maithree", "Apple"),
#        ("d4","MacBookPro2","Siripala","Apple"), ("d5", "Win123", "Suji","Windows"),
#        ("d6", "Mac01", "Sunimal", "Apple"), ("d7", "Wind1", "Somapala", "Windows"), ("d8", "iMac",  "Mahinda", "Apple"),
#        ("d9", "Win345", "Nayana", "Windows"), ("d10", "Windows234", "Sirisena", "Windows")]
#
# for (id, name, owner, type) in ids:
#     t = Device(id, name, type, owner, "ABC_COrporation")
#     dao = DeviceDAO()
#     dao.createDevice(t)
#     print id, name, owner, type

dao = DeviceDAO()
devices = dao.getWindowsDevices("ABC_COrporation")

for d in devices:
    print(d.id, d.name)

   #
   # deviceId = "",
   #               deviceName = "",
   #               deviceType = "",
   #               deviceOwner = "",
   #               deviceOrg = ""):