# Dicionários
# Armazena dados de uma única coisa
# Semelhante a um objeto ou array associativo

aluna = {
  "nome": "Ana",
  "idade": 45,
  "curso": "Python",
  "status": True
}

print(aluna)
print(aluna["nome"])

aluna["idade"] = 54 # Altera o valor de idade
aluna["cidade"] = "São Paulo" # Adiciona um novo conjunto de chave+valor

print(aluna)

aluna.pop("idade") # Remove um conjunto de chave+valor
print(aluna)