"""
Como parte de uma análise inicial, você precisa criar uma função para avaliar um conjunto de valores numéricos.

Crie uma função que receba uma lista de números e retorne:

- o valor máximo
- o valor mínimo
- a média dos valores
"""

def obter_valores(lista):
  soma = 0
  # Variaveis de max/min começam com o primeiro item da lista para comparar
  maximo = lista[0]
  minimo = lista[0]

  # Percorre a lista de numeros
  for numero in lista:
    soma += numero # Soma os valores e guarda

    # Verifica se o numero é maior/menor
    if numero > maximo:
      maximo = numero
    elif numero < minimo:
      minimo = numero

  media = soma / len(lista) # divide soma pela quantidade da lista

  return maximo, minimo, media

# Testando a função

lista_numeros = [345, 185, 46, 234]

print('Lista:', lista_numeros)
print('Máximo, mínimo e a média:', obter_valores(lista_numeros))