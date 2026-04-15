from flask import Flask, request, jsonify, render_template
from banco import conectar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar', methods=['POST'])
def adicionar_transacao():
    tipo = request.json.get('tipo')
    valor = request.json.get('valor')
    categoria = request.json.get('categoria')
    data = request.json.get('data')
    descricao = request.json.get('descricao')

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO transacoes (tipo, valor, categoria, data, descricao) VALUES (?, ?, ?, ?, ?)",
               (tipo, valor, categoria, data, descricao))
    conexao.commit()
    conexao.close()

    return jsonify({"mensagem": "Transação salva!"})

@app.route('/listar', methods=['GET'])
def listar_transacoes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM transacoes")
    transacoes = cursor.fetchall()
    conexao.close()

    return jsonify(transacoes)

@app.route('/deletar/<id>', methods=['DELETE'])
def deletar_transacao(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM transacoes WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

    return jsonify({"mensagem": "Essa transação foi excluida!"})

@app.route('/limites', methods=['POST'])
def limites_transacoes():
    categoria = request.json.get('categoria')
    valor_max = request.json.get('valor_max')
    mes = request.json.get('mes')

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('INSERT INTO limites (categoria, valor_max, mes) VALUES (?, ?, ?)', (categoria, valor_max, mes))
    conexao.commit()
    conexao.close()

    return jsonify({"mensagem": "Limites salvos!"})

@app.route('/mostrarlimites', methods=['GET'])
def listar_limites():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM limites')
    lista_limites = cursor.fetchall()
    conexao.close()
     
    return jsonify(lista_limites)
if __name__ == '__main__':
    app.run(debug=True)