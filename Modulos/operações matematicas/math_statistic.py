import math

# 1 -> Acessar o número PI
print(math.pi)
print(f'{math.pi:.2f}')
print("=" * 20)
# 2 -> Acessar o número de Euler
print(math.e)
print(f'{math.e:.2f}')
print("=" * 20)

# 3 -> Arredondando números para cima e para baixo
num = 10.4
print(math.ceil(num)) # arredonda para cima
print(math.floor(num)) #arredonda para baixo
print("=" * 20)

# 4 -> Fatorial de um numero
num2 = int(input("Digite um número: "))
print(math.factorial(num2))
print("=" * 20)

# 5 -> Potência de números
print(math.pow(5,5)) # potencia
print("=" * 20)

# 6 -> Raiz quadrada de um número
print(math.sqrt(169)) # raiz
print("=" * 20)

# 7 -> MDC = Maximo divisor comum
mdc = math.gcd(20,100)
print(mdc)
print("=" * 20)

# 9 -> Logaritimo
print(math.log(10))
