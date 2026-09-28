from flask import Blueprint, Flask, jsonify, request

calculadora_bp = Blueprint ('calculadora', __name__)

@calculadora_bp.post("/soma")
def somar():
    # Pegar os dados no formato de JSON
    dados = request.get_json()
    
    num1 = dados.get("num1")
    num2 = dados.get("num2")

    resultado = num1 + num2

    return jsonify(resultado)


@calculadora_bp.post("/subtracao")
def subtrair():
    # Pegar os dados no formato de JSON
    dados = request.get_json()
    
    num1 = dados.get("num1")
    num2 = dados.get("num2")

    resultado = num1 - num2

    return jsonify(resultado=num1-num2)


@calculadora_bp.post("/divisao")
def dividir():
    # Pegar os dados no formato de JSON
    dados = request.get_json()
    
    num1 = dados.get("num1")
    num2 = dados.get("num2")

    resultado = num1 / num2

    return jsonify(resultado=num1/num2)


@calculadora_bp.post("/multiplicacao")
def multiplicar():
    # Pegar os dados no formato de JSON
    dados = request.get_json()
    
    num1 = dados.get("num1")
    num2 = dados.get("num2")

    resultado = num1 * num2

    return jsonify(resultado=num1*num2)