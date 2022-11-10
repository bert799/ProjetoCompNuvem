variable "instance_vars"{
  type = map (
    object({
      image_id = string,
      host_type = string,
      image_name = string
    })
  )
}