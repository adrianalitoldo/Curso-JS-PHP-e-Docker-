from flask import Flask, jsonify, request, send_from_directory
import importlib

#importando as blueprints criadas nos arquivos de rotas
from exemplos.calculos.calculadora import calculadora_bp
from exemplos.condicionais.calculadora_2 import calculadora_2_bp
from exemplos.condicionais.media import media_bp
from exemplos.laco_repeticao.exemplo_laco import laco_repeticao_bp
from exemplos.colecoes.carrinho_compra import carrinho_compra_bp
from exemplos.arquivos.manipulacao_arquivos import arquivos_bp
from exemplos.api.cotacao_dolar import api_bp 


# exercicios calculos
from exercicios.calculos.exercicio_1 import exercicio_1_bp
from exercicios.calculos.exercicio_2 import exercicio_2_bp
from exercicios.calculos.exercicio_3 import exercicio_3_bp
from exercicios.calculos.exercicio_4 import exercicio_4_bp
from exercicios.calculos.exercicio_5 import exercicio_5_bp

# exercicios operadores
from exercicios.operadores.exercicio_1 import exercicio_operadores_1_bp
from exercicios.operadores.exercicio_2 import exercicio_operadores_2_bp
from exercicios.operadores.exercicio_3 import exercicio_operadores_3_bp
from exercicios.operadores.exercicio_4 import exercicio_operadores_4_bp
from exercicios.operadores.exercicio_5 import exercicio_operadores_5_bp


# exercicios laço repetição
from exercicios.laco_repeticao.exercicio_1 import exercicio_laco_1_bp
from exercicios.laco_repeticao.exercicio_2 import exercicio_laco_2_bp

# exercicios coleções
from exercicios.colecoes.exercicio_1 import exercicio_colecoes_1_bp
from exercicios.colecoes.exercicio_2 import exercicio_colecoes_2_bp
from exercicios.colecoes.exercicio_3 import exercicio_colecoes_3_bp

# exercicios manipulação
from exercicios.manipulacao.exercicio_1 import arquivos_bp

# exercicios chamando api
from exercicios.chamando_api.exercicio_1 import api_exercicio_1_bp

# exercicios operadores html
from exercicios.operadores.exercicio_1 import exercicio_operadores_1_bp
from exercicios.operadores.exercicio_2 import exercicio_operadores_2_bp
from exercicios.operadores.exercicio_3 import exercicio_operadores_3_bp
from exercicios.operadores.exercicio_4 import exercicio_operadores_4_bp
from exercicios.operadores.exercicio_5 import exercicio_operadores_5_bp




app = Flask(__name__)

#Resgistros das blueprints no app principal
app.register_blueprint(calculadora_bp)
app.register_blueprint(calculadora_2_bp)
app.register_blueprint(media_bp)
app.register_blueprint(laco_repeticao_bp)
app.register_blueprint(carrinho_compra_bp)
app.register_blueprint(arquivos_bp)
app.register_blueprint(api_bp)

# exercicios calculos
app.register_blueprint(exercicio_1_bp)
app.register_blueprint(exercicio_2_bp)
app.register_blueprint(exercicio_3_bp)
app.register_blueprint(exercicio_4_bp)
app.register_blueprint(exercicio_5_bp)

# exercicios operadores
app.register_blueprint(exercicio_operadores_1_bp)
app.register_blueprint(exercicio_operadores_2_bp)
app.register_blueprint(exercicio_operadores_3_bp)
app.register_blueprint(exercicio_operadores_4_bp)
app.register_blueprint(exercicio_operadores_5_bp)

# exercicios laço repetição
app.register_blueprint(exercicio_laco_1_bp)
app.register_blueprint(exercicio_laco_2_bp)

# exercicios coleções
app.register_blueprint(exercicio_colecoes_1_bp)
app.register_blueprint(exercicio_colecoes_2_bp)
app.register_blueprint(exercicio_colecoes_3_bp)




#rotas
@app.get("/chama-aqui")
def inicial():
    return "Seja bem-vindo ao  Módulo Python"

@app.get("/calculos/calculadora")
def calculadora():
    return send_from_directory("paginas/calculos", "calcular.html")

@app.get("/carrinho_compra")
def carrinho_compra():
    return send_from_directory("paginas/calculos/colecoes", "compra.html")

