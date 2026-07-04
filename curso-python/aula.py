# Tratamento de Erros
# Evita que o programa pare, trabalhando as excessões
# Trate os erros específicos, use com mensagens claras
# Evite usar excepts genéricos, pois mascaram a causa do erro
# Evite colocar muito código dentro do try

# try/except é como if/else: tente fazer, se der erro, faça tal coisa
try: # tentando ler um arquivo
  arquivo = open("dados.txt", mode="r")
  conteudo = arquivo.read()

except FileNotFoundError: # Se o arquivo não existir
  print("Arquivo não encontrado")

finally: # Será sempre executado com ou sem erro
  print("Operação concluída")
