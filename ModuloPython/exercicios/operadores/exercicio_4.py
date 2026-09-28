from flask import Blueprint, request, jsonify

exercicio_operadores_4_bp = Blueprint("exercicio_operadores_4", __name__)


def calcular_media_estoque(quantidade_minima, quantidade_maxima):
    quantidade_media = (quantidade_minima + quantidade_maxima) / 2

    return quantidade_media


@exercicio_operadores_4_bp.post("/calculo_estoque")
def calculo_estoque():
    try:
        dados = request.get_json()

        quantidade_minima = float(dados.get("quantidade_minima"))
        quantidade_maxima = float(dados.get("quantidade_maxima"))

        quantidade_media = calcular_media_estoque(
            quantidade_minima, quantidade_maxima
        )

        return jsonify({"quantidade_media": quantidade_media})

    except Exception as erro:
        return jsonify({
            "mensagem": f"Erro: {erro}",
            "status": "erro"
        }), 400