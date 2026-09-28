from flask import Blueprint, request, jsonify

exercicio_1_bp = Blueprint("exercicio_1", __name__)


@exercicio_1_bp.post("/calculo-salario")
def calculo_salario():
    try:
        dados = request.get_json()

        salario = float(dados.get("salario"))
        desconto = float(dados.get("desconto"))

        salario_final = salario - desconto

        return jsonify({"salario_final": salario_final})

    except Exception as erro:
        return jsonify({
            "mensagem": f"Erro: {erro}", "status": "erro"}), 400