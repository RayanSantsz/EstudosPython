class Game:
    def __init__(self,name='', yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f'Game: {self.name}'

    def technical_sheet(self):
        print("=== Dados do Jogo ===")
        print(f'Nome do jogo: {self.name}')
        print(f'Ano de lançamento: {self.yearLaunch}')
        print(f'Modo multiplayer: {self.multiplayer}')
        print(f'Avaliação do jogo: {self.note}\n')
