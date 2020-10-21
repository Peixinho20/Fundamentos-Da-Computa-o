'''
Faça um programa que, dados pelo usuário dois números inteiros m e n, com m > n, escreve os valores de uma tripla Pitagórica (lado1, lado2 e hipotenusa) gerada a partir de m e n, através das 3 fórmulas:
Lado1 = m2 – n2                 Lado2 = 2mn                      Hipotenusa = m2 + n2
'''

m = input("Digite o valor de m:")
n = input("Digite o valor de n:")
l1 = m - n
l2 = m*n
hip = m + n
print "Lado 1:",l1," Lado 2:",l2," Hipotenusa:",hip
