from flask import Blueprint, request, jsonify

exercicio_laco_2_bp = Blueprint("exercicio_laco_2", __name__)

@exercicio_laco_2_bp.post("/calcular_media_anual")
def calcular_media_anual():
    try:
        dados = request.get_json()

        salarios_anuais = dados.get("salarios_anuais")

        soma_salarios = 0
        contador = 0

        while contador < 12:
            soma_salarios += salarios_anuais[contador]
            contador += 1

        media_salarial_anual = soma_salarios / 12

        return jsonify({
            "status": "sucesso",
            "media_salarial_anual": f"{media_salarial_anual:.2f}"
        })

    except Exception as erro:
        return jsonify({
            "mensagem": f"Erro: {erro}",
            "status": "erro"
        }), 400