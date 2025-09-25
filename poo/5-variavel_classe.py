class Game:
    total_game = 0 # variavel de classe para contar o número total de jogos
    def __init__(self, name="",yearLaunch=0, multiplayer=0,note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_game += 1
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f"Game: {self.name}"

    def technical_sheet(self):
        print(" === Dados dos jogos ===")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Avaliação: {self.note}\n")

    def evaluate(self,note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f'Média do filme {self.name}: {self.totalEvaluation / self.evaluators}')

game1 = Game('The Legend od Zelda', 2017, False, 9.5)
game2 = Game('Fortnite', 2017, True, 8.0)

game1.technical_sheet()
game1.evaluate(9.0)
game1.evaluate(7.5)

game2.technical_sheet()
game2.evaluate(6.5)
game2.evaluate(7.5)

game1.average()
game2.average()

# Exibindo o numero total de jogos criados
print(f'Total de jogos criado: {Game.total_game}')