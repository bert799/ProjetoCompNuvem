class instance:
    def __init__(self, image_id, host_type, image_name, security_group_id):
        self.image_id = image_id
        self.host_type = host_type
        self.image_name = image_name
        self.security_group_id = security_group_id

class user:
    def __init__(self, name):
        self.name = name

class security_group:
    def __init__(self, vpc_id, egress, ingress):
        self.vpc_id = vpc_id
        self.egress = egress
        self.ingress = ingress