# Números decimais - Float
preco = 2.50
temperatura = -3.14
media_notas = 7.5

# Aqui vai sobrescrever `preco` com a string que o usuário inserir
preco = input("Valor por minuto: ")

preco_promo = float(input("Valor promocional: "))

# `float()` também pode ser usado diretamente aqui na variável a ser convertida
# O número pode retornar com muitas casas decimais, por isso `round()`
print("Diferença de preço:", round(float(preco) - preco_promo, 2))