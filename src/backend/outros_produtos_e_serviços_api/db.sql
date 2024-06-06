-- Tabela de planos
CREATE TABLE PLANOS (
  ID UUID PRIMARY KEY NOT NULL DEFAULT uuid_generate_v4(),
  Tipo_servico VARCHAR(50) NOT NULL,
  Descricao VARCHAR(255) NOT NULL,
  Preco DECIMAL(10,2) NOT NULL,
  -- Adicionar mais campos se necessário
);

-- Tabela de serviços contratados
CREATE TABLE SERVICOS_CONTRATADOS (
  ID UUID PRIMARY KEY NOT NULL DEFAULT uuid_generate_v4(),
  ID_Plano UUID NOT NULL,
  ID_Cliente UUID NOT NULL,
  Data_Contratacao DATE NOT NULL,
  Data_Cancelamento DATE,
  -- Adicionar mais campos se necessário
  FOREIGN KEY (ID_Plano) REFERENCES PLANOS(ID),
);