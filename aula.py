# Dicionários
# Armazena dados de uma única coisa
# Semelhante a um objeto ou array associativo

# É possível misturar listas e dicionários

escola = [ # lista de alunas (dicionários) de uma escola
  {
    "nome": "Ana",
    "idade": 45,
    "curso": "Python",
    "status": True
  },
  {
    "nome": "Cynthia",
    "idade": 34,
    "curso": "C#",
    "status": True
  },
  {
    "nome": "Clarice",
    "idade": 23,
    "curso": "Dados",
    "status": False
  }
]

print(escola) # imprime toda a lista

for aluna in escola:
  print(aluna) # imprime individualmente cada item da lista
