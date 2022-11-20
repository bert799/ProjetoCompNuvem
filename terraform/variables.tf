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
      name = string,
      ingress = object({
        description      = string,
        from_port        = number,
        to_port          = number,  
        protocol         = string,
        cidr_blocks      = list(string),
        ipv6_cidr_blocks = list(string)
      })
    })
  )
}