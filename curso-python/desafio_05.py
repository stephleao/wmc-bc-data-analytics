"""
Antes de carregar os dados de novas inscritas em um evento para o banco de dados, você precisa limpá-los. Você recebeu uma lista de dicionários com nomes e cargos, mas os dados estão inconsistentes.

Crie um programa que percorra a lista e faça duas limpezas:

Remova espaços em branco no início e no final dos nomes. Padronize o campo cargo para que todas as variações de "Analista de Dados" (ex: "data analyst", "Analista de dados") se tornem "Analista de Dados".
"""

inscricoes = [
  {"nome": "  Ana Clara ", "cargo": "data analyst"},
  {"nome": "Beatriz Guedes", "cargo": "Cientista de dados"},
  {"nome": "Carla Dias", "cargo": "analista de Dados"},
  {"nome": "Daniela Moura  ", "cargo": "Engenheira de dados"},
  {"nome": " Eduarda Santana  ", "cargo": "Analista de dados"}
]

cargos_despadronizados = ("data analyst", "analista de dados")
cargo_analista = "Analista de Dados"

print("Dados limpos:\n")

# Percorre o dicionário de inscricoes
for inscrita in inscricoes:
  # Limpa a string e guarda o valor no item
  inscrita["nome"] = inscrita["nome"].strip()

  # Checa se o valor do cargo está na lista sem padrão
  if inscrita["cargo"].lower() in cargos_despadronizados:
    # Sem padrão, cargo recebe o valor padrão
    inscrita["cargo"] = cargo_analista

  print(inscrita)

print(f"\nLista: {inscricoes}")