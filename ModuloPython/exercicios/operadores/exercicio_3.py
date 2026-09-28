from flask import Blueprint, request, jsonify

exercicio_operadores_3_bp = Blueprint("exercicio_operadores_3", __name__)


def calcular_juros_simples(capital, taxa, tempo):
    juros = capital * taxa * tempo

    return juros


@exercicio_operadores_3_bp.post("/calcular_juros_simples")
def calcular_juros():
    try:
        dados = request.get_json()

        capital = float(dados.get("capital"))
        taxa = float(dados.get("taxa"))
        tempo = float(dados.get("tempo"))

        juros = calcular_juros_simples(capital, taxa, tempo)

        return jsonify({"juros": juros})

    except Exception as erro:
        return jsonify({
            "mensagem": f"Erro: {erro}",
            "status": "erro"
        }), 400