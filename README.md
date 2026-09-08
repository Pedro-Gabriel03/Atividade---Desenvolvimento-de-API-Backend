# 📚 StudyManager API

API RESTful desenvolvida em **Python** utilizando **FastAPI** e **SQLAlchemy**, criada para o gerenciamento de usuários, cursos e matrículas.

O projeto aplica conceitos de **Arquitetura Limpa**, **Clean Code**, **ORM**, validação de dados e tratamento padronizado de erros.

Link para o GITHUB: https://github.com/Pedro-Gabriel03/Atividade---Desenvolvimento-de-API-Backend
---

## 🎯 Objetivo

A StudyManager API tem como objetivo disponibilizar uma API para gerenciamento de:

* 👤 Usuários
* 📘 Cursos
* 📝 Matrículas

A aplicação permite:

* Cadastrar usuários
* Consultar usuários
* Atualizar usuários
* Excluir usuários
* Cadastrar cursos
* Consultar cursos
* Atualizar cursos
* Excluir cursos
* Matricular usuários em cursos
* Consultar os cursos de um usuário

---

## 🛠️ Tecnologias utilizadas

* Python 3
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn
* SQLite

---

## 🏗️ Arquitetura do projeto

O projeto foi organizado seguindo uma separação de responsabilidades baseada em princípios de **Arquitetura Limpa**.

```text
studymanager-api/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── database.py
│   │   └── exceptions.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── course.py
│   │   └── enrollment.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── course.py
│   │   └── enrollment.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── course_repository.py
│   │   └── enrollment_repository.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── course_service.py
│   │   └── enrollment_service.py
│   │
│   └── routes/
│       ├── user_routes.py
│       ├── course_routes.py
│       └── enrollment_routes.py
│
├── requirements.txt
├── README.md
└── studymanager.db
```

### Responsabilidade das camadas

**Routes:** responsáveis por receber as requisições HTTP e encaminhá-las para os serviços.

**Services:** concentram as regras de negócio da aplicação.

**Repositories:** responsáveis pelo acesso e manipulação dos dados através do SQLAlchemy.

**Models:** representam as entidades do banco de dados.

**Schemas:** definem e validam os dados de entrada e saída da API.

**Core:** contém recursos compartilhados da aplicação, como conexão com o banco e tratamento de exceções.

Essa separação evita que regras de negócio sejam colocadas diretamente nos controllers/routes, facilitando manutenção, testes e evolução do sistema.

---

## 🗄️ Modelagem do banco

A aplicação possui três entidades principais.

### 👤 User

| Campo      | Tipo     | Descrição           |
| ---------- | -------- | ------------------- |
| id         | Integer  | Identificador único |
| name       | String   | Nome do usuário     |
| email      | String   | E-mail único        |
| created_at | DateTime | Data de criação     |

### 📘 Course

| Campo       | Tipo    | Descrição              |
| ----------- | ------- | ---------------------- |
| id          | Integer | Identificador único    |
| title       | String  | Nome do curso          |
| description | Text    | Descrição do curso     |
| workload    | Integer | Carga horária em horas |

### 📝 Enrollment

| Campo       | Tipo     | Descrição           |
| ----------- | -------- | ------------------- |
| id          | Integer  | Identificador único |
| user_id     | Integer  | ID do usuário       |
| course_id   | Integer  | ID do curso         |
| enrolled_at | DateTime | Data da matrícula   |

### Relacionamentos

```text
User 1 -------- N Enrollment N -------- 1 Course
```

Um usuário pode possuir várias matrículas.

Um curso pode possuir várias matrículas.

Cada matrícula pertence a um usuário e a um curso.

Também existe uma restrição que impede que um usuário seja matriculado duas vezes no mesmo curso.

---

# 🚀 Instalação

## 1. Clonar ou acessar o projeto

Abra o terminal na pasta do projeto:

```bash
cd Atividade---Desenvolvimento-de-API-Backend-main
```

---

## 2. Criar ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

---

## 3. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a execução:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 4. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` ainda não tenha todas as dependências:

```powershell
python -m pip install fastapi uvicorn sqlalchemy pydantic email-validator
```

---

# ▶️ Executando a API

Com o ambiente virtual ativado:

```powershell
python -m uvicorn app.main:app --reload
```

A API será executada em:

```text
http://127.0.0.1:8000
```

---

# 📖 Documentação

O FastAPI gera automaticamente uma documentação interativa.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

O Swagger pode ser utilizado para testar todos os endpoints sem a necessidade de ferramentas externas.

---

# 🔌 Endpoints

## 👤 Usuários

### Criar usuário

```http
POST /users
```

Exemplo:

```json
{
  "name": "Pedro",
  "email": "pedro@email.com"
}
```

### Listar usuários

```http
GET /users
```

### Buscar usuário

```http
GET /users/{user_id}
```

Exemplo:

```text
GET /users/1
```

### Atualizar usuário

```http
PUT /users/{user_id}
```

Exemplo:

```json
{
  "name": "Pedro Silva",
  "email": "pedro.silva@email.com"
}
```

### Excluir usuário

```http
DELETE /users/{user_id}
```

---

# 📘 Cursos

### Criar curso

```http
POST /courses
```

Exemplo:

```json
{
  "title": "Python Básico",
  "description": "Curso de introdução à programação com Python",
  "workload": 40
}
```

### Listar cursos

```http
GET /courses
```

### Buscar curso

```http
GET /courses/{course_id}
```

### Atualizar curso

```http
PUT /courses/{course_id}
```

Exemplo:

```json
{
  "title": "Python Intermediário",
  "description": "Curso de programação Python em nível intermediário",
  "workload": 60
}
```

### Excluir curso

```http
DELETE /courses/{course_id}
```

---

# 📝 Matrículas

### Criar matrícula

```http
POST /enrollments
```

Exemplo:

```json
{
  "user_id": 1,
  "course_id": 1
}
```

A API verifica:

* Se o usuário existe
* Se o curso existe
* Se o usuário já está matriculado no curso

Não é permitida matrícula duplicada.

---

# 🔎 Consulta relacional

### Consultar cursos de um usuário

```http
GET /users/{user_id}/courses
```

Exemplo:

```text
GET /users/1/courses
```

Resposta esperada:

```json
{
  "success": true,
  "message": "User courses retrieved successfully",
  "data": {
    "user": {
      "id": 1,
      "name": "Pedro",
      "email": "pedro@email.com"
    },
    "courses": [
      {
        "id": 1,
        "title": "Python Básico",
        "description": "Curso de introdução à programação com Python",
        "workload": 40
      }
    ]
  }
}
```

Essa consulta utiliza os relacionamentos definidos no SQLAlchemy para recuperar os cursos relacionados ao usuário.

---

# ✅ Validações

A API utiliza **Pydantic** para validar os dados recebidos.

Exemplos de validação:

* Nome com tamanho mínimo
* E-mail em formato válido
* E-mail único
* Título do curso obrigatório
* Descrição obrigatória
* Carga horária maior que zero
* IDs de usuário e curso válidos

---

# ⚠️ Tratamento de erros

A API utiliza códigos HTTP apropriados e mensagens padronizadas.

### Usuário não encontrado

```http
404 Not Found
```

```json
{
  "success": false,
  "message": "User not found",
  "data": null
}
```

### Curso não encontrado

```http
404 Not Found
```

```json
{
  "success": false,
  "message": "Course not found",
  "data": null
}
```

### E-mail já cadastrado

```http
409 Conflict
```

```json
{
  "success": false,
  "message": "Email already registered",
  "data": null
}
```

### Matrícula duplicada

```http
409 Conflict
```

```json
{
  "success": false,
  "message": "User is already enrolled in this course",
  "data": null
}
```

### Dados inválidos

```http
422 Unprocessable Entity
```

```json
{
  "success": false,
  "message": "Validation error",
  "data": [...]
}
```

---

# 🧪 Fluxo básico de utilização

Para testar o sistema, recomenda-se seguir esta ordem:

```text
1. Criar usuário
       ↓
2. Criar curso
       ↓
3. Criar matrícula
       ↓
4. Consultar cursos do usuário
```

### Exemplo

Criar usuário:

```json
{
  "name": "Pedro",
  "email": "pedro@email.com"
}
```

Resultado:

```text
ID = 1
```

Criar curso:

```json
{
  "title": "Python Básico",
  "description": "Curso de introdução à programação com Python",
  "workload": 40
}
```

Resultado:

```text
ID = 1
```

Criar matrícula:

```json
{
  "user_id": 1,
  "course_id": 1
}
```

Consultar:

```text
GET /users/1/courses
```

---

# 🧹 Clean Code

O projeto procura seguir princípios de Clean Code, como:

* Nomes claros e significativos
* Métodos pequenos
* Separação de responsabilidades
* Baixo acoplamento entre camadas
* Regras de negócio concentradas nos services
* Acesso ao banco concentrado nos repositories
* Validação através dos schemas
* Tratamento centralizado de erros

A estrutura permite que cada parte da aplicação tenha uma responsabilidade bem definida.

---

# 📂 Banco de dados

O projeto utiliza **SQLite** para simplificar a execução.

Ao iniciar a aplicação, o banco é criado automaticamente:

```text
studymanager.db
```

Não é necessário instalar ou configurar um servidor de banco de dados externo para executar o projeto.

---

# 🔐 Regras de negócio

A aplicação possui as seguintes regras:

### Usuários

* O nome é obrigatório.
* O e-mail é obrigatório.
* O e-mail precisa possuir formato válido.
* Não é permitido cadastrar dois usuários com o mesmo e-mail.

### Cursos

* O título é obrigatório.
* A descrição é obrigatória.
* A carga horária deve ser maior que zero.

### Matrículas

* O usuário precisa existir.
* O curso precisa existir.
* Um usuário não pode possuir duas matrículas no mesmo curso.

---

# 📌 Requisitos atendidos

| Requisito                     | Implementação |
| ----------------------------- | ------------- |
| API RESTful                   | ✅             |
| FastAPI                       | ✅             |
| SQLAlchemy                    | ✅             |
| ORM                           | ✅             |
| Arquitetura em camadas        | ✅             |
| Clean Code                    | ✅             |
| CRUD de usuários              | ✅             |
| CRUD de cursos                | ✅             |
| Matrículas                    | ✅             |
| Validação                     | ✅             |
| E-mail único                  | ✅             |
| Matrícula duplicada bloqueada | ✅             |
| Consulta relacional           | ✅             |
| Tratamento de erros           | ✅             |
| HTTP Status Codes             | ✅             |
| Documentação Swagger          | ✅             |

---

