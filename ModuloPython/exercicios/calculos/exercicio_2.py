from flask import Blueprint, request, jsonify

exercicio_2_bp = Blueprint("exercicio_2", __name__)


@exercicio_2_bp.post("/calculo-area-retangulo")
def calculo_area_retangulo():
    try:
        dados = request.get_json()

        largura = float(dados.get("largura"))
        altura = float(dados.get("altura"))

        area = largura * altura

        return jsonify({"Área do retângulo: ": area})

    except Exception as erro:
        return jsonify({"mensagem": f"Erro: {erro}", "status": "erro"}), 400