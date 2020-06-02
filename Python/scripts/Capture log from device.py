# In this script we are going to open list of command and run on router
#!/bin/usr/env python3

import netmiko
import getpass

#define global variable so that they can be used anywhere.
router_list = []
command_list = []
device_type = []
cisco_ios_router=[]
cisco_xr_router = []
cisco_xe_router = []
juniper_junos_router=[]
alcatel_sros_router = []
cisco_ios_command = []
cisco_xr_command = []
cisco_xe_command = []
juniper_junos_command = []
alcatel_sros_command =[]
required_command =[]
device_in_role =[]

""" Fetch router list from file on which operation required"""

with open(r"/root/python/input/routers.txt", mode="r") as router:
    router_list_raw = router.readlines()

print("Following is the list of routers :- \n"+router_list_raw)

#Iterate to remove new lines from list

for index in range(len(router_list)):
    router_list.append(router_list[index].rstrip("\n"))

# #Accept username and password from user which is used in logging router
Username = raw_input("Please enter your username:") #python2.X does not support only input hence raw_input sed to avoid evaluation
Password = getpass.getpass()  #it will not echo

if Password:
    with open(r"/root/python/output/raised_error_while_executing.txt", mode="w") as error_file:
        try:
            with open(r"/root/python/inventory/cisco_ios_inv.txt") as cisco_ios_inv_file:
                cisco_ios_inv = cisco_ios_inv_file.readlines()
                for i in range(len(cisco_ios_inv)):
                    cisco_ios_router.append(cisco_ios_inv[i].rstrip("\n"))
            with open(r"/root/python/inventory/cisco_xr_inv.txt") as cisco_xr_inv_file:
                cisco_xr_inv = cisco_xr_inv_file.readlines()
                for i in range(len(cisco_xr_inv)):
                    cisco_xr_router.append(cisco_ios_inv[i].rstrip("\n"))
            with open(r"/root/python/inventory/cisco_ios_inv.txt") as cisco_xe_inv_file:
                cisco_xe_inv = cisco_xe_inv_file.readlines()
                for i in range(len(cisco_xe_inv)):
                    cisco_xe_router.append(cisco_xe_inv[i].rstrip("\n"))
            with open(r"/root/python/inventory/juniper_junos_inv.txt") as juniper_junos_inv_file:
                juniper_junos_inv = juniper_junos_inv_file.readlines()
                for i in range(len(juniper_junos_inv)):
                    juniper_junos_router.append(juniper_junos_inv[i].rstrip("\n"))
            with open(r"/root/python/inventory/alcatel_sros_inv.txt") as alcatel_sros_inv_file:
                alcatel_sros_inv = alcatel_sros_inv_file.readlines()
                for i in range(len(alcatel_sros_inv)):
                    alcatel_sros_router.append(alcatel_sros_inv[i].rstrip("\n"))

            #Fetch commands with respect to specific device model/vendor
            with open(r"/root/python/input/cisco_ios_command.txt") as cisco_ios_command_file:
                cisco_ios_command_raw = ios_command_file.readlines()
                for j in range(len(cisco_ios_command_raw)):
                    cisco_ios_command.append(cisco_ios_command_raw[j].rstrip("\n"))
            with open(r"/root/python/input/cisco_xr_command.txt") as cisco_xr_command_file:
                cisco_xr_command_raw = cisco_xr_command_file.readlines()
                for i in range(len(cisco_xr_command_raw)):
                    cisco_xr_command.append(cisco_xr_command_raw.rstrip("\n"))
            with open("/root/python/input/cisco_xe_command.txt") as cisco_xe_command_file:
                cisco_xe_command_raw = cisco_xe_command_file.readlines()
                for i in range(len(cisco_xe_command_raw)):
                    cisco_xe_command.append(cisco_xe_command_raw[i].rstrip("\n"))
            with open(r"/root/python/input/juniper_junos_command.txt") as juniper_junos_command_file:
                juniper_junos_command_raw = juniper_junos_command_file.readlines("\n")
                for i in range(len(juniper_junos_command_raw)):
                    juniper_junos_command.append(juniper_junos_command_raw.rstrip("\n"))
            with open(r"/root/python/input/alcatel_sros_command.txt") as alcatel_sros_command_file:
                alcatel_sros_command_raw = alcatel_sros_command_file.readlines()
                for i in range(len(alcatel_sros_command_raw)):
                    alcatel_sros_command.append(alcatel_sros_command_raw[i].rstrip("\n"))

            # Login into each device one by one from list and fetch required logs
            for i in range(len(router_list)):
                print("\n Currently working on ", router_list[i])
                device_in_role = router_list[i]
                if router_list[i] in cisco_ios_router:
                    device_type="cisco_ios"
                    required_command = cisco_ios_command
                else:
                    if router_list[i] in cisco_xr_router:
                        device_type = "cisco_xr"
                        required_command = cisco_xr_command
                    else:
                        if router_list[i] in cisco_xe_router:
                            device_type = "cisco_xe"
                            required_command = cisco_xe_command
                        else:
                            if router_list[i] in juniper_junos_router:
                                device_type = "juniper_junos"
                                required_command = juniper_junos_command
                            else:
                                if router_list[i] in alcatel_sros_router:
                                    device_type = "alcatel_sros"
                                    required_command = alcatel_sros_command

                with open(r"/root/python/output/"+str(router_list[i])+".txt", mode="w") as router_terminal_output:
                    pattern = "****************************"*4
                    print(device_type)
                    router_attrib = { "host": router_list[i],
                                      "username":Username,
                                      "password":Password,
                                      "device_type":device_type}
                    router_terminal_output.write(pattern+"\n")
                    router_terminal_output.write("\t\t Following is the output from router "+str(router_list[i])+"\n")
                    router_terminal_output.write("\n"+pattern+"\n")
                    router_SSH = netmiko.ConnectHandler(**router_attrib)
                    prompt = router_SSH.find_prompt()
                    for k in range(len(required_command)):
                        router_SSH.find_prompt()
                        router_terminal_output.write(prompt + required_command[k] + "\n")
                        router_command_output = router_SSH.send_command(required_command[k])
                        router_terminal_output.write(router_command_output+"\n")
                    router_SSH.disconnect()
                    router_terminal_output.write(pattern+"\n\t If you found error please send this output and error "
                                                         "file raised_error_while_execting.txt to \n "
                                                         "prakhar*******@gmail.com\n"+pattern)
        except Exception as Error:
            error_file.write("Exception error while executing program for device : "+device_in_role+
                            "and exception is :- "+Error)
else:
    print("Your entered password is null. From null password we can't proceed")
