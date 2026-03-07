# Listas

cursos = ["Python", "Git", "Design", "CV"]

# Impremindo a lista e a posição 1
print(cursos)
print(cursos[1])

# Altera o valor da posição 1
cursos[1] = "Git e Github"
print(cursos)

# Adiciona um novo item na lista
cursos.append("Dados")
print(cursos)

# Remove um item da lista
cursos.remove("Design") # pelo valor
cursos.pop(0) # pela posição
print(cursos)