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

  linhas = lista.readlines()

print(linhas)

# O resultado retorna uma lista, porém "suja"