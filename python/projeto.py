import os
import json
import classes
import time
from create_functs import *
from general_functs import *
from delete_functs import *
from list_functs import * 

current_region = "us-east-1"

HA_enabled = False

ami_dict = {
    "us-east-1" : {
        "Ubuntu 22.04": "",
        "Ubuntu 20.04": "",
        "Ubuntu 18.04": ""
    },
    "us-east-2" : {
        "Ubuntu 22.04": "",
        "Ubuntu 20.04": "",
        "Ubuntu 18.04": ""
    }
}

host_types_list = ['t2.nano', 't2.micro']

user_policies = ["admin", "read_only"]


def main_menu():
    while(True):
        print('''
        1: Create new infrastructure
        2: List infrastructure
        3: Delete infrastructure
        4: Change region
        5: Apply
        6: Exit
        ''')
        option = int(input('Select an option: '))
        if option == 1:
            print('option 1')
            clear_terminal()
            create_infrastructure()
        elif option == 2:
            print('option 2')
            return None
        elif option == 3:
            print('option 3')
            return None
        elif option == 4:
            print('option 4')
            return None
        elif option == 5:
            print('option 5')
            return None
        elif option == 6:
            clear_terminal()
            return 1       
        else:
            input('Invalid option, press any key to continue.')
            clear_terminal()
        clear_terminal()


def main():
    while(True):    
        clear_terminal()
        status = main_menu()
        if status == 1:
            return

if __name__=="__main__":
    main()
    