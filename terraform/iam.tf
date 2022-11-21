locals {
    policies = {
        policy_admin ={
            name = "admin"
            policy =<<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
EOF
        }

        policy_read_only ={
            name = "read_only"
            policy =<<EOF
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "iam:Get*",
            "iam:List*",
            "iam:Generate*",
            "iam:ChangePassword"
        ],
        "Resource": "*",
        "Sid": "FirstStatement"
    }   
}
EOF
        }
    }
  
}

resource "aws_iam_user" "user_bernardo" {
    for_each = var.user_vars
    
    name = each.value.name

    tags = {
        tag-key = "users-bernardo"
    }
}

resource "aws_iam_user_login_profile" "login_bernardo" {
    for_each = var.user_vars

    user    = aws_iam_user.user_bernardo[each.key].name
    password_reset_required = each.value.reset_password

}

resource "aws_iam_user_policy" "user_policy_bernardo" {
    for_each = var.user_vars
    name = "test"
    user = aws_iam_user.user_bernardo[each.key].name

    # Terraform's "jsonencode" function converts a
    # Terraform expression result to valid JSON syntax.
    policy = lookup(local.policies, each.value.user_policy, local.policies.policy_read_only).policy
}

output "password" {
    value = [for password in aws_iam_user_login_profile.login_bernardo : password]
}

