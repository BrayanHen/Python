# Desafio 77 - Contagem de vogais

palavras = ('aprender', 'programar', 'python', 'curso')
for palavra in palavras:
    vogais = [letra for letra in palavra if letra in 'aeiou']
    print(f"Na palavra {palavra.upper()} temos {', '.join(vogais)}")
