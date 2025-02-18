# provider "aws" {
#   region = var.aws_region
# }
# # Create a VPC
# resource "aws_vpc" "main" {
#   cidr_block = var.main_vpc_cidr_block
#   enable_dns_support = "true" 
#   enable_dns_hostnames = "true"
#   tags = {
#         Name = "terra-vpc"
#     }

# }
# resource "aws_subnet" "terra-pub-sub1" {
#   vpc_id = aws_vpc.main.id
#   cidr_block = var.my-public-subnet_cidr_block
#   map_public_ip_on_launch = "true"
#   availability_zone = "us-east-1a"
#   tags = {
#         Name = "terra-pub-sub1"
#     }
# }
# resource "aws_subnet" "terra-priv-sub1" {
#   vpc_id = aws_vpc.main.id
#   cidr_block = var.my-private-vpc_cidr_block
#   availability_zone = "us-east-1a"
#   tags  = {
#     Name = "terra-pub-sub1"
#     }
# }
# resource "aws_internet_gateway" "gw" {
#   vpc_id = aws_vpc.main.id

#   tags = {
#     Name = "main"
#   }
# }
# resource "aws_route_table" "my_Public_Route_table" {
#     vpc_id = aws_vpc.main.id

#     route {
#         cidr_block = "0.0.0.0/0"
#         gateway_id = aws_internet_gateway.gw.id
#     }

#     tags = {
#         Name = "Public Subnet Route Table."
#     }
# }

# resource "aws_route_table_association" "my_public_RT_association" {
#     subnet_id = aws_subnet.terra-pub-sub1.id
#     route_table_id = aws_route_table.my_Public_Route_table.id
   
# }

# resource "aws_route_table" "my_Private_Route_table" {
#     vpc_id = aws_vpc.main.id
#     tags = {
#         Name = "Private Subnet Route Table."
#     }
# }

# resource "aws_route_table_association" "my_private_RT_association" {
#     subnet_id = aws_subnet.terra-priv-sub1.id
#     route_table_id = aws_route_table.my_Private_Route_table.id
    
# }

# resource "aws_security_group" "allow-http" {
#   name        = "allow-http"
#   description = "Allow inbound traffic"
#   vpc_id      = aws_vpc.main.id

#   ingress {
#       description      = "HTTP from every where"
#       from_port        = 80
#       to_port          = 80
#       protocol         = "tcp"
#       cidr_blocks      = ["0.0.0.0/0"]
      
#     }
  
#   egress {
#       from_port        = 0
#       to_port          = 0
#       protocol         = "-1"
#       cidr_blocks      = ["0.0.0.0/0"]
#       ipv6_cidr_blocks = ["::/0"]
#     }

#   tags = {
#     Name = "allow_http"
#   }
# }
# resource "aws_security_group" "allow-ssh" {
#   name        = "allow-shh"
#   description = "Allow inbound traffic"
#   vpc_id      = aws_vpc.main.id


#   ingress {
#       description      = "ssh from VPC"
#       from_port        = 22
#       to_port          = 22
#       protocol         = "tcp"
#       cidr_blocks      = [aws_vpc.main.cidr_block]
      
#     }
  
#   egress {
#       from_port        = 0
#       to_port          = 0
#       protocol         = "-1"
#       cidr_blocks      = ["0.0.0.0/0"]
#       ipv6_cidr_blocks = ["::/0"]
#     }

#   tags = {
#     Name = "allow_ssh"
#   }
# }

# variable "aws_region" {
#     type = string
#     description = "my region"
#     default = "us-east-1"
# }

# variable "main_vpc_cidr_block" {
#     type = string
#     description = "my main vpc cidr block terra vpc"
#     default = "10.0.0.0/16"
# }
# variable "my-public-subnet_cidr_block" {
#     type = string
#     description = "my public subnet cidr bloc"
#     default = "10.0.0.0/24"
# }
# variable "my-private-vpc_cidr_block" {
#     type = string
#     description = "my private vpc cidr bloc"
#     default = "10.0.1.0/24"
# }

# variable "instance_type" {
#     type = string
#     description = "instance_type"
#     default = "t2.micro"
# }
# variable "instance_key_pair" {
#     type = string
#     description = "my terraform key"
#     default = "terraform-labs-key"
# }
# variable "VPC-cidr-block" {
#     type = string
#     description = "my vpc-cidr"
#     default = "terraform-labs-key"
# }


# data "aws_ami" "my-ami" {
#   most_recent      = true
#   owners           = ["amazon"]

#   filter {
#     name   = "name"
#     values = ["amzn2-ami-hvm-2.0.*.1-x86_64-gp2"]
#   }

# }
# resource "aws_instance" "my_private_instance" {
#   ami           = data.aws_ami.my-ami.id
#   instance_type = var.instance_type
#   key_name = var.instance_key_pair
#   vpc_security_group_ids = [aws_security_group.allow-ssh.id]
#   subnet_id = aws_subnet.terra-priv-sub1.id
#   tags = {
#     Name = "my_private_instance"
#   }
# }
# resource "aws_instance" "my_public_instance" {
#   ami = data.aws_ami.my-ami.id
#   instance_type = var.instance_type
#   key_name = var.instance_key_pair
#   vpc_security_group_ids = [aws_security_group.allow-ssh.id, aws_security_group.allow-http.id]
#   subnet_id = aws_subnet.terra-pub-sub1.id
#   tags = {
#     Name = "my_public_instance"
#   }
# }