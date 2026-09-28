from flask import Blueprint, request, jsonify

exercicio_3_bp = Blueprint("exercicio_3", __name__)


@exercicio_3_bp.post("/calculo-media")
def calculo_media():
    try:
        dados = request.get_json()

        nota1 = float(dados.get("nota1"))
        nota2 = float(dados.get("nota2"))
        nota3 = float(dados.get("nota3"))

        media = (nota1 + nota2 + nota3) / 3

        return jsonify({"media": media})

    except Exception as erro:
        return jsonify({
            "mensagem": f"Erro: {erro}", "status": "erro"}), 400