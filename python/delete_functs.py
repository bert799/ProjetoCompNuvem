import time
import globals
import general_functs
import list_functs

def delete_infrastructure():
    general_functs.clear_terminal()
    while(True):
        print(f'''        Current Region:{globals.region}

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
            delete_instance()
        elif option == 2:
            delete_sec_group()
        elif option == 3:
            delete_sec_group_rule()
        elif option == 4:
            delete_user()
        elif option == 5:
            delete_high_availability()
        elif option == 6:
            print('option 6')
            return None        
        else:
            input('Invalid option, press any key to continue.')
            general_functs.clear_terminal()
        general_functs.clear_terminal()

def delete_instance():
    general_functs.clear_terminal()
    data = general_functs.read_json()
    inst_dict = data['instance_vars']
    list_functs.list_instances()
    inst_index = int(input('What is the index of the instance that you want to delete? '))
    inst_key =  list(inst_dict.keys())[inst_index]
    general_functs.delete_from_infr('instance_vars', inst_key)

def delete_sec_group():
    general_functs.clear_terminal()
    data = general_functs.read_json()
    sec_group_dict = data['security_group_vars']
    sec_group_rules_dict = data['security_group_rule_vars']
    list_functs.list_sec_groups()
    sec_group_index = int(input('What is the index of the security group that you want to delete? '))
    sec_group_key =  list(sec_group_dict.keys())[sec_group_index]
    for rule_key, rule_value in sec_group_rules_dict.items():
        if rule_value['security_group_name'] == sec_group_key:
            general_functs.delete_from_infr('security_group_rule_vars', rule_key)
            print(f'Rule: {rule_key} deleted successfully')
    general_functs.delete_from_infr('security_group_vars', sec_group_key)
    print(f'Security Group: {sec_group_key} deleted successfully')

def delete_sec_group_rule():
    general_functs.clear_terminal()
    data = general_functs.read_json()
    sec_group_dict = data['security_group_vars']
    sec_group_rules_dict = data['security_group_rule_vars']
    list_functs.list_sec_groups()
    sec_group_index = int(input('What is the index of the security group that you want to delete a rule from? '))
    sec_group_rule_index = int(input('What is the number of the rule that you want to delete? '))
    sec_group_key =  list(sec_group_dict.keys())[sec_group_index]
    sec_group_rule_key = list(sec_group_rules_dict.keys())[sec_group_rule_index]
    general_functs.delete_from_infr('security_group_rule_vars', sec_group_rule_key)
    print(f'Security Group {sec_group_key} rule: {sec_group_rule_key} deleted successfully')
    time.sleep(1)

def delete_user():
    general_functs.clear_terminal()
    data = general_functs.read_json()
    users_dict = data['user_vars']
    list_functs.list_users()
    user_index = int(input('What is the index of the user that you want to delete? '))
    user_key =  list(users_dict.keys())[user_index]
    general_functs.delete_from_infr('user_vars', user_key)
    print(f'User {user_key} deleted successfully')
    time.sleep(1)

def delete_high_availability():
    infr = general_functs.read_json()
    if (infr['create_HA_infrastructure'] != False):
        infr['create_HA_infrastructure'] = False
        general_functs.write_json(infr)
        print(f'High availability setting sucessfully removed from the configuration file!')
    else: 
        print('High availability already disabled.')
    time.sleep(1)