# Operações Especiais

"""
Exemplos de operadores:
+= Implemento
-= Decremento
"""

valorA = int(input("Qual o valor A? "))
valorB = int(input("Qual o valor B? "))

# Pega o valor inserido, calcula com o valor e armazena de novo
valorA += 5 # equivale a valorA = valorA + 5
valorB -= 2 # equivale a valorB = valorB - 2

print("Resultado de A:", valorA)
print("Resultado de B:", valorB)

# Uso do resto
if valorA % 2 == 0:
  print("A é par")
else:
  print("A é ímpar")