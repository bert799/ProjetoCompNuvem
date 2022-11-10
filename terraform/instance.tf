resource "aws_instance" "app_server" {
  for_each = var.instance_vars
  ami = each.value.image_id
  instance_type = each.value.host_type
  
  network_interface {
    network_interface_id = aws_network_interface.foo.id
    device_index         = 0
  }
  
  tags = {
    Name = each.value.image_name
  }
}