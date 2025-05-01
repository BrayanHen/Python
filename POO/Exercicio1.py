class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

pessoa1=Pessoa('Brayan',17)
pessoa1.apresentar()

pessoa2=Pessoa('Laura',18)
pessoa2.apresentar()