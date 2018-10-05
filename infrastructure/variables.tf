variable "access_key" {
  default = "AKIAIUITY2ZKT3JY7Y7Q"
}

variable "secret_key" {
  default = "iBSwP1OMqfKb6VI+idzhAKlDtwMb+gCMZhjeOiMT"
}

variable "server_port" {
  description = "The port the server will use for HTTP requests"
  default = 8080
}

variable "ssh_port" {
  description = "The port server will use for SSH requests"
  default = 22
}