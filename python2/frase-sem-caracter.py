#Faça um programa que leia uma string e um caractere e crie uma outra string sem o caractere lido.

frase = raw_input("Digite uma frase: ")
caracter = raw_input("Escolha um caractere: ")
palavras = frase.split(caracter)
junto = ''.join(palavras)
#print frase
print junto
