# Flask API com Boas Práticas de Segurança e Docker

## Sobre o Projeto
Este repositório contém as respostas para o teste teste para vaga de desenvolvedor python Jr. bem como uma API desenvolvida com Flask, que inclui boas práticas de segurança e está preparada para ser executada em um ambiente Docker. O projeto inclui:
- Uma rota de saudação
- Um sistema de login com armazenamento seguro de senhas usando hash
- Dockerização da aplicação para facilitar a execução e o deploy

## Tecnologias Utilizadas
- Python 3.9
- Flask
- Hashlib para hashing de senhas
- Docker

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/TiaErikaDev/desafio-Einstein.git
cd desafio-Einstein
```

### 2. Criar e Ativar um Ambiente Virtual (Opcional)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar a API Localmente
```bash
python hello.py
```
A API estará acessível em `http://localhost:5000`.

## Endpoints da API

### 1. Saudação
**Rota:** `GET /saudacao/<nome>`

**Exemplo de Requisição:**
```bash
curl http://localhost:5000/saudacao/Erika
```

### 2. Login Seguro

## Melhorando a Segurança
A API implementa hashing de senhas para evitar armazenamento inseguro. O código a seguir demonstra o uso de `hashlib` para proteger senhas:
```python
import hashlib

users = {
    'admin': '81dc9bdb52d04dc20036dbd8313ed055'  # Hash da senha '1234'
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    password_hash = hashlib.md5(password.encode()).hexdigest()

    if username in users and users[username] == password_hash:
        return "Acesso concedido"
    return "Acesso negado"
```

## Rodando a API com Docker

### 1. Construir a Imagem Docker
```bash
docker build -t flask-api .
```

### 2. Executar o Container
```bash
docker run -p 5000:5000 flask-api
```

Agora, a API estará acessível em `http://localhost:5000`.

## Contribuição
Fique à vontade para abrir issues e pull requests para sugerir melhorias!


