#!/usr/bin/env python

import paramiko

host = "192.168.11.1"
port = 22
username = "prakhar"
password = "password"

command = ["terminal length 0", "show ip interface brief", "show interface description"] # Here we can use any text file to read set of commands to get output.
command_strip = command.stripline("\n")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
for i in len(command):
	with open(r"output of"+str(command_strip[i]), mode="w") as outputfile:
		terminal_output = ssh.exec_command(command[i])
		lines = terminal_output.readlines()
		outputfile.write("\n Following is the output of device"+host+"\n")
		outputfile.write(lines)

ssh.disconnect()
