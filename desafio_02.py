"""
Como parte de uma análise inicial, você precisa criar uma função para avaliar um conjunto de valores numéricos.

Crie uma função que receba uma lista de números e retorne:

- o valor máximo
- o valor mínimo
- a média dos valores
"""

# Função que obtém o maior valor
def obter_max(lista):
  # Variavel começa com o primeiro item da lista para comparar
  comparador = lista[0]

  # Percorre a lista de numeros
  for numero in lista:
    # Checa entre o comparador e o numero para poder guardar o valor
    if numero > comparador:
      comparador = numero

  return comparador

# Função que obtém o menor valor
# Mesma lógica da função max, porém verificando se é menor
def obter_min(lista):
  comparador = lista[0]

  for numero in lista:
    if numero < comparador:
      comparador = numero

  return comparador

# Função que calcula a média
def obter_media(lista):
  media = 0

  # Percorre a lista de numeros
  for numero in lista:
    media += numero # Soma os valores e guarda

  # divide a media pela quantidade da lista e retorna
  return media / len(lista)

# Função que concatena os resultados das demais
def obter_valores(lista):
  maximo = obter_max(lista)
  minimo = obter_min(lista)
  media = obter_media(lista)

  return maximo, minimo, media

# Testando as funções

lista_numeros = [345, 185, 46, 234]

print('Lista:', lista_numeros)
print('Máximo, mínimo e a média:', obter_valores(lista_numeros))