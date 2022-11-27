resource "aws_launch_configuration" "web_service" {
  count = var.create_HA_infrastructure ? 1 : 0
  name_prefix     = "bernardo-asg-"
  image_id        = "	ami-0e291adf79e91660a"
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.web_service_instance[count.index].id]
  key_name = "bernardo"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "web_service" {
  count = var.create_HA_infrastructure ? 1 : 0
  name                 = "web-service"
  min_size             = 1
  max_size             = 3
  desired_capacity     = 1
  launch_configuration = aws_launch_configuration.web_service[count.index].name
  vpc_zone_identifier  = aws_subnet.subnet_asg.*.id

  lifecycle { 
    ignore_changes = [desired_capacity, target_group_arns]
  }

  tag {
    key                 = "Name"
    value               = "HA-Instance-Bernardo"
    propagate_at_launch = true
  }
}

resource "aws_lb" "web_service" {
  count = var.create_HA_infrastructure ? 1 : 0
  name               = "bernardo-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.web_service_lb[count.index].id]
  subnets            = aws_subnet.subnet_asg.*.id
}

resource "aws_lb_listener" "web_service" {
  count = var.create_HA_infrastructure ? 1 : 0
  load_balancer_arn = aws_lb.web_service[count.index].arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.web_service[count.index].arn
  }
}

resource "aws_lb_target_group" "web_service" {
  count = var.create_HA_infrastructure ? 1 : 0
  name     = "asg-web-service"
  port     = 8080
  protocol = "HTTP"
  vpc_id   = aws_vpc.vpc_projeto.id
}


resource "aws_autoscaling_attachment" "web_service" {
  count = var.create_HA_infrastructure ? 1 : 0
  autoscaling_group_name = aws_autoscaling_group.web_service[count.index].id
  alb_target_group_arn   = aws_lb_target_group.web_service[count.index].arn
}

resource "aws_security_group" "web_service_instance" {
  count = var.create_HA_infrastructure ? 1 : 0
  name = "HA-sg-instance-bernardo"
  ingress {
    from_port       = 8080
    to_port         = 8080
    protocol        = "tcp"
    security_groups = [aws_security_group.web_service_lb[count.index].id]
  }

  ingress {
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 443
    to_port         = 443
    protocol        = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 80
    to_port         = 80
    protocol        = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    security_groups = [aws_security_group.web_service_lb[count.index].id]
  }

  vpc_id = aws_vpc.vpc_projeto.id
}

resource "aws_security_group" "web_service_lb" {
  count = var.create_HA_infrastructure ? 1 : 0
  name = "lb-sg-Bernardo"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  vpc_id = aws_vpc.vpc_projeto.id
}