resource "aws_key_pair" "ssh_key" {
  key_name = "ssh_key"
  public_key = file("/Users/irehankhan/.ssh/id_rsa.pub")
}