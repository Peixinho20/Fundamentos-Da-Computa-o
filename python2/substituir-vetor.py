#Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8 últimas posições. Imprima o vetor original e o vetor trocado
	
vetor = []*16
for i in range(0,16):
   vetor.append(raw_input('valor: '))
print '\nOriginal: ',vetor,'\n'

for i in range(0,16):
   if i <= 7:
      aux = vetor[i]
      vetor[i] = vetor[len(vetor)-i-1]
      vetor[len(vetor)-i-1] = aux
print 'Novo: ',vetor	
