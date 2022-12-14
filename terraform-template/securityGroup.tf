resource "aws_security_group" "default_sec_group" {
    name        = "default_project_bernardo"
    vpc_id      = aws_vpc.vpc_projeto.id

    ingress {
        description      = "TLS from VPC"
        from_port        = 443
        to_port          = 443
        protocol         = "tcp"
        cidr_blocks      = ["0.0.0.0/0"]
        ipv6_cidr_blocks = ["::/0"]
    }

    egress {
        from_port        = 0
        to_port          = 0
        protocol         = "-1"
        cidr_blocks      = ["0.0.0.0/0"]
        ipv6_cidr_blocks = ["::/0"]
    }

    tags = {
        Name = "default_bernie"
    }
}

resource "aws_security_group" "custom_sec_group" {
    for_each    = var.security_group_vars
    name        = each.value.name
    vpc_id      = aws_vpc.vpc_projeto.id

    tags = {
        Name    = "custom_bernie"
    }
}

resource "aws_security_group_rule" "add_rule" {
    for_each = var.security_group_rule_vars
    type              = each.value.type
    from_port         = each.value.from_port
    to_port           = each.value.to_port
    protocol          = each.value.protocol
    cidr_blocks       = each.value.cidr_blocks
    ipv6_cidr_blocks  = each.value.ipv6_cidr_blocks
    security_group_id = aws_security_group.custom_sec_group[lookup(var.security_group_vars, each.value.security_group_name, null).name].id
}