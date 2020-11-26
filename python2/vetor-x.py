#Ler um vetor de números inteiros de 30 posições. Depois, ler um número inteiro X, imprimir quantas vezes o número X aparece no vetor. Q5

vet = []*30
for i in range(0,30):
	vet.append(input('Digite um valor: '))

soma = 0
x = input('Qual numero que encontrar: ')
for i in range(len(vet)):
    if vet[i]==x:
        soma += 1
print soma
