resource "aws_instance" "BACKEND-SERVER" {
    ami = "ami-0fc5d935ebf8bc3bc"
    instance_type = "t2.micro"
    key_name = aws_key_pair.ssh_key.key_name
    count=1

    tags = {
        Name = "Server Instance"

    }
}