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

    ingress     = each.value.ingress

    tags = {
        Name    = "custom_bernie"
    }
}