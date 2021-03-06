provider "aws" {
  region = "us-east-1"
}

//variable "key_name" {}
//
//resource "tls_private_key" "example" {
//  algorithm = "RSA"
//  rsa_bits  = 4096
//}
//
//resource "aws_key_pair" "generated_key" {
//  key_name   = "${var.key_name}"
//  public_key = "${tls_private_key.example.public_key_openssh}"
//}

data "template_file" "userdata" {
  template = "${file("terraform-deploy.sh")}"
}

resource "aws_instance" "example" {
  ami = "ami-013be31976ca2c322"
  instance_type = "t2.micro"
  vpc_security_group_ids = ["${aws_security_group.instance.id}"]
  key_name = "ec2"
//  provisioner "file" {
//    source = "terraform-deploy.sh"
//    destination = "tmp/terraform-deploy.sh"
//    connection {
//      type = "ssh"
//      user = "ubuntu"
//    }
//  }
//
//  provisioner "remote-exec" {
//    inline = [
//      "chmod +x /tmp/terraform-deploy.sh",
//      "/tmp/terraform-deploy.sh"
//    ]
//  }
  user_data = "${file("terraform-deploy.sh")}"
  tags {
    Name = "terraform-example"
  }
}

resource "aws_security_group" "instance" {
  name = "terraform-example-DMZ"
  ingress {
    from_port = "${var.server_port}"
    to_port = "${var.server_port}"
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port = "${var.ssh_port}"
    to_port = "${var.ssh_port}"
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "public_ip" {
  value = "${aws_instance.example.public_ip}"
}