from flask import Blueprint, request, jsonify

exercicio_colecoes_1_bp = Blueprint("exercicio_colecoes_1", __name__)

estoque = {
    "mouse": 5,
    "teclado": 34,
    "monitor": 21
}

@exercicio_colecoes_1_bp.post("/verificar_estoque")
def verificar_estoque():
    try:
        dados = request.get_json()

        produto = dados.get("produto")
        quantidade = int(dados.get("quantidade"))

        quantidade_atual = estoque.get(produto, 0)

        tem_estoque = produto in estoque and quantidade <= quantidade_atual

        return jsonify({
            "produto": produto,
            "tem_estoque": tem_estoque,
            "quantidade_atual": quantidade_atual
        })

    except Exception as erro:
        return jsonify({"mensagem": f"Erro: {erro}", "status": "erro" }), 400