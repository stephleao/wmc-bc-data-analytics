# Trabalhando com textos - String

nome = "Stephanne"

print(nome)

# Slicing
# Pega apenas o caractere da posição 1, que é o ´t´
print(nome[1])
# Pega caracteres a partir da posição 0 até antes da posição 5, ou seja 4
print(nome[0:5])

# Quebras de linha
frase1 = "Quanto mais estudo, \nmais sinto que minha mente \nnisso é insaciável."
print(frase1)

# Quebra como texto pre-formatado - 3x aspas simples ou duplas
# Escape de caracteres - usa `\` antes
frase2 = """\"Quanto mais estudo,
mais sinto que minha mente
nisso é insaciável.\""""
print(frase2)

# Ao usar aspas simples, não é necessário fazer escape das aspas duplas
# Poderia usar as aspas simples triplicadas para deixar pre-formatado
frase3 = '"Quanto mais estudo, mais sinto que minha mente nisso é insaciável."'
print(frase3)