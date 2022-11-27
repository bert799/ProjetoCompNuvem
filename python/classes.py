class instance:
    def __init__(self, image_id, host_type, image_name, security_group_name):
        self.image_id = image_id
        self.host_type = host_type
        self.image_name = image_name
        self.security_group_name = security_group_name

class user:
    def __init__(self, name, reset_password, user_policy):
        self.name = name
        self.reset_password = reset_password
        self.user_policy = user_policy

class security_group:
    def __init__(self, name):
        self.name = name

class security_group_rule:
    def __init__(self, type, from_port, to_port, protocol, cidr_blocks, ipv6_cidr_blocks, security_group_name):
        self.type = type
        self.from_port = from_port
        self.to_port = to_port
        self.protocol = protocol
        self.cidr_blocks = cidr_blocks
        self.ipv6_cidr_blocks = ipv6_cidr_blocks
        self.security_group_name = security_group_name
