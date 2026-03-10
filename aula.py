# Tratamento de Erros
# Evita que o programa pare, trabalhando as excessões

# try/except é como if/else: tente fazer, se der erro, faça tal coisa
try:
  # se digitar qualquer coisa além de número, dará erro
  numero = int(input("Digite um número: "))
  print(10 / numero)
except: # Evita que o programa pare devido ao erro
  print("Ocorreu um erro")