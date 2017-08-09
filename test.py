import parsespreadsheet
import Customer



device = Customer.CustomerDevice(row="2",name="TESTDEVICE",function="Switch",
                                 ip='100.123.48.166',design_id="RTR",
                                 user='a1cw2k',password='amWux=owhuk2',
                                 recv_buffer=100000)

device.connect()

device.get_cdp_neighbors()

#print(device.cdp_neighbors_list[0].interf)


for device in device.cdp_neighbors_list:
    print("----------------")
    print("Name:      {}".format(device.device_id))
    print("Interface: {}".format(device.interf))     
