class Biblioteca:
    nome = ""
    ativo = False

biblioteca_cidade = Biblioteca()
biblioteca_cidade.nome = "Biblioteca da Cidade"
biblioteca_cidade.ativo = True

biblioteca_shopping = Biblioteca()

bibliotecas = [biblioteca_shopping, biblioteca_cidade]

print(vars(biblioteca_shopping))
print(vars(biblioteca_cidade)) # retorna as informações como um dicionario usando o 'vars'

for biblioteca in bibliotecas:
    print(vars(biblioteca))

