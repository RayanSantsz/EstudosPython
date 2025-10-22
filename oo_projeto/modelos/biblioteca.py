class Biblioteca:
    # atributo de classe: lista que guarda todas as bibliotecas criadas
    bibliotecas = []

    def __init__(self, nome):
        # nome da biblioteca
        self.nome = nome
        # por padrão, a biblioteca começa desativada
        self._ativo = False
        # adiciona automaticamente a biblioteca criada na lista de todas as bibliotecas
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        # define o que aparece ao usar print(objeto)
        # aqui retorna apenas o nome da biblioteca
        return self.nome

    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Status'}")
        # percorre todas as bibliotecas já criadas e exibe seus dados
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"



