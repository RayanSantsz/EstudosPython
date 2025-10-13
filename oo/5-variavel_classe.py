# classe e atributos
class Game:
    # variavel de classe: para contar o número total de jogos
    total_games = 0

    # metodo construtor: irá passar automaticamente os atributos no momento em que a classe for instanciada
    def __init__(self, name='', yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        # toda vez que o método construtor for chamado, vai criar um novo game
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0

    # self é utilizado para acessar os atributos da classe
    def __str__(self):
        return f'Game: {self.name}'

    # metodo para trazer as informações do game de forma mais limpa
    def technical_sheet(self):
        print('=== Dados dos Jogos ===')
        print(f'Nome do jogo: {self.name}')
        print(f'Ano de lançamento: {self.yearLaunch}')
        print(f'Modo multiplayer? {self.multiplayer}')
        print(f'Avaliação do jogo: {self.note}\n')

    # metodos para avaliar o jogo
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f'Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}')


# ao criar os objetos, os parametros devem ser passados para que o construtor receba os dados e armazene
game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("Red Dead Redemption 2", 2018, False, 10.0)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9.0)
game1.evaluate(7.5)
game1.average()
game2.evaluate(6.5)
game2.evaluate(7.5)
game2.average()

# exibindo o numero total de jogos criados
print(f'\nTotoal de jogos criados: {Game.total_games}')