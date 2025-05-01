class Vendedor():
    def __init__(self,nome):
        self.nome = nome
        self.vendas=0

    def vendeu(self,vendas):
        self.vendas = vendas

    def bateuMeta(self, meta):
        if self.vendas >= meta:
            print(f'{self.nome} bateu a méta')
        else:
            print(f'{self.nome} não bateu a meta')

vendedor1=Vendedor('Brayan')
vendedor1.vendeu(100)
vendedor1.bateuMeta(500)

vendedor2=Vendedor('Laura')
vendedor2.vendeu(1000)
vendedor2.bateuMeta(1500)