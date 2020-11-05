#Faça um programa que leia duas strings e imprima a interseção entre as strings
Ex:   cabelo e pelo => e, l, o

frase1 = raw_input("Digite uma frase: ").lower().strip()
frase2 = raw_input("Digite outra frase: ").lower().strip()
for i in range(len(frase1)):
	for j in range(len(frase2)):
		if frase1[i] == frase2[j]:
		  print "", frase1[i],
