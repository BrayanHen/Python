frase=str(input('Digite uma frase:').upper().strip())
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]

if inverso==junto:
     print('É um palindromo!')
else:
     print('Não é um palindromo')



