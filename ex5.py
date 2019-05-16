

p = int(input('Digite o peso de uma caixa: '))
pt = 0
caixa = 0
while caixa <= 25:
    if p > 0:
        p = int(input('Digite o peso de uma caixa: '))
        pt = (caixa + 1)*(p + 1)
    else:
        print('peso total', pt)        
    dando erro
