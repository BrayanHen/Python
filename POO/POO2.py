class Cliente:
    def __init__(self, nome, email,plano):
        self.nome=nome
        self.email=email
        self.lista_de_planos=['basic','premium']
        if plano  not in self.lista_de_planos:
            print('Plano invalido')
        else:
            self.plano=plano

    def mudar_plano(self,novo_plano):
        if novo_plano in self.lista_de_planos:
            self.plano=novo_plano
        else:
            print('Plano invalido')

    def ver_filme(self, filme,plano_filme):
        if plano_filme not in self.lista_de_planos:
            print('Plano invalido')
        if self.plano == 'basic' and plano_filme == 'premium':
            print('Faça um upgrade para ver esse filme!')
        if self.plano == 'premium':
            print(f'Ver filme {filme} com plano {plano_filme}!')


cliente1= Cliente('Brayan','rabittococada@gmail.com','basic')
print(cliente1.plano)
cliente1.ver_filme('Vingadores','premium')

cliente1.mudar_plano('premium')
print(cliente1.plano)
cliente1.ver_filme('Vingadores','premium')
