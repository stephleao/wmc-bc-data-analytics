# Laços de Repetição com WHILE
# Usado quando não sabemos quantas vezes vai repetir
# Enquanto a condição for verdadeira - Cuidado com o looping infinito!

# Incremento
contador = 0

while contador < 3:
  contador += 1
  print("Oi!")

# Decremento
tentativas = 3

while tentativas >= 0:
  print("Você tem", tentativas, "tentativas")
  tentativas -= 1