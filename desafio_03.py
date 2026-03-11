"""
Você recebeu uma lista com os nomes das participantes inscritas no bootcamp e precisa realizar uma filtragem simples para organização interna.

Crie um programa que percorra a lista e exiba apenas as participantes da Região Sul.
"""

participantes = [
  {"nome": "Ana Paula", "regiao": "Sul"},
  {"nome": "Beatriz", "regiao": "Sudeste"},
  {"nome": "Carla", "regiao": "Nordeste"},
  {"nome": "Daniela", "regiao": "Sul"},
  {"nome": "Eduarda", "regiao": "Centro-Oeste"},
  {"nome": "Fernanda", "regiao": "Norte"},
  {"nome": "Gabriela", "regiao": "Sul"},
  {"nome": "Helena", "regiao": "Sudeste"},
  {"nome": "Isabela", "regiao": "Nordeste"},
  {"nome": "Juliana", "regiao": "Centro-Oeste"},
  {"nome": "Karina", "regiao": "Sul"},
  {"nome": "Larissa", "regiao": "Sudeste"},
  {"nome": "Mariana", "regiao": "Norte"},
  {"nome": "Natália", "regiao": "Nordeste"},
  {"nome": "Patrícia", "regiao": "Sul"}
]

filtro_regiao = "sul"

participantes_sul = [] # receberá os dados filtrados

print(f"Participantes da região {filtro_regiao.upper()}:\n")

# Percorre a lista
for participante in participantes:
  # Checa se a participante é da região especificada
  if participante["regiao"].lower() == filtro_regiao:
    # Adiciona participante a lista de filtragem
    participantes_sul.append(participante["nome"])
    print(participante["nome"])

print(f"\nLista: {participantes_sul}")