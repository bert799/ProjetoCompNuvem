resource "aws_instance" "app_server" {
  for_each        = var.instance_vars
  ami             = each.value.image_id
  instance_type   = each.value.host_type
  
  subnet_id       = aws_subnet.subnet_projeto.id
  security_groups = [each.value.security_group_id != "" ? each.value.security_group_id : aws_security_group.default_sec_group.id]

  tags = {
    Name          = each.value.image_name
  }
}