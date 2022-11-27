import classes
import time
from general_functs import *
from projeto import ami_dict, host_types_list, user_policies


def create_infrastructure():
    while(True):
        print('''
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

def create_instance():
    clear_terminal()
    i = 1
    for name, ami in ami_dict[current_region].items():
        print(f'        {i}: Name: {name} | ami:{ami}')
        i += 1
    ami_selected = int(input('Please, select one of the above images for your instance: '))
    image_id = list(ami_dict[current_region].values())[ami_selected]
    clear_terminal()
    print('''
        1: t2.nano
        2: t2.micro
    ''')
    type = host_types_list[int(input('Please, select the type of your instance from on of the above: '))-1]
    clear_terminal()
    image_name = input('Insert a name for your instance: ')
    clear_terminal()
    security_group_name = input('(optional) give the name to a security group you wish to associate your instance with: ')
    if security_group_name == "":
        security_group_name = f"{image_name}-sg"
        auto_create_security_group(security_group_name)
        auto_create_security_group_rule(security_group_name)
        auto_create_security_group_rule(security_group_name, type="egress", from_port=0, to_port=0, protocol="-1")
    inst = classes.instance(image_id=image_id, host_type=type, image_name=image_name, security_group_name=security_group_name)
    add_to_infr('instance_vars', inst, image_name)
    print(f'Instance {image_name} sucessfully added to the configuration file!')
    time.sleep(1)

def create_security_group():
    clear_terminal()
    name = input('Insert a name for your security group: ')
    auto_create_security_group(name)
    create_security_group_rule(name=name)
    print(f'Security group {name} sucessfully added to the configuration file!')
    time.sleep(1)


def create_security_group_rule(name = ""):
    clear_terminal()
    if name == "":
        name = input('Insert the name of the security group you would like to add a rule to: ')
    clear_terminal()
    add_rule = input('Would you like to add a rule to your security group y/n: ')
    while(add_rule.lower() == 'y'):
        clear_terminal()        
        rule_type = input("What type of rule is this? (ingress/egress): ")
        rule_from_port = int(input("From which port should this rule apply? "))
        rule_to_port = int(input('To which port should this rule apply? '))
        rule_protocol = input('Which protocol should this rule use? ')
        ipv4 = [input('From which ipv4 addresses should connections be accepted? (0.0.0.0/0 accepts all) ')]
        if ipv4 == "":
            rule_cidr_blocks = []
        else:
            rule_cidr_blocks = ipv4        
        ipv6 = input('From which ipv6 addresses should connections be accepted? (::/0 accepts all) ')
        if ipv6 == "":
            rule_ipv6_cidr_blocks = []
        else:
            rule_ipv6_cidr_blocks = ipv6
        auto_create_security_group_rule(security_group_name=name, type=rule_type, from_port=rule_from_port, to_port=rule_to_port, protocol=rule_protocol, cidr_blocks=rule_cidr_blocks, ipv6_cidr_blocks=rule_ipv6_cidr_blocks)
        add_rule = input('Would you like to add another rule to your security group y/n: ')    

def auto_create_security_group(name):
    sg = classes.security_group(name=name)
    add_to_infr('security_group_vars', sg, sg.name)

def auto_create_security_group_rule(security_group_name, type = "ingress", from_port = 22, to_port = 22, protocol = "tcp", cidr_blocks = ['0.0.0.0/0'], ipv6_cidr_blocks = []):
    sg_rule = classes.security_group_rule(type=type, from_port=from_port, to_port=to_port, protocol=protocol, cidr_blocks=cidr_blocks, ipv6_cidr_blocks=ipv6_cidr_blocks, security_group_name=security_group_name)
    key_name = f'{security_group_name}-{type}-rule-port-{from_port}'
    add_to_infr('security_group_rule_vars', sg_rule, key_name)

def create_user():
    clear_terminal()
    name = input('Insert user name: ')
    clear_terminal()
    reset_password_query = input('Would you like for the user to have to reset his password on first login? (y/n) ').lower()
    if reset_password_query == 'y':
        reset_password = True
    elif reset_password_query == 'n':
        reset_password = False
    clear_terminal()
    print('''
    1: admin
    2: read_only
    ''')
    user_permissions = int(input("Select the level of permissions you would like the user to have: "))
    user_policy = user_policies[user_permissions-1]

    user = classes.user(name=name, reset_password=reset_password, user_policy=user_policy)
    add_to_infr('user_vars', user, user.name)
    print(f'User {name} sucessfully added to the configuration file!')
    time.sleep(1)

def create_high_availability():
    infr = read_json()
    infr['create_HA_infrastructure'] = True
    write_json(infr)
    print(f'high_availability setting sucessfully added to the configuration file!')
    time.sleep(1)