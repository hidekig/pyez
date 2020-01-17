from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP
import datetime
import os

now = datetime.datetime.now()
new_dir = '/home/watashi/config/auto_get/'+now.strftime('%y%m%d_%H%M%S')
os.mkdir(new_dir)

USER = "uuuu"
PASSWD = "pppp"
DEVICE = [
     "NODE1",
     "NODE2",
     "NODE3",
     "NODE4" ,
]

for d in DEVICE:
    dev = Device(host=d, user=USER, password=PASSWD)
    with SCP(dev) as scp:
        scp.get("/config/juniper.conf", local_path=new_dir+'/'+d+"_juniper.conf")
