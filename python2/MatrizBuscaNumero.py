#Leia uma matriz 4x4 e um valor X, procure a primeira vez que esse valor aparece na matriz imprimindo sua linha e coluna. Caso não exista o elemento, imprima uma mensagem de erro.

mat=[]
for i in range(0,4):
    mat.append(0)
    mat[i]=[]
    for j in range(0,4):
        mat[i].append(input('Numero '))
x=input('Buscar Numero ')
achou=False
for i in range(0,4):
    for j in range(0,4):
        if mat[i][j]==x:
            linha=i+1
            coluna=j+1
            achou=True
            break
for i in range(0,4):
    for j in range (0,4):
        print "%3d" % mat[i][j],
    print    
if achou:
    print'Numero encontrado na linha',linha,'coluna',coluna
else:
    print'Erro! Numero nao encontrado!'

