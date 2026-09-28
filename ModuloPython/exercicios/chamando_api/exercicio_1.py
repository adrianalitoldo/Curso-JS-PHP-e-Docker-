from flask import Blueprint, request, jsonify
import requests


api_exercicio_1_bp = Blueprint("api_exercicio_1", __name__)


@api_exercicio_1_bp.get("/buscar_cep")
def buscar_cep():
    try:
        #Pegando o cep enviado na requisição
        cep = request.args.get("cep")

        #Verificando se o cep foi informado
        if not cep:
            return jsonify({
                "mensagem": "Informe o CEP"
            }), 400

        #remoção dos caracteres que não são números
        cep = cep.replace("-", "").replace(".", "").strip()


        #verfificando se o cep possui 8 numeros
        if not cep.isdigit() or len(cep) !=8:
            return jsonify({"status": "erro", "mensagem": "CEP inválido! Informe um CEP coom 8 números!"}), 400
        
        API_URL = f"https://viacep.com.br/ws/{cep}/json/"
        
        #fazendo a requisição da API externa
        resposta = requests.get(API_URL)
        
        if resposta.status_code != 200:
            return jsonify({
                "status": "erro", "mensagem": "Erro ao consultar API de CEP"}), 500
            
        dados_cep = resposta.json()

        #verificar se cep foi encontrado
        if dados_cep.get("erro"):
            return jsonify({
                "status": "erro", 
                "mensagem": f"Não foi encontrado nenhum endereço com o CEP {cep} informado"
            }), 404
            
        #Retornando os dados encontrados
        return jsonify({
            "status": "sucesso",
            "cep": dados_cep.get("cep"),
            "logradouro": dados_cep.get("logradouro"),
            "bairro": dados_cep.get("bairro"),
            "cidade": dados_cep.get("localidade"),
            "estado": dados_cep.get("uf")
            }), 200
            

    except Exception as erro:
        return jsonify({
            "mensagem": f"Erro ao consultar o CEP: {str(erro)}"
        }), 500