# THis script will login into router (in this hard coded to IOS ) and configur it as per config file
import netmiko
import getpass


""" Fetch router list from file"""
with open(r"switch.txt", mode="r") as switch:
    switch_list = switch.readlines()

print(switch_list)
print(type(switch_list))

switch_list_no_new_line = []
for index in range(len(router_list)):
    switch_list_no_new_line.append(switch_list[index].rstrip("\n"))

print(switch_list_no_new_line)
Username = str(raw_input("Please enter your username:"))
Password = getpass.getpass()

if Password:
        for i in range(len(switch_list_no_new_line)):
            with open("SW-"+i+1+".conf") as config_file:
                cofiguration = config_file.readlines()
                with open("terminal_response_"+switch_list[i]+".txt", mode="w") as router_output:
                        print("working on "+ switch_list[i])
                        router_attrib = { "host": switch_list_no_new_line[i],
                                  "username":Username,
                                  "password":Password,
                                  "device_type":"cisco_ios"}
                        router_SSH = netmiko.ConnectHandler(**router_attrib)
                        router_terminal_output = router_SSH.send_config_set(cofiguration)
                        router_output.write(router_terminal_output)
else:
    print("Your entered password is null. From null password i can't proceed")
