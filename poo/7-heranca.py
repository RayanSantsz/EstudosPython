# classe pai (super classe) - Generalista
class Game:
    # variável de classe que conta o número total de jogos criados
    total_game = 0

    # método construtor (inicializa os atributos do objeto)
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name  # nome do jogo
        self.yearLaunch = yearLaunch  # ano de lançamento
        self.multiplayer = multiplayer  # se é multiplayer (True/False ou 1/0)
        self.note = note  # nota inicial do jogo
        Game.total_game += 1  # toda vez que um jogo é criado, incrementa o contador de jogos
        self.totalEvaluation = 0  # soma das notas recebidas nas avaliações
        self.evaluators = 0  # quantidade de pessoas que avaliaram

    # método especial que define a forma como o objeto será exibido em string
    def __str__(self):
        return f"Game: {self.name}"

    # método que imprime a ficha técnica do jogo
    def technical_sheet(self):
        print(" === Dados dos jogos ===")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Avaliação: {self.note}\n")

    # método para avaliar o jogo (somando as notas)
    def evaluate(self, note):
        self.totalEvaluation += note  # soma a nota à avaliação total
        self.evaluators += 1  # incrementa o número de avaliadores

    # método que calcula e mostra a média das avaliações
    def average(self):
        print(f'Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}')


# classe derivada (subclasse) - especializada em jogos single player
class singlePlayerGame(Game):
    # construtor da subclasse
    def __init__(self, name='', yearLaunch=0, note=0, storyLine=''):
        # chama o construtor da classe pai (superclasse)
        super().__init__(name, yearLaunch, multiplayer=False, note=note)
        self.storyLine = storyLine  # atributo extra: enredo da história do jogo

    # sobrescreve o método da classe pai para incluir o enredo
    def technical_sheet(self):
        super().technical_sheet()  # chama o método da classe pai para reaproveitar o código
        print(f"Enredo: {self.storyLine}\n")


# criando um objeto da classe Game (jogo multiplayer)
mult_game = Game('Fortnite', 2017, True, 8.0)
mult_game.technical_sheet()  # exibindo ficha técnica do jogo

# criando um objeto da classe singlePlayerGame (jogo single player)
sing_game = singlePlayerGame("The Last of Us", 2020, 9.5, 'Emocionante história de sobrevivência e vingança')
sing_game.technical_sheet()  # exibindo ficha técnica do jogo (inclui o enredo)
