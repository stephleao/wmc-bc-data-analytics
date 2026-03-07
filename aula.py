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
  # Forma mais prática e direta de imprimir os valores, dentro da própria string
  print(f"Nome: {aluna['nome']}") # `f` = formatado
  print(f"Curso: {aluna['curso']}")
  print("-" * 20)

# Criando uma variável e atribuindo um dicionário da lista
aluna = escola[2]

print(aluna)