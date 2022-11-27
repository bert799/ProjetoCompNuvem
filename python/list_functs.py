import time
import general_functs
import globals
import pprint

def list_infrastructure():
    general_functs.clear_terminal()
    while(True):
        print(f'''        Current Region:{globals.region}

        Choose what to list:
        
        1: Instances
        2: Security Groups
        3: User
        4: High-availability web-service
        5: Change region
        6: Back       
        ''')
        option = int(input('Select an option: '))
        if option == 1:
            list_instances()
            input('Press any key to continue.')
        elif option == 2:
            list_sec_groups()
            input('Press any key to continue.')
        elif option == 3:
            list_users()
            input('Press any key to continue.')
        elif option == 4:
            list_high_availability()
            input('Press any key to continue.')
        elif option == 5:
            general_functs.clear_terminal()
            globals.change_region()
            print(f'Region Changed to {globals.region}')
            time.sleep(1)
        elif option == 6:
            print('option 6')
            return None        
        else:
            input('Invalid option, press any key to continue.')
            general_functs.clear_terminal()
        general_functs.clear_terminal()

def list_instances():
    general_functs.clear_terminal()
    data = general_functs.read_json()
    instances = data['instance_vars']
    print(f'Instances in region {globals.region}:\n')
    i = 0
    for value in instances.values():
        print(f'{i}: ', end="")
        pprint.pprint(value)
        print('\n')
        i += 1

def list_users():
    general_functs.clear_terminal()
    data = general_functs.read_json()
    user = data['user_vars']
    print(f'Users created:\n')
    i = 0
    for value in user.values():
        print(f'{i}: ', end="")
        pprint.pprint(value, sort_dicts=False)
        print('\n')
        i += 1 
    
def list_sec_groups():
    general_functs.clear_terminal()
    data = general_functs.read_json()
    sec_groups = data['security_group_vars']
    sec_groups_rules = data['security_group_rule_vars'] 
    print(f'Security groups and their rules:\n\n')
    i = 0 
    for sec_group_name in sec_groups.keys():
        print(f'{i}: {sec_group_name}\n')
        print('rules:\n')
        j = 0
        for rule_key, rule_value in sec_groups_rules.items():
            if rule_value['security_group_name'] == sec_group_name:
                print(f'rule {j}: {rule_key}\n')
                pprint.pprint(rule_value, sort_dicts=False)
                print('\n')
                j += 1
        i += 1

def list_sec_groups_rules(sec_group):
    general_functs.clear_terminal()
    data = general_functs.read_json()
    sec_groups_rules = data['security_group_rule_vars'] 
    print(f'Rules of security group {sec_group}:\n\n')
    i = 0 
    for rule_key, rule_value in sec_groups_rules.items():
        if rule_value['security_group_name'] == sec_group:
            print(rule_key,'\n')
            pprint.pprint(rule_value, sort_dicts=False)
            print('\n')
            i += 1

def list_high_availability():
    general_functs.clear_terminal()
    infr = general_functs.read_json()
    status = bool(infr['create_HA_infrastructure'])
    if status == True:
        print(f'High availability service is enabled in this region!')
    else:
        print(f'High availability service is disabled in this region!')