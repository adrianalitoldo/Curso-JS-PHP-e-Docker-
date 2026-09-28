from flask import Blueprint, request, jsonify

exercicio_laco_1_bp = Blueprint("exercicio_laco_1", __name__)

@exercicio_laco_1_bp.post("/calculo_semestre")
def calculo_semestre():
    try:
        dados = request.get_json()

        ganhos_semestre = dados.get("ganhos_semestre")

        total_ganho_semestral = sum(ganhos_semestre)
        return jsonify({
            "status": "sucesso",
            "total_ganho_semestral": f"{total_ganho_semestral:.2f}"
        })

    except Exception as erro:
        return jsonify({"mensagem": f"Erro: {erro}", "status": "erro"}), 400