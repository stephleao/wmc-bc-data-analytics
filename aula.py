# Acessando e Lendo Arquivos

arquivo = "alunas.txt"

# Acessa o arquivo para leitura em UTF-8, e garante que ele seja fechado
# corretamente
with open(arquivo, mode="r", encoding="utf-8") as lista:
  # `with ... as ...` : gerenciador de contexto -> dá mais segurança e controle
  # `with ...` : garante que o arquivo será automaticamente fechado ao final do
  # bloco identado, mesmo que ocorra erro no bloco -> boa prática
  # `open()` : abre um objeto de arquivo
  # `mode="r"` : "read", leitura
  # `encoding="utf-8"` : trata corremente caracteres especiais
  # `as` : associa a uma variável
  # `lista` : variável que representa o objeto do arquivo e poderá manipulá-lo
  # com os métodos

  # percorre cada linha do arquivo e imprime
  for linha in lista:
    # strip() vai limpar a linha vazia do arquivo
    print(linha.strip())

  # resultado é o mesmo do exemplo anterior, com a diferença que lá todo o
  # conteúdo do arquivo estava sendo impresso de uma vez, sem tratamento.