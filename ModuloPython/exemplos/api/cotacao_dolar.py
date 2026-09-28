from flask import Blueprint, request, jsonify
import requests


api_bp = Blueprint("api", __name__)

#chamando api externa
API_URL = "http://economia.awesomeapi.com.br/json/last/USD-BRL"


@api_bp.get("/cotacao_dolar")
def cotacao_dolar():
    try:
        resposta = requests.get(API_URL)
        
        if resposta.status_code != 200:
            return jsonify({
                "status": "erro",
                "mensagem": f"Erro ao chamar API. Status: {resposta.status_code}"
            }), resposta.status_code      
            
        
        dados_cotacao = resposta.json()
        valor = f"{float(dados_cotacao['USDBRL']['bid']):.2f}"
        moeda = dados_cotacao['USDBRL']['name']
        
        return jsonify({
            "status": "sucesso",
            "moeda" : "moeda",
            "valor_real" : valor
            })
                
        
        

    except Exception as e:
                return jsonify({"status": "erro", "mensagem": f"Erro geral {str(e)}"}), 500