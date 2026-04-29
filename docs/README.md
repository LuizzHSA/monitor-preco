# 🚀 Monitor de precos — Sistema de Monitoramento de Preços

## 📌 Visão Geral

O **Monitor de Precos** é um sistema web leve para monitoramento de preços de fornecedores, com foco em **detecção de alterações** e **alertas inteligentes de vencimento**.

A solução permite que empresas acompanhem a evolução de preços e tomem decisões mais rápidas, evitando prejuízos com ofertas expiradas ou alterações inesperadas.

---

## 🎯 Problema que Resolve

Empresas frequentemente:

- Perdem prazos de ofertas
- Não percebem mudanças de preços em tempo hábil
- Não possuem histórico organizado para análise

👉 O Monitor resolve isso com **automação simples e visual clara**.

---

## 💡 Proposta de Valor

- 🔔 Alertas automáticos de alteração de preço
- ⏰ Notificação de vencimentos próximos ou expirados
- 📊 Visualização de histórico com gráficos
- ⚡ Sistema leve, rápido e fácil de usar

---

## 🧩 Funcionalidades

### 📦 Gestão de Produtos

- Cadastro e listagem de produtos
- Associação com fornecedores

### 🏢 Gestão de Fornecedores

- Cadastro simples
- Relacionamento com produtos

### 💰 Monitoramento de Preços

- Registro de preços com validade
- Controle de histórico

### 🔔 Sistema de Alertas

- Alterações de preço detectadas automaticamente
- Alertas de vencimento:
  - Próximo do vencimento
  - Vencido

### 📊 Dashboard

- Visão geral do sistema
- Indicadores principais
- Gráficos de evolução de preços

---

## 🧠 Regras de Negócio

### ✔ Detecção de Alteração

Ao cadastrar um novo preço:

- O sistema compara com o último valor registrado
- Caso haja diferença → gera alerta automático

### ✔ Controle de Vencimento

- Alertas são gerados antes do vencimento
- Alertas críticos para preços expirados

---

## 🏗️ Arquitetura do Projeto

### Backend

- Python (Flask)
- SQLite

### Frontend

- HTML, CSS, JavaScript puro
- Chart.js para gráficos

### Estrutura

```
monitor - precos/
├── backend/
├── frontend/
├── docs/
├── database.db
```

---

## 🗄️ Modelo de Dados

**Produtos**

- id
- nome
- descrição

**Fornecedores**

- id
- nome

**Preços**

- produto_id
- fornecedor_id
- valor
- data_inicio
- data_fim

**Alertas**

- tipo (ALTERACAO | VENCIMENTO)
- mensagem
- status (lido/não lido)

---

## 🔌 API (Resumo)

| Método | Endpoint  | Descrição       |
| ------ | --------- | --------------- |
| GET    | /produtos | Listar produtos |
| POST   | /produtos | Criar produto   |
| GET    | /precos   | Listar preços   |
| POST   | /precos   | Registrar preço |
| GET    | /alertas  | Listar alertas  |

---

## 🖥️ Interface

O sistema conta com:

- Dashboard com indicadores
- Listagem de dados
- Sistema de notificações
- Gráficos interativos

---

## 🚀 Como Executar o Projeto

### 1. Clonar repositório

```
git clone https://github.com/seu-usuario/pricewatch.git
```

### 2. Instalar dependências

```
pip install -r requirements.txt
```

### 3. Executar backend

```
python app.py
```

### 4. Abrir frontend

Abrir `index.html` no navegador

---

## 📈 Possíveis Evoluções

- Integração com APIs de fornecedores
- Notificações por e-mail ou WhatsApp
- Multiusuário com autenticação
- Versão SaaS

---

## 💼 Aplicações Reais

- Controle de compras
- Gestão de fornecedores
- Monitoramento de ofertas
- Apoio à tomada de decisão

---

## 🧠 Diferenciais

- Simples e eficiente
- Fácil de implementar
- Baixo custo
- Ideal para pequenas e médias empresas

---

## 📌 Autor

Desenvolvido por **Luiz Henrique**
Estudante de Análise e Desenvolvimento de Sistemas

---

## ⭐ Contribuição

Sinta-se à vontade para contribuir com melhorias ou sugestões.

---

## 📬 Contato

- LinkedIn: [luizzhsa](https://www.linkedin.com/in/luizhsa)
- Gmail: [Luiz](seniorlulu20@gmail.com)

---

> 💡 “Monitorar preços não é custo — é economia inteligente.”
