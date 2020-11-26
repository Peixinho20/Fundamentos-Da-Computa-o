# Faça um programa em python que leia uma cadeia e crie uma outra cadeia invertendo apenas os caracteres de ÍNDICE ÍMPAR.
#Ex1:             BRASIL
#Resposta:    BLASIR
#Ex2:            CARRO
#Resposta:   CRRAO
#No final imprimir a cadeia original e a cadeia invertida
#Importante: Só pode enviar a questão uma única vez
#Não usar acento nem cedilha

frase = raw_input('Diga a cadeia: ')
impar = ''
for i in range(0,len(frase)):
    if len(frase)%2==0:
        if i%2 == 0:
            impar = impar+frase[i]
        else:
            impar = impar+frase[len(frase)-i]
    else:
        if i%2 == 0:
            impar = impar+frase[i]
        else:
            impar = impar+frase[len(frase)-i-1]
print 'Original: ',frase,'\nInvertidos:', impar
