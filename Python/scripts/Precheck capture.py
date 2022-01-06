#!/usr/bin/env python

import netmiko
import getpass
import datetime


purpose = input("Please enter purpose of output as below:-\n"
                "1. For Precheck capture enter pre\n"
                "2. For T-7 logs enter t7\n"
                "3. For T-48 logs enter t48\n"
                "4. For T-24 logs enter t24 \n\n"
                "So your response is :-  ")
username = str(input("Please enter your username: "))
login_pwd = getpass.getpass("Please enter your login password: ")

with open(r"C:\Users\Automation\Python\Input\Device_list.txt") as file:
    device_list = file.readlines()

# Clear "\n" because when device read new character automatically came with device name
devices = []
for i in device_list:
    devices.append(i.strip("\n"))

# Open file to capture if runtime error occurred
with open(r"C:\Users\Automation\Python\Output\runtime_error.txt", mode="w") as runtimefile:
    try:
        # Execute operation on one by one device
        for TMO_Device in devices:
            device_details = {"device_type": "cisco_nxos", "host": TMO_Device, "username": username,
                              "password": login_pwd, "fast_cli": False}
            SSH_Connection_Device = netmiko.ConnectHandler(**device_details)
            prompt = SSH_Connection_Device.find_prompt()

            # Create file as per purpose and write output of devices
            with open(r"C:\Users\Automation\Python\Output\\" + TMO_Device + "_" + purpose + ".txt", "w") as output_file:
                try:
                    if "ARE" in TMO_Device:
                        # Read commands which are needed as per logs
                        if purpose.lower() in ["pre", "precheck", "pre-check"]:
                            with open(r"C:\Users\Automation\Python\Input\ARE_Commands_precheck.txt") as are_file:
                                are_commands = are_file.readlines()
                        elif purpose.lower() in ["t-7", "t7"]:
                            with open(r"C:\Users\Automation\Python\Input\ARE_Commands_t7.txt") as are_file:
                                are_commands = are_file.readlines()
                        elif purpose.lower() in ["t48", "t-48"]:
                            with open(r"C:\Users\Automation\Python\Input\ARE_Commands_t48.txt") as are_file:
                                are_commands = are_file.readlines()
                        elif purpose.lower() in ["t24", "t-24"]:
                            with open(r"C:\Users\Automation\Python\Input\ARE_Commands_t24.txt") as are_file:
                                are_commands = are_file.readlines()
                        else:
                            output_file.write("Your purpose is not correct")

                        # To display progress on terminal
                        print("***************"*5)
                        print("Capturing log from device " + TMO_Device)
                        output_file.write("******** Connected to device " + str(TMO_Device) + " at " +
                                      str(datetime.datetime.now()) + "*******\n")

                        # Send each commands one by one
                        for command_sent in are_commands:
                            output_file.write(prompt + command_sent + "\n")
                            device_output = SSH_Connection_Device.send_command(command_sent, expect_string = prompt, delay_factor = 5)
                            output_file.write(device_output)
                        SSH_Connection_Device.disconnect()
                        output_file.write("\n****** Disconnected from device " + str(TMO_Device) + " at " +
                                              str(datetime.datetime.now()) + " ******")

                        # inform to terminal about log capturing completed for device
                        print("Capturing of log from device " + TMO_Device + " completed")
                        print("***************"*5)

                    elif ("DRE" in TMO_Device):

                        # Read comands which are needed as per purpose
                        if purpose.lower() in ["pre".lower(), "Precheck".lower(), "pre-check".lower()]:
                            with open(r"C:\Users\Automation\Python\Input\DRE_Commands_precheck.txt") as dre_file:
                                dre_commands = dre_file.readlines()
                        elif purpose.lower() in ["t-7", "t7"]:
                            with open(r"C:\Users\Automation\Python\Input\DRE_Commands_t7.txt") as dre_file:
                                dre_commands = dre_file.readlines()
                        elif purpose.lower() in ["t48", "t-48"]:
                            with open(r"C:\Users\Automation\Python\Input\DRE_Commands_t48.txt") as dre_file:
                                dre_commands = dre_file.readlines()
                        elif purpose.lower() in ["t24", "t-24"]:
                            with open(r"C:\Users\Automation\Python\Input\DRE_Commands_t24.txt") as dre_file:
                                dre_commands = dre_file.readlines()
                        else:
                            output_file.write("Your purpose is not correct")

                        # To display on terminal about progress
                        print("***************" * 5)
                        print("Capturing log from device " + TMO_Device)
                        output_file.write("******** Connected to device " + str(TMO_Device) + " at " +
                                          str(datetime.datetime.now()) + "*******\n")

                        # Send each command one by one
                        for command_sent in dre_commands:
                            output_file.write(prompt + command_sent + "\n")
                            device_output = SSH_Connection_Device.send_command(command_sent, expect_string=prompt,
                                                                               delay_factor=5)
                            output_file.write(device_output)
                        SSH_Connection_Device.disconnect()
                        output_file.write("****** Disconnected from device " + str(TMO_Device) + " at " +
                                              str(datetime.datetime.now()) + " ******")

                        # Inform on terminal that log capturing completed
                        print("Capturing of log from device " + TMO_Device + " completed")
                        print("***************" * 5)
                    else:
                        output_file.write("Device is not ARE nor DRE")

                # Capture error occurred while working on particular device
                except Exception as Error:
                    output_file.write("Error occurred as while executing and error is " + Error)

    # Capture error occurred while performing/executing program
    except Exception as runtime_error:
        runtimefile.write("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n Error occurred while executing")
        runtimefile.write(str(runtime_error))
        runtimefile.write("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
