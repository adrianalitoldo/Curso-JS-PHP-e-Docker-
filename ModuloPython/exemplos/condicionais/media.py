from flask import request, jsonify, Blueprint

media_bp = Blueprint('media', __name__)

def obter_media(nota1, nota2, nota3, nota4):
    raise NotImplementedError

def obter_classificacao():
    raise NotImplementedError

@media_bp.post("/calculo_media")
def calcular_media():
    try:
        dados = request.get_json()
        nome = dados.get("nome").strip()
        
        nota1 = float(dados.get("nt1"))
        nota2 = float(dados.get("nt2"))
        nota3 = float(dados.get("nt3"))
        nota4 = float(dados.get("nt4"))
        
        if nome == "":
            return jsonify({"Resultado": "Informe o nome do aluno."}), 400
        
        if nota1 < 0 or nota1 > 100:
            return jsonify({"Resultado": "A Nota 1 deverá ser entre 0 - 100."}), 400
        
        if nota2 < 0 or nota2 > 100:
            return jsonify({"Resultado": "A Nota 2 deverá ser entre 0 - 100."}), 400
        
        if nota3 < 0 or nota3 > 100:
            return jsonify({"Resultado": "A Nota 3 deverá ser entre 0 - 100."}), 400

        if nota4 < 0 or nota4 > 100:
            return jsonify({"Resultado": "A Nota 4 deverá ser entre 0 - 100."}), 400

        #media = (nota1 + nota2 + nota3 + nota4) / 4
        media = obter_media(nota1, nota2, nota3, nota4)
        classificacao = obter_classificacao(media)
        
        
        return jsonify({
            "Nome": nome,
            "Média": media,
            "Classificação": classificacao
        })
        
    except ValueError:
        return jsonify({"Resultado": "As notas deverão ser numéricas."}), 400
    except Exception as e:
        return jsonify({"Resultado": f"Ocorreu um erro: {str(e)}"}), 500
    
    
def obter_media(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

def obter_classificacao(media):
            
    # Se a média está entre 0 - 39
    if media <= 40:
        return "Reprovado"
    elif media < 60:
        return "Exame"
    else:
        return "Aprovado"
