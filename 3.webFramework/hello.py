from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/saudacao/<username>')
def profile(username):
    return jsonify({"mensagem":f"Seja bem-vinda ao Hospital Albert Einstein, {username}!!!"})

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    num1 = dados['num1']
    num2 = dados['num2']
    return {'soma': num1 + num2}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)