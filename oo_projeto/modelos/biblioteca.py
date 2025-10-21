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

    def listar_bibliotecas():
        # percorre todas as bibliotecas já criadas e exibe seus dados
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} | {biblioteca.ativo}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"



# criando a primeira biblioteca e adicionando automaticamente à lista
biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
# criando a segunda biblioteca e adicionando automaticamente à lista
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

# exibe apenas o nome da biblioteca, por causa do __str__
print(biblioteca_shopping)
biblioteca_shopping.alterna_estado()
print(biblioteca_cidade)
biblioteca_cidade.alterna_estado()

# lista todas as bibliotecas criadas e seus estados (ativo ou não)
Biblioteca.listar_bibliotecas()
