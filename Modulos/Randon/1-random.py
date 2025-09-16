import random

# 1 -> seleciona valor aleatório de uma lista
list1 = [7, 6, 4, 3, 2, 1]
print(random.choice(list1))

# 2 -> gera um número aleatório em um itervalo de valores
r1 = random.randint(5,15)
print(r1)

# 3 -> seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4 -> seleciona mais de um valor aleatorio
# random.sample(sequencia,tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = "olá mundo"
print(random.sample)
