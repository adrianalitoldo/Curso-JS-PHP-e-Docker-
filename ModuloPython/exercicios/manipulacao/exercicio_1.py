from flask import Blueprint, request, jsonify
import os

arquivos_bp = Blueprint("arquivos_exercicio_1", __name__)

DIRETORIO_ARQUIVOS = "arquivos/arq_gerados"


# Verificação se o arquivo já existe.
def verificar_arquivo(caminho_completo):
    if not os.path.exists(caminho_completo):
        return False
    return True


# CRIAR ARQUIVO =================================================================
@arquivos_bp.post("/criar-arquivo")
def criar():
    try:

        # Pegando os dados enviados no formato JSON.
        dados = request.get_json()

        # Pegando o nome e o conteúdo do arquivo.
        nome_arquivo = dados.get("nome").strip()
        conteudo = dados.get("conteudo").strip()

        # Verificando se os campos foram preenchidos.
        if nome_arquivo == "" or conteudo == "":
            return jsonify({
                "status": "erro",
                "mensagem": "Informar o NOME e o CONTEÚDO do arquivo!"
            }), 400

        # Caso a pasta não exista, ela será criada.
        if not os.path.exists(DIRETORIO_ARQUIVOS):
            os.makedirs(DIRETORIO_ARQUIVOS)

        # Criando o caminho completo do arquivo.
        caminho_completo = os.path.join(
            DIRETORIO_ARQUIVOS,
            nome_arquivo
        )

        # Verificando se o arquivo já existe.
        if verificar_arquivo(caminho_completo):
            return jsonify({
                "status": "erro",
                "mensagem": f"O arquivo '{nome_arquivo}' já existe!"
            }), 400

        # Criando fisicamente o arquivo.
        with open(
            caminho_completo,
            "w",
            encoding="utf-8"
        ) as arquivo:
            arquivo.write(conteudo)

        return jsonify({
            "status": "sucesso",
            "mensagem": f"Arquivo '{nome_arquivo}' criado com SUCESSO!"
        }), 200

    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": f"ERRO ao criar o ARQUIVO: {str(e)}"
        }), 500


# LISTAR ARQUIVOS =================================================================
@arquivos_bp.get("/listar-arquivos")
def listar():
    try:

        # Verificando se a pasta existe.
        if not os.path.exists(DIRETORIO_ARQUIVOS):
            return jsonify({
                "status": "sucesso",
                "arquivos": []
            }), 200

        # Lista de arquivos.
        arquivos = os.listdir(DIRETORIO_ARQUIVOS)
        lista_arquivos = []

        # Percorrendo os arquivos.
        for item_arquivo in arquivos:

            caminho_completo = os.path.join(
                DIRETORIO_ARQUIVOS,
                item_arquivo
            )

            # Verificando se é realmente um arquivo.
            if os.path.isfile(caminho_completo):
                with open(
                    caminho_completo,
                    "r",
                    encoding="utf-8"
                ) as arquivo:

                    conteudo = arquivo.read()

                    lista_arquivos.append({
                        "nome": item_arquivo,
                        "conteudo": conteudo
                    })

        return jsonify({
            "status": "sucesso",
            "arquivos": lista_arquivos
        }), 200

    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": f"ERRO ao listar os ARQUIVOS: {str(e)}"
        }), 500