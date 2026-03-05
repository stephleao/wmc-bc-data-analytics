# Fazendo o código tomar decisões
# Condições com if, else, elif

nota1 = 7
nota2 = 8
nota3 = 5

# a divisão retorna float, arrendondamos para 2 casas
media = round((nota1 + nota2 + nota3) / 3, 2)

if media >= 7:
  print("Aprovada - Média: ", media)
elif media >= 5:
  print("Recuperação - Média: ", media)
else:
  print("Reprovada - Média: ", media)