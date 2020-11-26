#Crie uma matriz 5x5 com 1 na diagonal principal e 0 nas outras posições. Imprima a matriz.

mat=[]
for i in range(0,5):
    mat.append(0)
    mat[i]=[]
    for j in range(0,5):
        if i==j:
            mat[i].append(1)
        else:
            mat[i].append(0)
for i in range(0,5):
    for j in range (0,5):
        print "%3d" % mat[i][j],
    print    
