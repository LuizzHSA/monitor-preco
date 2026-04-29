
-- Tabela de Fornecedores
CREATE TABLE fornecedor (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	cnpj TEXT UNIQUE NOT NULL,
	contato TEXT
);

-- Tabela de Produtos
CREATE TABLE produto (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	descricao TEXT,
	categoria TEXT
);

-- Tabela de Preços
CREATE TABLE preco (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	produto_id INTEGER NOT NULL,
	fornecedor_id INTEGER NOT NULL,
	valor REAL NOT NULL,
	data_coleta DATE NOT NULL,
	FOREIGN KEY (produto_id) REFERENCES produto(id),
	FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id)
);

-- Tabela de Alertas
CREATE TABLE alerta (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	produto_id INTEGER NOT NULL,
	preco_id INTEGER NOT NULL,
	mensagem TEXT NOT NULL,
	data_alerta DATE NOT NULL,
	FOREIGN KEY (produto_id) REFERENCES produto(id),
	FOREIGN KEY (preco_id) REFERENCES preco(id)
);
