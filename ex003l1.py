'''
Crie um algoritmo que leia uma quantidade não determinada de números inteiros. O
programa deve calcular e escrever a quantidade de números pares e ímpares e a
média aritmética dos números pares. A leitura deve ser encerrada quando for lido o
número zero, que não deve ser considerado.
'''

a = 0
par = 0
impar = 0
media_par = 0
total = 0

a = int(input('entre com um número inteiro:'))
while a > 0:
   if a%2 == 0:
       par = par + 1
       total = total + 1
   else:
       impar = impar + 1
       total = total + 1
   a = int(input('entre com um número inteiro:'))
print('O total de par é', par, 'media de par é', par/total)
print('O total de impar é', impar,'media de impar é', impar/total)
