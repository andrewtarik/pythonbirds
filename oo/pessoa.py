class Pessoa:
    def __init__(self, *filhos, nome=None,idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    andrew = Pessoa(nome='Andrew')
    procopio = Pessoa(andrew,nome='Procopio')
    print(Pessoa.cumprimentar(procopio))
    print(id(procopio))
    print(procopio.cumprimentar())
    print(procopio.nome)
    print(procopio.idade)
    for filho in procopio.filhos:
        print(filho.nome)
