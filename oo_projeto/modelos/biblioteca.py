class Biblioteca:
    # atributo de classe: lista que guarda todas as bibliotecas criadas
    bibliotecas = []

    def __init__(self, nome):
        # nome da biblioteca
        self.nome = nome
        # por padrão, a biblioteca começa desativada
        self.ativo = False
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


# criando a primeira biblioteca e adicionando automaticamente à lista
biblioteca_cidade = Biblioteca(nome="Biblioteca da Cidade")
# criando a segunda biblioteca e adicionando automaticamente à lista
biblioteca_shopping = Biblioteca(nome="Biblioteca do Shopping")

# exibe apenas o nome da biblioteca, por causa do __str__
print(biblioteca_shopping)
print(biblioteca_cidade)

# lista todas as bibliotecas criadas e seus estados (ativo ou não)
Biblioteca.listar_bibliotecas()
