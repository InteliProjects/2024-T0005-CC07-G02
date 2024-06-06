resource "aws_instance" "bastion_host" {
  ami                    = "ami-0440d3b780d96b29d"
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.public.id
  key_name               = "morto"
  vpc_security_group_ids = [aws_security_group.bastion_sg.id]
  tags = {
    Name = "BastionHost"
  }
}

resource "aws_instance" "telefonia_api" {
  ami                    = "ami-0440d3b780d96b29d"  # Substitua pelo ID da AMI apropriada
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.private.id  # Use a subnet privada
  key_name               = "morto"

  vpc_security_group_ids = [aws_security_group.private_sg.id]  # Grupo de segurança para a instância na subnet privada

  tags = {
    Name = "TelefoniaAPI"
  }
}

resource "aws_instance" "internet_api" {
  ami                    = "ami-0440d3b780d96b29d"  # Substitua pelo ID da AMI apropriada
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.private.id  # Use a subnet privada
  key_name               = "morto"

  vpc_security_group_ids = [aws_security_group.private_sg.id]  # Grupo de segurança para a instância na subnet privada

  tags = {
    Name = "InternetAPI"
  }
}

resource "aws_instance" "outros_api" {
  ami                    = "ami-0440d3b780d96b29d"  # Substitua pelo ID da AMI apropriada
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.private.id  # Use a subnet privada
  key_name               = "morto"

  vpc_security_group_ids = [aws_security_group.private_sg.id]  # Grupo de segurança para a instância na subnet privada

  tags = {
    Name = "OutrosAPI"
  }
}

resource "aws_instance" "fatura_api" {
  ami                    = "ami-0440d3b780d96b29d"  # Substitua pelo ID da AMI apropriada
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.private.id  # Use a subnet privada
  key_name               = "morto"

  vpc_security_group_ids = [aws_security_group.private_sg.id]  # Grupo de segurança para a instância na subnet privada

  tags = {
    Name = "FaturaAPI"
  }
}

resource "aws_instance" "barramento_api" {
  ami                    = "ami-0440d3b780d96b29d"  # Substitua pelo ID da AMI apropriada
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.private.id  # Use a subnet privada
  key_name               = "morto"

  vpc_security_group_ids = [aws_security_group.private_sg.id]  # Grupo de segurança para a instância na subnet privada

  tags = {
    Name = "BarramentoAPI"
  }
}

resource "aws_instance" "cadastro_api" {
  ami                    = "ami-0440d3b780d96b29d"  # Substitua pelo ID da AMI apropriada
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.private.id  # Use a subnet privada
  key_name               = "morto"

  vpc_security_group_ids = [aws_security_group.private_sg.id]  # Grupo de segurança para a instância na subnet privada

  tags = {
    Name = "CadastroAPI"
  }
}