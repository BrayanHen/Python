def metade(n,show=False):
    resultado=n/2
    return f'R${resultado:.2f}' if show else resultado

def dobro(n,show=False):
    resultado=n*2
    return f'R${resultado:.2f}' if show else resultado

def aumentar(p,n,show=False):
    porcentagem = p * n / 100
    resultado=p+porcentagem
    return f'R${resultado:.2f}' if show else resultado

def diminuir(n,p,show=False):
    porcentagem=n*p/100
    resultado=n-porcentagem
    return f'R${resultado:.2f}' if show else resultado

def moeda(n):
    return f'R${n:.2f}'

