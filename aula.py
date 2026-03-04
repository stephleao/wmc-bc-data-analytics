# Fazendo o código tomar decisões
# Condições com if, else, elif

idade = 65
eh_membro = True

if idade >= 60:
  if(eh_membro):
    print("Desconto 30%")
  else:
    print("Desconto 20%")
elif idade >= 50:
  print("Cashback 10%")
else:
  print("Sem desconto")