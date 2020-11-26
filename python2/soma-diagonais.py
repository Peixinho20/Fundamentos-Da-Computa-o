#Leia uma matriz 3x3 e imprima a soma dos elementos da diagonal principal e a soma dos elementos da diagonal secundária.

mat=[]
soma=0
soma2=0
for i in range(0,3):
    mat.append(0)
    mat[i]=[]
    for j in range(0,3):
        mat[i].append(input('Numero '))
for i in range(0,3):
    for j in range(0,3):
        if i==j:
            soma=soma+mat[i][i]
            soma2=soma2+mat[i][3-i-1]
for i in range(0,3):
    for j in range (0,3):
        print "%3d" % mat[i][j],
    print    
print'Soma da diagonal principal ',soma,'\nSoma da diagonal secundaria ',soma2 

