import openpyxl.workbook
import requests
import json
from requests.auth import HTTPBasicAuth
import getpass
import openpyxl



def get_first_host_record(endpoint, user, user_pwd):
    # Called first API to get information and next page id if data is more
    first_call = requests.get(url=endpoint, auth=HTTPBasicAuth(user, user_pwd), verify=False)
    first_payload = first_call.json() # Get response in JSON format
    complete_data = first_payload['result']  # Get only required data and results is in list
    if 'next_page_id' in first_payload:    # If more than one page is present with pagination then next_page_id will be present otherwise not
        next_page_id = first_payload['next_page_id']  # Get next page id because further API call require this to get information of particular page
        # print('Type of response is: ' + str(type(first_payload))) 
        # print('Next page id is ' + next_page_id)
        while 1:   # Running infinite loop till next_page_id absent from response, because last page will not have next_page_id
            # print("I am in while loop")
            # Making another API call get information for next page and so on till lastpage
            next_call = successive_api_call(endpoint=endpoint, page_id=next_page_id,user=user, passwd=user_pwd)
            # print(next_call)
            complete_data = complete_data + next_call['result']  # Merging from previous call to this call to get all data in one variable
            if 'next_page_id' in next_call:    # In last page of respnsoe next_psge_id will be absent
                next_page_id = next_call['next_page_id']  # Changing next page id for next call because we ave to move one by one ahead
            else:     
                break   # Breaking infite loop because we reached at last page of API call. 
        
    print("**************************************")
    print("Length of complete data : " + str(len(complete_data)))

    return complete_data

# Getting information from infoblox using page ids. 
def successive_api_call(endpoint, page_id, user, passwd):
    # print("I am in successive function")
    new_endpoint = str(endpoint) + str("&_page_id={id}".format(id=page_id))
    further_response = requests.get(url=new_endpoint, auth=HTTPBasicAuth(user,passwd), verify=False)
    return further_response.json()

# Write in excel file to record all data
def write_excel(device_info):
    excel_file = openpyxl.Workbook()
    current_sheet = excel_file.active
    current_sheet.append(['Device Name', 'Device IP address'])
    for name,ip in device_info.items():
        current_sheet.append([name, ip])
    excel_file.save('infoblox_data.xlsx')


def main():
    # Get username and password which will be used to get information from INfoblox
    username = str(input("Please enter your username of infoblox: "))
    password = str(getpass.getpass("Please enter password of username: "))
    infoblox_url = "https://infoblox.net"
    record_path = "/wapi/v2.10/record:host"

    # Constructing complete endpoint for first API call.
    first_complete_endpoint = str(infoblox_url) + str(record_path) + "?_max_results=2000&_paging=1&_return_as_object=1"
    # print(first_complete_endpoint)
    # Calling function to get infoblox data
    complete_response = get_first_host_record(endpoint = first_complete_endpoint, user=username, user_pwd=password)
    # first_response = requests.get(url="https://infoblox.net/wapi/v2.10/record:host?_max_results=20&_paging=1&_return_as_object=1", timeout=50, verify=False, auth=(username,password))
    # print(first_response)
    name_ip_dict = {}
    for item in complete_response:
        name_ip_dict.update({item['name']:item['ipv4addrs'][0]['ipv4addr']})
    
    # print("Complete required dictionary")
    # print(name_ip_dict)
    write_excel(name_ip_dict)


if __name__ == "__main__":
    main()
