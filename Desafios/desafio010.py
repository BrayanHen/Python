l=int(input('Largura da parede:'))
a=int(input('Altura da parede:'))
area=l*a
lt=area/2
#2m²=1lt de tinta#

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, voce precisara de {}l de tinta.'.format(l,a,area,lt))