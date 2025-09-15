# 1 -> Função para imprimir uma mensagem
def welcome():
    print("Bem vindo ao sistema de filmes!")
welcome()

# 2-> Função para calcular média de notas
def calculate_average():
    num_ratings = int(input('Digite quantas avaliações deseja fazer pro filme: '))
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme: "))
        total += note

    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    return average

print(f"A média de avaliações é: {calculate_average():.2f}")

# 3 -> Função para cadastrar um filme
def create_movie():
    name = input("Digite o nome do filme: ")
    yearLauch = int(input(" Digite o ano de lançamento do filme: "))
    moviePrice = float(input("Qual valor do ingresso: "))
    rating = float(input("Digite a nota do filme: "))
    print(f"{name} ({yearLauch}) - R${moviePrice:.2f}")

create_movie()