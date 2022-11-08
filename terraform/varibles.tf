variable "image_id" {
  type        = string
  description = "The id of the machine image (AMI) to use for the server. Por padrão é Ubuntu 18.04 HVM"
  default = "ami-0ee23bfc74a881de5"

  validation {
    condition     = length(var.image_id) > 4 && substr(var.image_id, 0, 4) == "ami-"
    error_message = "The image_id value must be a valid AMI id, starting with \"ami-\"."
  }
}

variable "host_type" {
  type        = string
  description = "The size of the machine used to run the instance. default is t2.micro"
  default = "t2.micro"
}

variable "image_tag" {
  type        = string
  description = "The tag of the image used to name it"
}