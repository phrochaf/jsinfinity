Documentação do Projeto: Sistema de Gerenciamento de Segurança das Indústrias Wayne
Sumário
Introdução
Arquitetura do Sistema
Instalação e Configuração
Estrutura do Banco de Dados
Rotas e Funcionalidades
Exemplo de Uso
Considerações Finais


Introdução
O Sistema de Gerenciamento de Segurança das Indústrias Wayne é uma aplicação web desenvolvida em Flask para gerenciar a segurança e os recursos internos da empresa. A aplicação permite o registro, edição e exclusão de recursos, bem como a autenticação e autorização de usuários com diferentes níveis de acesso.

Arquitetura do Sistema
A arquitetura do sistema é baseada na arquitetura MVC (Model-View-Controller):

Model: Interage com o banco de dados MySQL para realizar operações de CRUD (Criar, Ler, Atualizar, Deletar).
View: Utiliza Jinja2 para renderizar templates HTML dinâmicos, apresentando dados ao usuário.
Controller: Gerencia as rotas e a lógica de negócios, conectando o modelo à visualização.
Instalação e Configuração
Pré-requisitos
Python 3.x
MySQL
Bibliotecas: Flask, Flask-MySQLdb, Werkzeug
Passos de Instalação
Clone o repositório:

bash
Copiar código
git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_PROJETO>
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate  # Windows
Instale as dependências:

bash
Copiar código
pip install Flask Flask-MySQLdb Werkzeug
Configuração do Banco de Dados:

Certifique-se de que o MySQL está em execução.
Crie um banco de dados chamado wayne_security.
Importe as tabelas necessárias (exemplo abaixo).
Inicie a aplicação:

bash
Copiar código
python app.py
Estrutura do Banco de Dados
sql
Copiar código
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('employee', 'manager', 'security_admin') NOT NULL
);

CREATE TABLE resources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    description TEXT,
    status ENUM('active', 'inactive') NOT NULL
);
Rotas e Funcionalidades
Rota	Método	Descrição
/	GET	Página inicial.
/login	GET, POST	Página de login para autenticação de usuários.
/register	GET, POST	Página de registro de novos usuários.
/employee_dashboard	GET	Dashboard para funcionários.
/manager_dashboard	GET	Dashboard para gerentes.
/security_admin_dashboard	GET	Dashboard para administradores de segurança.
/logout	GET	Realiza o logout do usuário.
/resources	GET	Exibe todos os recursos (apenas para admin de segurança).
/view_resources	GET	Visualiza todos os recursos.
/register_resource	GET, POST	Registra novos recursos (apenas para gerentes/admins).
/edit_resource/<id>	GET, POST	Edita um recurso existente.
/delete_resource/<id>	POST	Deleta um recurso existente.
Exemplo de Uso
Login:

O usuário acessa /login e insere suas credenciais.
Após a autenticação bem-sucedida, é redirecionado para seu respectivo dashboard.
Registro de Recursos (apenas para gerentes e administradores):

Acesse /register_resource para adicionar um novo recurso.
Preencha os campos necessários e envie o formulário.
Visualização de Recursos:

Acesse /view_resources para visualizar todos os recursos registrados.
Considerações Finais
Este projeto visa fornecer uma solução prática e segura para o gerenciamento de segurança e recursos nas Indústrias Wayne. O sistema pode ser estendido com funcionalidades adicionais, como relatórios detalhados e notificações em tempo real. Sinta-se à vontade para contribuir e aprimorar a aplicação!

