import hashlib
from flask import Flask, request
app = Flask(__name__)

USERS_DB = {"admin": hashlib.sha256("1234".encode()).hexdigest()}
 
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return "Usuário ou senha inválidos"
    
    stored_password = USERS_DB.get(username)
    if stored_password and stored_password == hashlib.sha256(password.encode()).hexdigest():
        return "Acesso concedido"
    else:
	    return "Acesso negado"
 
if __name__ == '__main__':
    app.run()


# O código verifica o usuário e senha diretamente no código-fonte, o que é extremamente
# inseguro. O ideal é que essas informações estejam em um banco de dados. Outro ponto, 
# é que as senhas nunca devem ser armazenadas ou comparadas em texto. Devem ser armazenadas
# de forma segura com hashing.
# O uso de debug=True é uma prática insegura, pois pode expor informações sensíveis.