from flask import Blueprint, request, jsonify
import os
arquivos_bp = Blueprint('arquivos', __name__)

DIRETORIO_ARQUIVOS = "arquivos/gerados" 


def verificar_arquivo(caminho_completo):
    return bool(os.path.exists(caminho_completo))


@arquivos_bp.put('/alterar_arquivo')
def alterar_arquivo():
    try:
        dados = request.get_json()
        nome_arquivo = dados.get('nome').strip()
        novo_conteudo = dados.get('conteudo').strip()
        
        if nome_arquivo == "" or novo_conteudo == "":
            return jsonify({"status": "erro", "mensagem": f"Erro ao alterar arquivo: {str(e)}"}), 500
                
        caminho_completo = os.path.join(DIRETORIO_ARQUIVOS, nome_arquivo)
        
        #se arquivo existe 
        if not verificar_arquivo(caminho_completo):
            return jsonify({"status": "erro", "mensagem": f"Arquivo'{nome_arquivo}' não encontrado."}), 500
        
        
        with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(novo_conteudo)
        return jsonify({"status": "erro", "mensagem": f"conteúdo do arquivo '{nome_arquivo}' alterado com sucesso"}), 500
                        
    except Exception as e:
            return jsonify({"status": "erro", "mensagem": f"Erro ao criar arquivo: {str(e)}"}), 500
        
        
@arquivos_bp.delete("/excluir_arquivos")
def excluir():  # sourcery skip: remove-redundant-fstring
    try: 
        dados = request.get_json()
        nome_arquivo = dados.get("nome").strip()
        
        if nome_arquivo == "":
            return jsonify({"status": "erro", "mensagem": f"Nome do arquivo é obrigatório para exclusão."}), 400
        
        caminho_completo = os.path.join(DIRETORIO_ARQUIVOS, nome_arquivo)
        
        if not verificar_arquivo(caminho_completo):
            return jsonify({"status": "erro", "mensagem": f"Não foi encontrado arquivo para ser excluído"}), 400
        
        os.remove(caminho_completo)
        
        return jsonify({"status": "erro", "mensagem": f"Arquivo: '{nome_arquivo}', excluído com sucesso "}), 200

    except Exception as e:
        return jsonify({"status": "erro", "mensagem": f"Erro ao criar arquivo: {str(e)}"}), 500



@arquivos_bp.get('/listar_arquivos')
def listar_arquivos():
    arquivos = os.listdir(DIRETORIO_ARQUIVOS)
    lista_arquivos = []
    for item_arquivo in arquivos:
        caminho_completo = os.path.join(DIRETORIO_ARQUIVOS, item_arquivo)
        conteudo  = ""
        with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        
        
        lista_arquivos.append({
            "nome": item_arquivo,
            "conteudo": conteudo
        })

    return jsonify({"status": "sucesso", "arquivos": lista_arquivos}), 200


@arquivos_bp.post('/criar_arquivo')
def criar_arquivo():
    try:
        #pegar informações do arquivo
        dados = request.get_json()
        
        #pegando nome do arquivo e conteúdo
        nome_arquivo = dados.get('nome').strip()
        conteudo = dados.get('conteudo').strip()
        
        if nome_arquivo == "" or conteudo == "":
            return jsonify({"status": "erro", "mensagem": "Informar o erro e o nome do arquivo"}), 400
        
        if not os.path.exists(DIRETORIO_ARQUIVOS):
            os.makedirs(DIRETORIO_ARQUIVOS) 
                    
        caminho_completo = os.path.join(DIRETORIO_ARQUIVOS, nome_arquivo)
        
        
        if verificar_arquivo(caminho_completo):
            return jsonify({"status": "erro", "mensagem": f"O arquivo '{nome_arquivo}' já existe"}), 400
        
        #escrever o conteúdo dentro do arquivo            
        with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
            
        return jsonify({"status": "sucesso", "mensagem": f"Arquivo '{nome_arquivo}' Nome do arquivo foi criado com sucesso"}), 201


    except Exception as e:
        return jsonify({"status": "erro", "mensagem": f"Erro ao criar arquivo: {str(e)}"}), 500
    