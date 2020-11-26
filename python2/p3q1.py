mat=[]
for i in range(0,5):
    mat.append(0)
    mat[i] = []
    for j in range(0,4):
        mat[i].append(input('Digite um numero '))

vetSP=[0]*5
for i in range(0,5):
    soma = 0
    for j in range(0,4):
        soma +=mat[i][j]
    vetSP[i] = soma 

vetSC=[0]*4
for i in range(0,4):
    somaC = 0
    for j in range(0,5):
        somaC+=mat[j][i]
    vetSC[i] = somaC

for i in range(0,len(mat)):
    for j in range(0,len(mat[i])):
        print '%3d' % mat[i][j],
    print
print 'Perimetros ', vetSP, '\nSoma Colunas ', vetSC   
