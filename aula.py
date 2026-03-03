# Números inteiros
escola = 12
aulas = 35
alunos = 23

print("Código da escola:", escola, " Aulas realizadas:", aulas, " Alunos: ", alunos)

# Este não é um inteiro
preco = 2.50

print("Valor por minuto:", int(preco))

# Isso daria erro se inserisse números decimais sem converter antes para float
preco_promo = int(float(input("Valor promocional: ")))

print("Valor promocional por minuto:", int(preco_promo))