from flask import request, jsonify, Blueprint

calculadora_2_bp = Blueprint('calculadora_2', __name__)

@calculadora_2_bp.post("/calculadora_resposta")
def calculadora_2():
    try:
        dados = request.get_json()
        num1 = float(dados.get("num1"))
        num2 = float(dados.get("num2"))
        operador = dados.get("op")

        if operador == "+":
            res = (num1 + num2)
        elif operador == "-":
            res = (num1 - num2)
        elif operador in ['x', 'X']:
            res = (num1 * num2)
        elif operador == "/":
            if num2 == 0:
                return jsonify({"Resultado": "Não poderá ser zero na divisão."}), 400
            res = (num1 / num2)
        else:
            res = "Operador inexistente"

        return jsonify(resultado=res)
    except ValueError:
        return jsonify({"Resultado": "Revise as informações."}), 400
    except Exception as e:
        return jsonify({"Resultado": f"Ocorreu um erro geral: {str(e)}"}), 500