from flask import Blueprint, request, jsonify

exercicio_operadores_1_bp = Blueprint("exercicio_operadores_1", __name__)

def calcular_media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3):
    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

    return media


@exercicio_operadores_1_bp.post("/calculo_media_ponderada")
def calculo_media_ponderada():
    try:
        dados = request.get_json()

        nota1 = float(dados.get("nota1"))
        nota2 = float(dados.get("nota2"))
        nota3 = float(dados.get("nota3"))

        peso1 = float(dados.get("peso1"))
        peso2 = float(dados.get("peso2"))
        peso3 = float(dados.get("peso3"))

        media = calcular_media_ponderada(
            nota1, nota2, nota3, peso1, peso2, peso3
        )

        return jsonify({"media_ponderada": media})

    except Exception as erro:
        return jsonify({"mensagem": f"Erro: {erro}","status": "erro"}), 400