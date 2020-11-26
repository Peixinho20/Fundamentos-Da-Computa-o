frase = raw_input('Diga a frase ')
palavra = ''
vet = []
for i in range(0,len(frase)):
    if frase[i] != ' ':
        palavra = palavra + frase[i]
    else:
        if palavra != '': 
            vet.append(palavra)
            palavra = ''
vet.append(palavra)

for i in range(0,len(vet)-1):
    for j in range(i+1,len(vet)):
        if vet[i]>vet[j]:
            aux = vet[i]
            vet[i] = vet[j]
            vet[j]= aux

print 'Ordem das palavras ', vet
