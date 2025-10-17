class Game:
    name = ""
    yearLauch = ""
    multiplayer = False
    note = 0

# Primeiro jogo
game1 = Game()
game1.name = 'The Legend of Zelda: breath of the Wild'
game1.yearLauch = 2017
game1.multiplayer = False
game1.note = 9.5

#Segundo Jogo
game2 = Game()
game2.name = "Fortnite"
game2.yearLauch = 2017
game2.multiplayer = True
game2.note = 8.0

print("=== Dados dos Jogos ===")
print(f'Nome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLauch}\n')
print(f'Nome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLauch}')
