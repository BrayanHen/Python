def metade(num):
    res=num/2
    return res

def dobro(num):
    res=num*2
    return res

def aumentar(num,taxa):
    res=num+(num*taxa/100)
    return res

def moeda(num):
    return f'R${num:.2f}'.replace('.',',')
