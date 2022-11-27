import json
import os
from projeto import current_region

def read_json():
    with open(f'../{current_region}/.auto.tfvars.json', 'r') as json_file:
        data = json.load(json_file)
    return data

def write_json(infra_dict):
    with open(f'../{current_region}/.auto.tfvars.json', 'w') as json_file:
       json.dump(infra_dict, json_file)

def add_to_infr(var_name, data, data_name):
    data_dict = convert_class_to_dict(data)
    infr = read_json()
    infr[var_name][data_name] = data_dict
    write_json(infr)

def delete_from_infr(var_name, data_name):
    infr = read_json()
    del infr[var_name][data_name]
    write_json(infr)

def convert_class_to_dict(object):
    dict_class = object.__dict__
    return dict_class

def clear_terminal():
    os.system("clear")