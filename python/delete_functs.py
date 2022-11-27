import time
from general_functs import *
from projeto import ami_dict, host_types_list, user_policies


def delete_high_availability():
    infr = read_json()
    infr['create_HA_infrastructure'] = False
    write_json(infr)
    print(f'high_availability setting sucessfully removed from the configuration file!')
    time.sleep(1)