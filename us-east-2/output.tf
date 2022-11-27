output "password" {
  description = "Password of the created users"
  value = [for password in aws_iam_user_login_profile.login_bernardo : password]
}

output "lb_endpoint" {
  description = "URL of load balancer"
  value = [for lb in aws_lb.web_service : "http://${lb.dns_name}"]
}

output "application_endpoint" {
  description = "URL of the application associated with the load balancer"
  value = [for lb in aws_lb.web_service : "http://${lb.dns_name}/index.php"]
}

output "asg_name" {
  description = "Name of the auto-scaling group"
  value = [for asg in aws_autoscaling_group.web_service : asg.name]
}