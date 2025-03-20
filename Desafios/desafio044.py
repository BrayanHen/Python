preco=float(input('Preço do produto:'))
f1=print('1-Á dinheiro/cheque')
f2=print('2-Á vista cartão')
f3=print('3-Até 2x no cartão')
f4=print('4-3x ou mais no cartão')

forma_pagamento=input('Forma de pagamento:')

avista=preco-(preco*10/100)
avistac=preco-(preco*5/100)
p3x=preco+(preco*20/100)

if forma_pagamento == '1':
    print('Voce pagara {} com um  desconto de 10% por pagar á vista!'.format(avista))
elif forma_pagamento == '2':
    print('Voce pagara {} com um desconto de 5% por pagar á vista no cartão!'.format(avistac))
elif forma_pagamento == '3':
    print('Voce não receberá nemhum desconto.')
elif forma_pagamento == '4':
    parcelas=float(input('Em quantas parcelas?:'))
    juros = p3x / parcelas
    print('Voce pagara {:.2f} em {:.0f}x  de {:.2f} com juros!!'.format(preco,parcelas,juros))
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preco,p3x))

