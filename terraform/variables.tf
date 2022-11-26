variable "instance_vars"{
  type = map (
    object({
      image_id = string,
      host_type = string,
      image_name = string,
      security_group_name = string
    })
  )
}

variable "security_group_vars"{
  type = map (
    object({
      name = string
    })
  )
}

variable "user_vars"{
  type = map (
    object({
      name = string,
      reset_password = bool,
      user_policy = string
  }))
}

variable "security_group_rule_vars"{
  type = map (
    object({
      type = string,
      from_port        = number,
      to_port          = number,  
      protocol         = string,
      cidr_blocks      = list(string),
      ipv6_cidr_blocks = list(string),
      security_group_name = string
    })
  )
}

variable "create_HA_infrastructure" {
  type = bool
}