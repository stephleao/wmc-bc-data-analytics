# Operações Matemáticas

"""
Exemplos de operadores:
+ soma
- subtração
* multiplicação
/ divisão - vai retornar decimal
/ divisão inteira - vai retornar inteiro
% resto da divisão
** potenciação
"""

valorA = int(input("Qual o valor A? "))
valorB = int(input("Qual o valor B? "))

# Armazenando os resultados dos cálculos
result_soma = valorA + valorB
result_subtr = valorA - valorB
result_mult = valorA * valorB
result_div = valorA / valorB
result_div_int = valorA // valorB
result_resto = valorA % valorB
result_pot = valorA ** valorB

print("soma:", result_soma)
print("subtração:", result_subtr)
print("multiplicação:", result_mult)
print("divisão:", result_div)
print("divisão inteira:", result_div_int)
print("resto da divisão:", result_resto)
print("potenciação:", result_pot)