from flask import Blueprint, request, jsonify

exercicio_colecoes_2_bp = Blueprint("exercicio_colecoes_2", __name__)

@exercicio_colecoes_2_bp.post("/analisar_ganhos")
def analisar_ganhos():
    try:
        dados = request.get_json()

        nome_cliente = dados.get("nome_cliente")
        ganhos_ultimos_3_meses = dados.get("ganhos_ultimos_3_meses")

        classificacao_ganhos = (
            "Aumento Ruim",
            "Aumento Bom",
            "Aumento Excelente"
        )

        media_ganhos = sum(ganhos_ultimos_3_meses) / len(ganhos_ultimos_3_meses)

        if media_ganhos < 1000:
            classificacao = classificacao_ganhos[0]

        elif media_ganhos <= 5000:
            classificacao = classificacao_ganhos[1]

        else:
            classificacao = classificacao_ganhos[2]

        return jsonify({
            "nome_cliente": nome_cliente,
            "media_ganhos": media_ganhos,
            "classificacao": classificacao
        })

    except Exception as erro:
        return jsonify({
            "mensagem": f"Erro: {erro}",
            "status": "erro"
        }), 400