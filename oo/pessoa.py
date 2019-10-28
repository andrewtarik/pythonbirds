class Pessoa:
    def __init__(self, *filhos, nome=None,idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    andrew = Pessoa(nome='Andrew')
    waschington = Pessoa(andrew, nome='Waschington')
    print(Pessoa.cumprimentar(waschington))
    print(id(waschington))
    print(waschington.cumprimentar())
    print(waschington.nome)
    print(waschington.idade)
    for filho in waschington.filhos:
        print(filho.nome)
    waschington.sobrenome = 'Procopio'
    del waschington.filhos
    print(waschington.__dict__)
    print(andrew.__dict__)
