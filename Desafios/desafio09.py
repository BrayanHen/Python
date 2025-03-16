c=float(input('Quanto dinheiro voce tem na carteira? R$:'))
d=(c/5.77)
eu=(c/6.26)

print('Com R${} vôce pode comprar US${:.2f} E €{:.2f}'.format(c,d,eu))