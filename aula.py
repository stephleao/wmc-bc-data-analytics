# Trabalhando com funções
# Um bloco de código que executa uma tarefa
# Reaproveita código
# É como uma receita
# Boa função faz uma ação só, deve ter nome claro

# def vem de 'define function' ou só 'defina'
# Passando um parâmetro, que é como uma variável que guardará um valor ao usar
# a função
def saudacao(nome, estado): # permite vários parâmetros
  print(f"Seja bem-vinda, {nome}. Muito bom ver alguém de {estado}.")

# Dará erro se não passar o valor do parâmetro que a função espera
saudacao("Steph", "RJ")

# Exemplo de função para cálculo
def soma(a, b):
  # Devolvendo um valor (que poderá ser usado em outras partes do código)
  return a + b

resultado = soma(5, 3)
print(resultado)

# Exemplo com checagem
def verificar_idade(idade):
  if idade >= 18:
    return "Maior de idade" # vai parar a execução aqui e retornar o valor se for verdadeiro
  else: # esse else poderia ser descartado e o return fora do if
    return "Menor de idade"

print(verificar_idade(38))