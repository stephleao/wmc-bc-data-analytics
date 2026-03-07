# Criando arquivos

arquivo = "alunas.txt"

# Cria/abre um arquivo para escrita em UTF-8, e garante que ele seja fechado
# corretamente
with open(arquivo, mode="w", encoding="utf-8") as lista:
  # `with ... as ...` : gerenciador de contexto -> dá mais segurança e controle
  # `with ...` : garante que o arquivo será automaticamente fechado ao final do
  # bloco identado, mesmo que ocorra erro no bloco -> boa prática
  # `open()` : abre um objeto de arquivo
  # `mode="w"` : "write", escrita. Se existir, será sobrescrito; senão, criado
  # `encoding="utf-8"` : trata corremente caracteres especiais
  # `as` : associa a uma variável
  # `lista` : variável que representa o objeto do arquivo e poderá manipulá-lo
  # com os métodos

  # write() é o método de escrita
  lista.write("Ana\n")
  lista.write("Beatriz\n")
  lista.write("Gisele\n")