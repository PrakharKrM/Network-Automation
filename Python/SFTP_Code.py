# Each time when we creat new case with uniper then JTAC want RSI and VARLOG from that router.
# That is why here we are going to create py code to upload files to JTAC server.
# It's assume that RSI and VARLOG alredy extracted from routers. If want code of that plase check previous codes of mine.

# For other SFTp server just required to some tweaking as per your requirement and it will work for you as well. 

import pysftp
import getpass

Username = input("Enter your username:- ")  # Username which is used by code to login into SFTP server
password = getpass.getpass()                # Password for that username. 


juniper_server = {
                        "host":"sftp.juniper.net",  # Define targeted SFTP server. Repalce "sftp.juniper.net" from your SFTP server/hostname.
                        "username":"anonymous",     # Define Username from which you are going to login into server. Replace anonymous from Username if do not want to hardcode
                        "password":"anonymous"      # Define password for username. Replace anonymous from password variable if do not hardcode
                }
                
pattern = "***********"*4

with open("JTACFILEOutput.txt", mode="w") as file:
        with pysftp.Connection(**juniper_server) as juniper_sftp:
                file.write(pattern)
                file.write("\n Connection established to Juniper Server  \n")
                try:
                        juniper_sftp.chdir("/pub/incoming")
                        try:
                                garb = juniper_sftp.mkdir("123-123-123")  # While creating new file it returned some value which is not of no use. Hence garb variable is used to store.
                                                                          # even after this garbage value test folder 123-123-123 created. Hence it is passed, this is for only Juniper server
                                                                          # may be different server will not give any agarbage value. 
                        except:
                                pass
                        juniper_sftp.chdir("123-123-123")
                        PWD =juniper_sftp.pwd
                        file.write(pattern+"\n"+PWD+"\n")
                        file.write(pattern+"\n We are going to upload RSI file \n")
                        juniper_sftp.put("RSI")
                        file.write("\n RSI file uploaded successfully. \n"+pattern+" \n VARLOG file going to upload \n ")
                        juniper_sftp.put("VARLOG.gz")
                        file.write("\n VARLOG file also uploaded successfully"+"\n"+pattern)
                        file.write("\nFiles uploaded on portal successfully \n"+pattern)
                        file.write(pattern)
                except:
                        file.write("\n Error occurred in main block"+"\n")


