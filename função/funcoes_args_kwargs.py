"""
*agrs - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter uma função
- Os argumentos são passados como uma tupla

**kwargs - Além dos valores podemos passar tambem as respectivas chaves para cada argumento.
- Os argumentos são passados como um dicionário
"""

# 1 -> Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")

sum(7)
sum(7,9)
sum(7,9,10,11)
sum(7,10,9,8,7,6)

# 2 - Apresentação de cursos
def presentation(**data):
    for key,value in data.items():
        print(f"{key} - {value}")

print("=" * 20)
print('Lista de cursos:')
presentation(name='Python',category='Backend', level='Iniciante')
print("=" * 20)
presentation(name='Visão Computacional',category='IA', level='Avançado')
print("=" * 20)
presentation(name='Dashbords com Dash',category='Data Science', level='Intermediario')

#