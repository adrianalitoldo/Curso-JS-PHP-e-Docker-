from flask import Blueprint, request, jsonify

exercicio_4_bp = Blueprint("exercicio_4", __name__)


@exercicio_4_bp.post("/calculo-troco")
def calculo_troco():
    try:
        dados = request.get_json()

        valor_total = float(dados.get("valor_total"))
        valor_pago = float(dados.get("valor_pago"))

        troco = valor_pago - valor_total

        return jsonify({"troco": troco})

    except Exception as erro:
        return jsonify({"mensagem": f"Erro: {erro}", "status": "erro"}), 400