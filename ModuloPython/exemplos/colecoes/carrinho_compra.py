from flask import request, jsonify, Blueprint

carrinho_compra_bp = Blueprint('carrinho_compra', __name__)

preco_produtos = {
    "maça" : 2.00,
    "uva" : 3.50
}

@carrinho_compra_bp.post('/processar_pedido')
def processar_pedido():
    try:
        #pegar informações dos pedidos
        dados_pedido = request.get_json()
        
        #pegando nome do cliente
        nome_cliente = dados_pedido.get('cliente')
        carrinhos = dados_pedido.get('carrinho')
        
        
        if nome_cliente == "":
            return jsonify({"Resultado": "Nome do cliente é obrigatório"}), 400
        
        if not isinstance(carrinhos, list):
            return jsonify({"Resultado": "Carrinho está no formato incorreto"}), 400        

        if not carrinhos:
            return jsonify({"Resultado": "Carrinho de compras está vazio"}), 400
        
        valor_total = 0
        for item in carrinhos:
            if not isinstance(item, dict):
                return jsonify({"Resultado": "Item incorreto"}), 400
            
            produto = item.get('produto')
            quantidade = item.get('quantidade')
            
            if produto == "" or not isinstance(produto, str):
                return jsonify({"Resultado": "Nome do produto é obrigatório"}), 400
            
            if not isinstance(quantidade, int) or quantidade <= 0:
                return jsonify({"Resultado": "Quantidade inválida"}), 400
            
            if produto  not in preco_produtos:
                return jsonify({"Resultado": f"Produto '{produto}' não encontrado"}), 400
            
            preco_unitario = preco_produtos[produto]
            valor_item = preco_unitario * quantidade
            valor_total += valor_item
            
            #resposta final
            status = ("Pedido processado com sucesso", 200)
            
            resposta = {
                "cliente": nome_cliente,
                "valor_total": valor_total,
                "status": status[0],
                "status_codigo": status[1]
            }
            
            return jsonify(resposta), 200
            
    except Exception as e:
        return jsonify({"Resultado": "Ocorreu um erro ao processar o pedido"}), 500
    