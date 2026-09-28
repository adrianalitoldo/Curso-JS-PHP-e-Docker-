from flask import Blueprint, request, jsonify

exercicio_colecoes_3_bp = Blueprint("exercicio_colecoes_3", __name__)

usuarios = {
    "admin": "12345",
    "joao": "senha123"
}

@exercicio_colecoes_3_bp.post("/login")
def login():
    try:
        dados = request.get_json()

        usuario = dados.get("usuario")
        senha = dados.get("senha")

        status = ("sucesso", "falha")
        mensagens = (
            "Login efetuado com sucesso",
            "Login não realizado"
        )

        if usuario in usuarios and usuarios[usuario] == senha:
            return jsonify({
                "status": status[0],
                "mensagem": mensagens[0]
            })

        return jsonify({
            "status": status[1],
            "mensagem": mensagens[1]
        })

    except Exception as erro:
        return jsonify({
            "mensagem": f"Erro: {erro}",
            "status": "erro"
        }), 400