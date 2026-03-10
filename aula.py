# Tratamento de Erros
# Evita que o programa pare, trabalhando as excessões

# try/except é como if/else: tente fazer, se der erro, faça tal coisa
try:
  # se digitar qualquer coisa além de número, dará erro
  numero = int(input("Digite um número: "))
  resultado = 10 / numero

# Checa se é uma divisão por zero
except ZeroDivisionError:
  print("Não é possível dividir por zero")

# Checa se o valor tem o tipo correto
except ValueError:
  print("Digite somente números inteiros")

else:
  print(f"Resultado: {round(resultado, 2)}")
