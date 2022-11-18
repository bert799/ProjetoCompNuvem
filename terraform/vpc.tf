resource "aws_vpc" "vpc_projeto" {
  cidr_block = "172.16.0.0/16"

  tags = {
    Name = "vpc-proj-bernie"
  }
}

resource "aws_subnet" "subnet_projeto" {
  vpc_id            = aws_vpc.vpc_projeto.id
  cidr_block        = "172.16.10.0/24"
  #availability_zone = "us-east-1"

  tags = {
    Name = "subnet-proj-bernie"
  }
}
