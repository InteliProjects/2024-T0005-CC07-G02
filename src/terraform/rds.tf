resource "aws_db_subnet_group" "rds_subnet_group" {
  name        = "meu-grupo-de-subnets-rds"
  description = "Grupo de subnets do RDS para instâncias privadas"
  subnet_ids  = [aws_subnet.private.id, aws_subnet.private2.id] # Substitua pelos IDs das suas subnets privadas

  tags = {
    Name = "RDS-Subnet-Group"
  }
}

resource "aws_db_instance" "internet_db" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0.35"
  instance_class       = "db.t3.micro"
  db_subnet_group_name = aws_db_subnet_group.rds_subnet_group.name
  identifier           = "internet-db"
  db_name              = "internetdb"
  username             = "root"
  password             = "password"
  skip_final_snapshot  = true

  # Configurações de segurança
  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  tags = {
    Name = "InternetDB"
  }
}

resource "aws_db_instance" "telefonia_db" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0.35"
  instance_class       = "db.t3.micro"
  db_subnet_group_name = aws_db_subnet_group.rds_subnet_group.name
  identifier           = "telefonia-db"
  db_name              = "telefoniadb"
  username             = "root"
  password             = "password"
  skip_final_snapshot  = true

  # Configurações de segurança
  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  tags = {
    Name = "TelefoniaDB"
  }
}

resource "aws_db_instance" "outros_db" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0.35"
  instance_class       = "db.t3.micro"
  db_subnet_group_name = aws_db_subnet_group.rds_subnet_group.name
  identifier           = "outros-db"
  db_name              = "outrosdb"
  username             = "root"
  password             = "password"
  skip_final_snapshot  = true

  # Configurações de segurança
  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  tags = {
    Name = "OutrosDB"
  }
}

resource "aws_db_instance" "fatura_db" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0.35"
  instance_class       = "db.t3.micro"
  db_subnet_group_name = aws_db_subnet_group.rds_subnet_group.name
  identifier           = "fatura-db"
  db_name              = "faturadb"
  username             = "root"
  password             = "password"
  skip_final_snapshot  = true

  # Configurações de segurança
  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  tags = {
    Name = "FaturaDB"
  }
}

resource "aws_db_instance" "cadastro_db" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0.35"
  instance_class       = "db.t3.micro"
  db_subnet_group_name = aws_db_subnet_group.rds_subnet_group.name
  identifier           = "cadastro-db"
  db_name              = "cadastrodb"
  username             = "root"
  password             = "password"
  skip_final_snapshot  = true

  # Configurações de segurança
  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  tags = {
    Name = "OutrosDB"
  }
}