from datetime import date
totmaior=0
totmenor=0
for c in range(1,8):
    ano: int=int(input('Digite o ano de nascimento da {}ᵃ pessoa:'.format(c)))
    idade = date.today().year - ano
    if idade > 18:
       totmaior += 1
    else:
        totmenor +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))

