import paramiko
import time
import re
from pprint import pprint
#import creds

##ip = '100.123.57.6'
##user = 'cisco'
##password = 'cisco'
recv_buffer = 100000





def writetoexcel(single_network_device_object):
    #pass this function a network device object
    #each network device will have things like ip, hostname, a list of cdp neighbors
    #this write columns for each interface (probably up to 28)
    #and populate the columns with a device id when it finds something on that interface
    ##how do I keep track of the row?
    pass


    
##for device in listofdevices():
##    writetoexcel(device)
    
##
##dev = NetworkDevice(ip,user,password)
##dev.connect()
##
##dev.get_version()
##dev.get_config()
##dev.get_cdp_neighbors()
##
###print(dev.cdp_neighbors['device_id'])
###print(len(dev.cdp_neighbors_list))
###print(dev.cdp_neighbors_list[1].ip)
##
##print('**************************************')
##print('Device IP: ', dev.ip)
##print('Device version: ', dev.version)
##print('CDP Neighbors: ')
##
##for neigh_device in dev.cdp_neighbors_list:
##    print('-------------------')
##    print(neigh_device.device_id)
##    print(neigh_device.platform)
##    print(neigh_device.ip)
##    print(neigh_device.interf)
##
##print('**************************************')
##


