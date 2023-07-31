# API DjangoRestFramework e Frontend Django Templates

## Introdução
Este é o README do projeto que consiste em uma aplicação API usando o DjangoRestFramework para gerenciar usuários e um frontend usando Django Templates para autenticação e painel do usuário.

A API permite a criação, leitura, atualização e exclusão (CRUD) de usuários, e o frontend oferece as seguintes funcionalidades:

- Registro de novos usuários.
- Login e autenticação.
- Visualização de um painel com informações do usuário logado.
- Alteração de e-mail e senha.
- Exclusão da conta do usuário.

## Requisitos
Para executar o projeto, é necessário ter o Python e o Django instalados no ambiente. Além disso, certifique-se de que os seguintes pacotes estejam instalados:

- Django (utilizado no frontend).
- DjangoRestFramework (utilizado na API).

Você pode instalar os pacotes necessários usando o gerenciador de pacotes pip:

## Ambiente Virtual
Como uma boa prática, deve-se criar e ativar um ambiente virtual para que as dependências fiquem centralizadas no projeto

## Installation
```bash
python -m venv venv
venv/Scripts/activate
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install django
pip install djangorestframework
```

## Configuração
- Clone o repositório para sua máquina local.
- Acesse a pasta api_usuario para configurar a API e acesse a pasta frontend para configurar o frontend.
- Configuração da API (DjangoRestFramework)
- Abra o terminal e navegue para a pasta api_usuario.
- Execute as migrações do banco de dados:

```bash
python manage.py migrate
```
- Crie um superusuário para acessar o painel administrativo (opcional):
```bash
python manage.py createsuperuser
```
- Inicie o servidor da API:
```bash
python manage.py runserver
```

A API estará acessível em http://127.0.0.1:8000/api/users/.

## Configuração do Frontend (Django Templates)
- Abra o terminal e navegue para a pasta frontend.


## API Endpoints
A API fornece os seguintes endpoints:

- GET /api/users/: Obtém a lista de todos os usuários.
- POST /api/users/: Cria um novo usuário.
- GET /api/users/{id}/: Obtém os detalhes de um usuário específico.
- PUT /api/users/{id}/: Atualiza os detalhes de um usuário específico.
- DELETE /api/users/{id}/: Exclui um usuário específico.

## Frontend Views
O frontend oferece as seguintes visualizações:

- Login: /login/ - Permite que os usuários façam login na aplicação.
- Registro: /register/ - Permite que novos usuários se registrem na aplicação.
- Painel do Usuário: /dashboard/ - Exibe informações do usuário logado após o login.
- Alterar E-mail: /change_email/ - Permite que o usuário logado altere seu e-mail.
- Alterar Senha: /change_password/ - Permite que o usuário logado altere sua senha.
- Excluir Conta: /delete_account/ - Permite que o usuário logado exclua sua conta.

## Observações
- O frontend está configurado para consumir a API da URL http://127.0.0.1:8000/api/users/. Verifique se a URL da API está correta na variável API_BASE_URL no arquivo views.py do frontend.
- Certifique-se de ter as permissões corretas para os endpoints da API, dependendo dos requisitos de autenticação da sua aplicação.
- É importante ressaltar que este README fornece apenas uma visão geral do projeto e detalhes específicos podem ser encontrados nos respectivos arquivos de código.

## License

[MIT](https://choosealicense.com/licenses/mit/)
