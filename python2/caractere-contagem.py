#Faca um programa que leia uma string e um caractere e diga quantas vezes o caractere aparece na string

cad = raw_input('Entre com uma cadeia: ')
caracter = raw_input('Escolha um caractere: ')
print 'O caractere', caracter, 'aparece',cad.count(caracter),'vezes'
