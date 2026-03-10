# Deletando Arquivos

# Importando módulo OS - que interage com o sistema operacional, para acessar
# os arquivos
import os

arquivo = "alunas.txt"

# Checa se o arquivo existe no sistema
# "Se o caminho deste arquivo existir no SO"
if os.path.exists(arquivo):
  os.remove(arquivo) # Remove o arquivo
  print("Arquivo deletado")
else:
  print("Arquivo não encontrado")