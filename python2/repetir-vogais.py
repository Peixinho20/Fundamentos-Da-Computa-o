#Faça um programa que leia uma string e crie uma outra string repetindo apenas as  vogais
#Ex:  carro => caarroo

frase = raw_input("Digite uma frase: ")
nova = ''
for vogal in range(len(frase)):
	if frase[vogal]=='a' or frase[vogal]=='e' or frase[vogal]=='i' or frase[vogal]=='o' or frase[vogal]=='u':
		nova += frase[vogal]*2
	else:
		nova += frase[vogal]
print nova


