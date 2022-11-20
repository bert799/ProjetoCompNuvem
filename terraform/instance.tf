resource "aws_instance" "app_server" {
  for_each        = var.instance_vars
  ami             = each.value.image_id
  instance_type   = each.value.host_type
  
  subnet_id       = aws_subnet.subnet_projeto.id
  vpc_security_group_ids = [aws_security_group.custom_sec_group[lookup(var.security_group_vars, each.value.security_group_name, null).name].id]

  tags = {
    Name          = each.value.image_name
  }
}
