#Leia uma frase e imprima as suas palavras.

frase=raw_input('Digitar Frase ')
espaco=''
for i in range(0,len(frase)):
    if frase[i]==' ':
        print espaco
        espaco=''
    else:
        espaco=espaco+frase[i]
print espaco
