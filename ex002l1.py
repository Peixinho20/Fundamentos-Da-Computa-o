'''
Crie um algoritmo que escreva os N primeiros termos de uma progressão aritmética 
(PA). O primeiro termo e a razão da PA devem ser informados pelo usuário.
'''
a1 = int(input('entre com o valor de a1: '))
n = int(input('entre com o valor de n: '))
r = int(input('entre com o valor da razao r: '))
an = a1 + (n - 1)*r
print('O valor de an é ', an)
