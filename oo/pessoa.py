class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    jose = Pessoa(nome='Jose')
    luiz = Pessoa(jose, nome='Luiz')
    print(Pessoa.cumprimentar(luiz))
    print(id(luiz))
    print(luiz.cumprimentar())
    print(luiz.nome)
    print(luiz.idade)
    for filho in luiz.filhos:
        print(filho.nome)
