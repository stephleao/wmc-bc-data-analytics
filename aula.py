# Atualizando Arquivos
# Precimos ler o arquivo para então escrever

arquivo = "alunas.txt"
alunas = []

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
  alunas = lista.readlines() # Guarda cada linha na lista

alunas_atualizadas = [] # Lista que receberá os dados

# Percorre cada item da lista
for aluna in alunas:
  # Guarda o nome limpo
  nome = aluna.strip()

  # Checa o nome que queremos remover
  if nome != "Gisele":
    alunas_atualizadas.append(nome) # Guarda o nome na lista se for true

# Precisamos escrever essa lista com os dados atualizados no arquivo
with open(arquivo, mode="w", encoding="utf-8") as lista:
  # Percorre cada item da lista atualizada
  for aluna in alunas_atualizadas:
    # Escreve no arquivo o dado
    lista.write(aluna + "\n")