import time
from general_functs import *
from projeto import ami_dict, host_types_list, user_policies

def delete_infrastructure():
    while(True):
        print('''
        Choose what to delete:

        1: Instance
        2: Security Group
        3: Security Group rule
        4: User
        5: High-availability web-service
        6: Back        
        ''')
        option = int(input('Select an option: '))
        if option == 1:
            create_instance()
        elif option == 2:
            create_security_group()
        elif option == 3:
            create_security_group_rule()
        elif option == 4:
            create_user()
        elif option == 5:
            create_high_availability()
        elif option == 6:
            print('option 6')
            return None        
        else:
            input('Invalid option, press any key to continue.')
            clear_terminal()
        clear_terminal()

def delete_high_availability():
    infr = read_json()
    infr['create_HA_infrastructure'] = False
    write_json(infr)
    print(f'high_availability setting sucessfully removed from the configuration file!')
    time.sleep(1)