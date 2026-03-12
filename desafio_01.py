"""
Você recebeu uma lista com os títulos das palestras submetidas para um evento "Women in Data". Sua primeira tarefa é fazer uma contagem rápida de quantos títulos mencionam temas de BI.

Crie um programa que percorra a lista de títulos e conte quantos deles contêm as palavras-chave "dados", "análise" ou "inteligência" (sem diferenciar maiúsculas e minúsculas).
"""

titulos_palestras = [
  "Machine Learning para Negócios",
  "O Poder da Análise de Dados no Varejo",
  "Introdução ao SQL",
  "Business Intelligence com Power BI",
  "Carreira em Dados: Dicas para Mulheres",
  "Storytelling com Inteligência Artificial"
]

# Como o desafio não explicita a inclusão de palavras estrangeiras, segui as
# palavras-chave à risca. Caso inclua "intelligence", o resultado será outro.
palavras_chave = ("análise", "dados", "inteligência")

contador = 0

print(f'Títulos que possuem as palavras {palavras_chave}:\n')

# Percorre a lista de títulos
for titulo in titulos_palestras:
  # Percorre a lista de palavras-chave
  for palavra in palavras_chave:
    # Verifica se a palavra está contida no título
    if palavra in titulo.lower():
      contador += 1
      print(f"{contador}. {titulo}")

      break # Força parada para não fazer mais contagem no mesmo título

print(f"\nTotal de títulos com as palavras-chave: {contador}")