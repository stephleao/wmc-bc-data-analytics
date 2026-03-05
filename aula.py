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

# Isso é um Dicionário - semelhante a um array com chave/valor ou objeto
perfil = { "nome": "Ana", "estado": "RS"}

# Percorre cada chave imprimindo o rótulo da chave e seu valor atribuído
for chave in perfil:
  print(chave, perfil[chave])

# Outro exemplo
indice = 0

# Vai somar o valor do indice e do item e armazenar, em cada iteração
for item in range(3):
  indice += item
  print("Número atual:", indice)