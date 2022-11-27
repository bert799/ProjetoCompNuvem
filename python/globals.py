def initialize():
    global region
    global HA_enabled
    global ami_dict
    global host_types_list
    global user_policies

    region = "us-east-1"

    HA_enabled = False

    ami_dict = {
        "us-east-1" : {
            "Ubuntu 22.04": "ami-08c40ec9ead489470",
            "Ubuntu 20.04": "ami-0149b2da6ceec4bb0",
            "Ubuntu 18.04": "ami-0ee23bfc74a881de5"
        },
        "us-east-2" : {
            "Ubuntu 22.04": "ami-097a2df4ac947655f",
            "Ubuntu 20.04": "ami-0d5bf08bc8017c83b",
            "Ubuntu 18.04": "ami-0a59f0e26c55590e9"
        }
    }

    host_types_list = ['t2.nano', 't2.micro']

    user_policies = ["admin", "read_only"]

def change_region():
    global region
    if region == 'us-east-1':
        region = 'us-east-2'
    else:
        region = 'us-east-1'