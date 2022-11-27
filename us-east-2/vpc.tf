data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "vpc_projeto" {
  cidr_block = "172.16.0.0/16"

  tags = {
    Name = "vpc-proj-bernie"
  }
}

resource "aws_subnet" "subnet_projeto" {
  vpc_id            = aws_vpc.vpc_projeto.id
  cidr_block        = "172.16.10.0/24"

  tags = {
    Name = "subnet-proj-bernie"
  }
}

resource "aws_subnet" "subnet_asg" {
  count = 3
  vpc_id            = aws_vpc.vpc_projeto.id
  cidr_block        = ["172.16.11.0/24", "172.16.12.0/24", "172.16.13.0/24"][count.index]
  availability_zone = "${data.aws_availability_zones.available.names[count.index]}"
  map_public_ip_on_launch = true

  tags = {
    Name = "subnet-asg-proj-bernie-${count.index}"
  }
}

resource "aws_internet_gateway" "IGW" {
    vpc_id = aws_vpc.vpc_projeto.id
    tags = {
        Name = "Internet-gateway-bernardo"
    }
} 

resource "aws_route_table" "route_table_bernardo" {
    vpc_id = aws_vpc.vpc_projeto.id
    tags = {
        Name = "Public Route table"
    }
}

resource "aws_route" "internet_access" {
    route_table_id         = aws_route_table.route_table_bernardo.id
    destination_cidr_block = "0.0.0.0/0"
    gateway_id             = aws_internet_gateway.IGW.id
}

resource "aws_route_table_association" "Public_association" {
    subnet_id      = aws_subnet.subnet_projeto.id
    route_table_id = aws_route_table.route_table_bernardo.id
}

resource "aws_route_table_association" "Public_association_asg" {
    count = 3
    subnet_id      = aws_subnet.subnet_asg[count.index].id
    route_table_id = aws_route_table.route_table_bernardo.id
}