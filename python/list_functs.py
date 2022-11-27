import classes
import time
from general_functs import *
from projeto import ami_dict, host_types_list, user_policies, current_region

def list_instances():
    data = read_json()
    instances = data['instance_vars']
    print(f'Instances in region {current_region}:')
    for value in instances.value():
        print(value)

def list_users():
    data = read_json()
    user = data['user_vars']
    print(f'Users created:')
    for value in user.value():
        print(value)    
    
def list_sec_groups():
    data = read_json()
    sec_groups = data['security_group_vars']
    sec_groups_rules = data['security_group_rule_vars'] 
    print(f'Security groups and their rules:.') 
    for sec_group_name in sec_groups.keys():
        print(sec_group_name)
        print('rules:')
        for rule_key, rule_value in sec_groups_rules.items():
            if rule_value.security_group_name == sec_group_name:
                print(rule_key)
                print(rule_value)
