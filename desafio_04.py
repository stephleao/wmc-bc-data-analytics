"""
Após uma palestra sobre "O Futuro da IA", foi feita uma enquete com a pergunta: "Qual foi o tópico mais impactante?". Os resultados foram armazenados em um dicionário onde a chave é o tópico e o valor é o número de votos.

Sua tarefa é calcular o número total de votos e exibir o resultado da enquete em porcentagens.
"""

resultado_enquete = {
  "IA Generativa": 120,
  "Ética em IA": 85,
  "IA no Mercado de Trabalho": 95,
  "Ferramentas de MLOps": 50
}

total = 0

print("Resultado da enquete:\n")

# Percorre o dicionario de tópicos
for topico in resultado_enquete:
  # Soma cada valor de votos e guarda na variavel
  total += resultado_enquete[topico]

# Percorre o dicionario de tópicos
for topico in resultado_enquete:
  votos = resultado_enquete[topico]
  # Calcula a porcentagem dos votos e arredonda
  porcentagem = round(votos * 100 / total, 1)

  print(f"{topico}: {porcentagem}%")

print(f"\nTotal de votos: {total}")