peso=float(input('Digite o peso em KG para calculo de IMC:'))
altura=float(input('Digite a altura para calculo de IMC:'))

imc=peso/(altura*altura)
print('Seu IMC é:{:.1f}'.format(imc))

if imc<18.5:
    print('Abaixo do peso')
elif imc>=18.5 and imc<25:
    print('Peso ideal')
elif imc>=25 and imc<30:
    print('Sobrepeso')
elif imc>=30 and imc<40:
    print('Obesso')
elif imc>40:
    print('Obesidade Morbida')


#imc == peso /(altura*altura)
#imc == indice de massa corporea
