'''
Faça um programa que calcule a quantia total dada uma porção de moedas. O programador deve dialogar com o usuário segundo o formato do exemplo abaixo:
Número de moedas de 1 Real:			3
Número de moedas de 50 centavos:		3
Número de moedas de 25 centavos:		1
Número de moedas de 10 centavos:		7
Número de moedas de 5 centavos:	       100
Número de moedas de 1 centavo:	         13
Quantia total calculada: R$ 10.58
'''

um = input("Moedas de 1 real: ")
cinq = input("Moedas de cinquenta centavos: ")
vcinco = input("Moedas de vinte e cinco centavos: ")
dez = input("Moedas de dez centavos: ")
umcent = input("Moedas de um centavo: ")
total = um + 0.5*cinq + 0.25*vcinco + 0.1*dez + 0.01*umcent
print "Total em R$: ", total
