"""
Como parte de uma análise inicial, você precisa criar uma função para avaliar um conjunto de valores numéricos.

Crie uma função que receba uma lista de números e retorne:

- o valor máximo
- o valor mínimo
- a média dos valores
"""

lista_numeros = [345, 185, 46, 234]

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

# Função que concatena os resultados das demais e exibe-os para o usuário
def obter_valor(lista):
  print('Lista:', lista)
  print('Valor máximo:', obter_max(lista))
  print('Valor mínimo:', obter_min(lista))
  print('Média:', obter_media(lista))

# Executa a função concatenadora
obter_valor(lista_numeros)