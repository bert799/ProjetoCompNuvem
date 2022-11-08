resource "aws_instance" "app_server" {
  ami = var.image_id
  ### AMI diferem aws e ubuntu
  instance_type = var.host_type
  
  network_interface {
    network_interface_id = aws_network_interface.foo.id
    device_index         = 0
  }
  
  tags = {
    Name = var.image_tag
  }
}