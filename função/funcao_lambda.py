# Função de potência de um número
power = lambda num: num ** 2
print(power(5))
print(power(9))

# Função que verifica se o número é par
is_even = lambda x: x % 2 == 0
print(is_even(27))
print(is_even(30))

# Função que divide um número por outro
div_num = lambda x,y: x / y
print(div_num(10,2))
print(div_num(6,2))

# Função que inverte um string
reverse_string = lambda s: s[::-1]
print(reverse_string("Python"))
print(reverse_string("JavasCript"))

# Funcionalidades relacionadas aos filmes:
movie_list = ["Titanic", "The GodFather", "Inception", "Jurassic Park", "The Matrix"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "The GodFather": [9.5, 9.9, 8.0],
    "Inception": [8.0, 7.0, 8.5],
    "Jurassic Park": [7.5, 7.0, 8.5],
    "Matrix": [8.8, 9.2, 8.5],
}

# Função para calcular a média de avalianções de um filme
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])
print(f"Média de avaliações do filme Matrix: {average_rating('Matrix'):.2f}")
