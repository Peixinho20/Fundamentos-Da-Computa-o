#Ler um vetor de 12 posições inteiras e depois ler dois números X e Y de 1 a 12. Imprimir  soma das posições X e Y do vetor.

vet=[]
for i in range(0,12):
    vet.append(input('Numero '))
print vet
x=input('Digitar valor X ')
y=input('Digitar valor Y ')
soma=vet[x]+vet[y]
print'Soma dos numeros na posiçao ',x,'e',y,' ',soma
