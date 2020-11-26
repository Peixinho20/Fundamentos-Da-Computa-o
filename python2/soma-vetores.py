#Leia dois vetores de 10 posições cada. Armazene em um vetor de 20 posições os elementos do vetor 1 depois os elementos do vetor 2. No final imprima os três vetores. 

vet1 = []*3
for i in range(0,3):
	vet1.append(input('Digite um valor: '))

vet2 = []*3
for j in range(0,3):
	vet2.append(input('Digite outro valor: '))
	
for k in range(0,6):
	vet3 = vet1 + vet2
print 'Vetor 1: ', vet1, '\nVetor 2: ', vet2, '\nVetor 3: ', vet3

