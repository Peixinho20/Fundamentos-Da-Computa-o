#Faca um programa em Python que mostre os N termos da Serie a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + ..... + N/M

#Alem disso, imprimir tambem a soma dos elementos da serie.

#Ex: N = 3

#S = 1 + 2/3 + 3/5

Soma = 2.266666
soma = 0
n = input('Quantos termos voce quer? ')
for c in range(1,n+1):
	s = c/float(2*c-1)
	print s
	soma += s
print 'A soma dos termos vale:', soma  

