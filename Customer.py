import paramiko
import time
import re

class Customer():
    def __init__(property_name,svc_type,clli,property_id):
        self.property_name = property_name
        self.svc_type = svc_type
        self.clli = clli
        self.property_id = property_id
        self.devices = []  #list of CustomerDevice objects


class NetworkDevice:
    def __init__(self,ip,user,password,recv_buffer=100000):
        self.ip = ip
        self.user = user
        self.password = password
        self.recv_buffer = recv_buffer

        self.sh_config = ''
        self.sh_ver = ''
        self.sh_cdp_neighbors = ''
        self.config = ''
        self.ver = ''
        self.cdp_neighbors_list = []
        self.shell = None
        
    def connect(self):
        '''
        Takes IP, user and password
        Returns shell object
        '''
        remote_connection = paramiko.SSHClient()
        remote_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_connection.connect(self.ip, username=self.user,password=self.password,look_for_keys=False)

        
        self.shell = remote_connection.invoke_shell()
        self.shell.send("term length 0\n")
        time.sleep(1)
        self.shell.recv(1000) #This clears out the "term length" output


    def get_config(self):
        self.shell.send("show run \n")
        time.sleep(2)
        #might need to sanitize longer than 512bytes lines
        self.sh_config = self.shell.recv(recv_buffer)

        output_list = dev.sh_config.decode("utf-8").splitlines(True)#keep \n character
        
        with open(self.ip+'_config.txt','w') as f:
            f.writelines(output_list)

    def get_version(self):
        self.shell.send("show ver \n")
        time.sleep(2)
        self.sh_version = self.shell.recv(recv_buffer)

        output_list = dev.sh_version.decode("utf-8").splitlines(True)#keep \n character
        
        with open(self.ip+'_version.txt','w') as f:
            f.writelines(output_list)

        pattern = re.compile(', Version (\d+\.\d+\(\w*\)\w\w\w+)')
        for line in output_list:
            mo = pattern.search(line)
            if mo != None:
                self.version = mo.group(1)

    def get_cdp_neighbors(self):
        self.shell.send("show cdp neigh detail  \n")
        time.sleep(2)
        self.sh_cdp_neighbors = self.shell.recv(self.recv_buffer)

        output_list = self.sh_cdp_neighbors.decode("utf-8").splitlines(True)#keep \n character
        
        with open(self.ip+'_cdp_neighbors.txt','w') as f:
            f.writelines(output_list)


        neigh_dev_id_pattern = re.compile('Device ID: (.*)')
        neigh_platform_pattern = re.compile('Platform: (.*),')  
        neigh_ip_pattern = re.compile('IP address: (.*)')
        neigh_interf_pattern = re.compile('Interface: (.*),')

        dev_list = self.sh_cdp_neighbors.decode("utf-8").split('-------------------------')

        #Create new CdpNeighbor object and populate it with data
        #Append each object to cdpneighbor list

        
        for device in dev_list[1:]:  #slice off show command 
            neighbor = CdpNeighbor()
        
            neigh_dev_id_mo = neigh_dev_id_pattern.search(device)
            neigh_platform_mo = neigh_platform_pattern.search(device)
            neigh_ip_mo = neigh_ip_pattern.search(device)
            neigh_interf_mo = neigh_interf_pattern.search(device)


            if neigh_dev_id_mo != None:
                 neighbor.device_id = neigh_dev_id_mo.group(1)

            if neigh_platform_mo != None:
                 neighbor.platform = neigh_platform_mo.group(1)

            if neigh_ip_mo != None:
                 neighbor.ip = neigh_ip_mo.group(1)

            if neigh_interf_mo != None:
                 neighbor.interf = neigh_interf_mo.group(1)

            self.cdp_neighbors_list.append(neighbor)


class CustomerDevice(NetworkDevice):
    def __init__(self,ip,user,password,recv_buffer,row,name,function,design_id):
        super().__init__(ip,user,password,recv_buffer)
        self.row = row
        self.name = name
        self.function = function
        self.ip = ip
        self.design_id = design_id
        self.user = user
        self.password = password
        self.cdp_neighbors_list = []

                
class CdpNeighbor:
    def __init__(self):

        self.device_id = ''
        self.platform = ''
        self.ip = ''
        self.interf = ''
    
