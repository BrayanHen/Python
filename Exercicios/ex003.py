dado=input('Digite algo:')

print('O tipo primitivo desse valor é',type(dado))
print('Só tem espaços?',dado.isspace())
print('É alfabético?',dado.isalpha())
print('É alfanumerico?',dado.isalnum())
print('Esta em maisculas?',dado.isupper())
print('Está em minusculas?',dado.islower())
print('Esta capitalizada?',dado.istitle())