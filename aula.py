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

# Unindo mais conceitos

for aluna in escola:
  if aluna["nome"] == "Cynthia": # checagem
    print(f"Nome: {aluna['nome']}")
    print(f"Curso: {aluna['curso']}")