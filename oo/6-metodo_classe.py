class Game:
    total_games = 0  # Variável de classe para contar o número total de jogos

    def __init__(self, name="", yearLaunch=0, multiplayer=False, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1  # Toda vez que um jogo é criado, soma +1 ao total
        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self):
        return f"Game: {self.name}"

    def technical_sheet(self):
        print("### Dados do Jogo ###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer?: {self.multiplayer}")
        print(f"Avaliação do Jogo: {self.note}\n")

    def evaluate(self, note):
        # Adiciona uma nova avaliação ao jogo
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        # Calcula e mostra a média das avaliações do jogo
        if self.evaluators > 0:
            print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")
        else:
            print(f"O jogo {self.name} ainda não foi avaliado.")

    @classmethod
    def print_total_games_stats(cls):
        print("#### Estatísticas Gerais dos Jogos ####")
        print(f"Total de jogos criados: {cls.total_games}")
        # (Removido o erro: o código tentava chamar 'cls.average(cls)', que não faz sentido)
        # A classe não tem uma média geral implementada, apenas os objetos têm.


# Criação de objetos (jogos)
game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("Red Dead Redemption 2", 2018, False, 10.0)

# Mostrando as fichas técnicas
game1.technical_sheet()
game2.technical_sheet()

# Avaliando os jogos
game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)

# Mostrando médias
game1.average()
game2.average()

# Mostrando total de jogos criados
Game.print_total_games_stats()
