'''
Crie um algoritmo que imprima o peso total que será carregado por um caminhão.
Sabe-se que este caminhão carrega 25 caixas. O peso de cada caixa deve ser informado
pelo usuário.
'''

pt = 0
caixa = 0
peso = 0
peso = float(input('Digite o peso de uma caixa em kg: '))
while caixa <= 25:
    caixa = caixa + 1
    pt = pt + peso
    peso = float(input('Digite o peso de mais uma caixa: '))
    if peso == 0.0:
        break #interrompe o while
print('O peso total é', pt, 'kg.')
