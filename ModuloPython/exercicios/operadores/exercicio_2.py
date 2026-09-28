from flask import Blueprint, request, jsonify

exercicio_operadores_2_bp = Blueprint("exercicio_operadores_2", __name__)


def converter_celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    
    return fahrenheit


@exercicio_operadores_2_bp.post("/converter_temperatura")
def converter_temperatura():
    try:
        dados = request.get_json()

        celsius = float(dados.get("celsius"))

        fahrenheit = converter_celsius_para_fahrenheit(celsius)

        return jsonify({"fahrenheit": fahrenheit})

    except Exception as erro:
        return jsonify({"mensagem": f"Erro: {erro}","status": "erro"}), 400