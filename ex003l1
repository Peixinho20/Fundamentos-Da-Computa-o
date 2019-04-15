'''
Crie um algoritmo que leia uma quantidade não determinada de números inteiros. O
programa deve calcular e escrever a quantidade de números pares e ímpares e a
média aritmética dos números pares. A leitura deve ser encerrada quando for lido o
número zero, que não deve ser considerado.
'''

n=0; cont_p=0; cont_i=0; media_p=0;
flag=0; #é usado pra que?

n = int(input("Entre com um inteiro: "))

if n!=0:
	flag=1

while flag:
	if n%2==0:
		cont_p +=1 #mais igual (+=)
		media_p +=n
	else:
		cont_i +=1
	
	n = int(input("Entre com um inteiro: "))
	
	if n==0:
		flag=0
	
if cont_p!=0:
	media_p = media_p/cont_p

print 'quantidade de números pares: %d \nQuantidade de números ímpares: %d \n Média de números pares: %d' %(cont_p, cont_i, media_p)
