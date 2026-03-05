# Laços de Repetição com FOR

# Lista
tecnologias = ["Python", "Dados", "IA"]

# Percorre cada item da lista imprimindo a informação armazenada
# range(len()) faz a mesma coisa do outro exemplo, mas o foco é na posição,
# então será útil para manipula-lo - modificar seu valor, comparar valores
# len() retorna o tamanho da lista e o range() cria a sequência numérica
for item in range(len(tecnologias)):
  # `item` aqui retorna a posição, não o valor
  print(tecnologias[item])