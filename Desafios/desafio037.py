num=int(input('Digite um numero que voce queira converter:'))
print('1 - Converter para BINARIO')
print('2 - Converter para OCTAL')
print(str('3 - Converter para HEXADECIMAL'))
num2=int(input('Escolha qual das opções a cima voce deseja converter:'))

bin=bin(num)
octal=oct(num)
hexadecimal=hex(num)
if num2==1:
    print('O numero {} convertido para binario é:{}'.format(num,bin))
elif num2==2:
    print('O numero {} convertido para octal é:{}).'.format(num,octal))
else:
    print('O numero {} convertido para hexadecimal é:{}'.format(num,hexadecimal))

















#bin para converter numeros int para binario, oct paraconverter para octal e hex para converter para hexadecimal