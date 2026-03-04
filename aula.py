# Números decimais - Float
preco = 2.50
temperatura = -3.14
media_notas = 7.5

# Aqui vai sobrescrever `preco` com a string que o usuário inserir
preco = input("Valor por minuto: ")

preco_promo = float(input("Valor promocional: "))

# Como `preco_promo` está como string, esse cálculo dá erro
print("Diferença de preço:", preco - preco_promo)