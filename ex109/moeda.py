def metade(num,formato=False):
    res=num/2
    return res if formato is False else moeda(res)

def dobro(num,formato=False):
    res=num*2
    return res if formato is False else moeda(res)

def aumentar(num,taxa, formato=False):
    res=num+(num*taxa/100)
    return res if formato is False else moeda(res)

def moeda(num):
    return f'R${num:.2f}'.replace('.',',')
