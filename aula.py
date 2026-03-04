# Operadores relacionais e precedência
# Retornam booleano - true/false

"""
Exemplos de operadores:
> maior que
< menor que
>= maior ou igual
<= menor ou igual
== igual a
!= diferente de
"""

valorA = int(input("Qual o valor A? "))
valorB = int(input("Qual o valor B? "))

print("A maior que B:", valorA > valorB)
print("A menor que B:", valorA < valorB)
print("A maior ou igual B:", valorA >= valorB)
print("A menor ou igual B:", valorA <= valorB)
print("A igual a B:", valorA == valorB)
print("A diferente de B:", valorA != valorB)

# Calcula e compara
resultado = valorA + valorB > 2
print(resultado)

# Precedência

# Priorizará a multiplicação
resultado = valorA + valorB * 2
print(resultado)

# Priorizará a soma
resultado = (valorA + valorB) * 2
print(resultado)