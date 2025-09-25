# Classe Game - representa um jogo individual
class Game:
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name                  # Nome do jogo
        self.yearLaunch = yearLaunch      # Ano de lançamento
        self.multiplayer = multiplayer    # Se é multiplayer (True/False ou 1/0)
        self.note = note                  # Nota inicial do jogo
        self.totalEvaluation = 0          # Soma de avaliações recebidas
        self.evaluators = 0               # Quantidade de avaliadores

    # Método especial que define a forma como o jogo é exibido como string
    def __str__(self):
        return f"Game: {self.name}"

    # Exibe os dados técnicos (ficha técnica) do jogo
    def technical_sheet(self):
        print(" === Dados dos jogos ===")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Avaliação: {self.note}\n")


# Classe GameStudio - representa um estúdio que pode ter vários jogos
class GameStudio:
    def __init__(self, nome=""):
        self.nome = nome      # Nome do estúdio
        self.games = []       # Lista para armazenar objetos da classe Game

    # Adiciona um jogo à lista de jogos do estúdio
    def add_game(self, game):
        self.games.append(game)

    # Avalia a qualidade geral do estúdio com base na média das notas dos jogos
    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)  # soma todas as notas dos jogos
        num_games = len(self.games)  # conta quantos jogos o estúdio tem
        if num_games == 0:
            print(f'O estúdio {self.nome} ainda não lançou jogo')
        else:
            average_note = total_notes / num_games  # calcula a média
            print(f'Avaliação média dos jogos do estúdio {self.nome}: {average_note:.2f}')


# Criando objetos da classe Game (jogos)
game1 = Game('The Legend od Zelda', 2017, False, 9.5)
game2 = Game('Fortnite', 2017, True, 8.0)
game3 = Game("The last od Us II", 2020, False, 9.0)

# Criando um estúdio e adicionando os jogos criados
studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)


# Exibindo a ficha técnica de todos os jogos do estúdio
for game in studio.games:
    game.technical_sheet()

# Avaliando a qualidade geral do estúdio (média das notas dos jogos)
studio.evaluate_studio_quality()
