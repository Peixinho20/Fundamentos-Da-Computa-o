#Considere um vetor de trajetórias de 9 elementos onde cada elemento possui o valor do próximo elemento a ser lido.
#Indice: 1  2  3  4  5  6  7  8  9   
#Valor:  5  7  6  9  2  8  4  0  3
#Fazer um programa que leia esse vetor e imprima a trajetória correta: sequência de impressão 5, 2, 7, 4, 9, 3, 6, 8, 0  

vetor = [-1,5,7,6,9,2,8,4,0,3] #pq e o inice zero e não vou usar
indice =1 
for i in range(0,9):
	print vetor[indice],
	indice = vetor[indice]
	
