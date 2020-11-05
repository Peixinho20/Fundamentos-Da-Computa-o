#Faça um programa que leia uma string e crie uma outra string repetindo os caracteres
#Ex:  carro => ccaarrrroo

frase = raw_input("Digite uma frase: ")
nova = ''
for letra in range(len(frase)):
  nova += frase[letra]*2
print nova
