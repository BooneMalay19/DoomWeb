import subprocess
import os
import sys

# Caminho para o executável do Chocolate Doom
doom_executable = r"C:\caminho\para\chocolate-doom.exe"  # Altere para o caminho correto

# Caminho para o arquivo WAD (exemplo: doom.wad)
wad_file = r"C:\caminho\para\doom.wad"  # Altere para o caminho correto

def run_chocolate_doom():
    # Verifica se o executável e o arquivo WAD existem
    if not os.path.exists(doom_executable):
        print("Erro: O executável do Chocolate Doom não foi encontrado.")
        sys.exit(1)

    if not os.path.exists(wad_file):
        print("Erro: O arquivo WAD não foi encontrado.")
        sys.exit(1)

    # Executa o Chocolate Doom usando subprocess
    try:
        subprocess.run([doom_executable, wad_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar rodar o Chocolate Doom: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_chocolate_doom()
