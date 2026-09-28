from flask import request, jsonify, Blueprint

laco_repeticao_bp = Blueprint('laco_repeticao', __name__)

@laco_repeticao_bp.post("/somar_for")
def somar_for():
    try:
        dados = request.get_json()
        precos = dados.get("precos")

        total = sum(precos)
        return jsonify({"Total dos valores com for": f"{total:.2f}"})

    except Exception as e:
        return jsonify({"Resultado": f"Ocorreu um erro: {str(e)}"}), 500
    
@laco_repeticao_bp.post("/somar_while")
def somar_while():
    try:
        dados = request.get_json()
        precos = dados.get("precos")
        total = sum(precos[contador] for contador in range(len(precos)))
        return jsonify({"Total dos valores com while": f"{total:.2f}"})

    except Exception as e:
        return jsonify({"Resultado": f"Ocorreu um erro: {str(e)}"}), 500
    
    