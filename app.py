from flask import Flask, render_template
import subprocess
import os
import sys

app = Flask(__name__)

doom_executable = r"C:\Users\PEDROBRITODESOUZA\Desktop\doom\chocolate-doom.exe" 
wad_file = r"C:\Users\PEDROBRITODESOUZA\Desktop\doom\doom.wad"

@app.route('/')
def index():
    # Exibir página com o YouTube e um botão para iniciar o Doom
    return render_template('index.html')

@app.route('/start_doom')
def start_doom():
    # Rodar o Chocolate Doom quando o link for acessado
    if not os.path.exists(doom_executable):
        return "Erro: O executável do Chocolate Doom não foi encontrado."
    if not os.path.exists(wad_file):
        return "Erro: O arquivo WAD não foi encontrado."
    
    try:
        subprocess.run([doom_executable, wad_file], check=True)
        return "Doom está rodando!"
    except subprocess.CalledProcessError as e:
        return f"Erro ao tentar rodar o Chocolate Doom: {e}"

if __name__ == "__main__":
    app.run(debug=True)
