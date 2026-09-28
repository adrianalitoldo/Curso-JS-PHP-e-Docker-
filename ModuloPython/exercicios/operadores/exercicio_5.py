from flask import Blueprint, request, jsonify

exercicio_operadores_5_bp = Blueprint("exercicio_operadores_5", __name__)


def dividir_conta(valor_total, numero_de_pessoas):
    valor_por_pessoa = valor_total / numero_de_pessoas

    return valor_por_pessoa


@exercicio_operadores_5_bp.post("/dividir_conta")
def calcular_divisao_conta():
    try:
        dados = request.get_json()

        valor_total = float(dados.get("valor_total"))
        numero_de_pessoas = int(dados.get("numero_de_pessoas"))

        valor_por_pessoa = dividir_conta(
            valor_total, numero_de_pessoas
        )

        return jsonify({"valor_por_pessoa": valor_por_pessoa})

    except Exception as erro:
        return jsonify({
            "mensagem": f"Erro: {erro}",
            "status": "erro"
        }), 400