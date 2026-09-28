from flask import Blueprint, request, jsonify

exercicio_5_bp = Blueprint("exercicio_5", __name__)


@exercicio_5_bp.post("/consumo-combustivel")
def consumo_combustivel():
    try:
        dados = request.get_json()

        distancia = float(dados.get("distancia"))
        litros = float(dados.get("litros"))

        consumo = distancia / litros

        return jsonify({"consumo_medio": consumo})

    except Exception as erro:
        return jsonify({"mensagem": f"Erro: {erro}", "status": "erro"}), 400