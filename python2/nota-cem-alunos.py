#Faça um programa em pascal para ler as notas de 100 alunos e imprimir quantos alunos tiraram nota abaixo da media da turma e quantos tiraram acima ou igual a media.

soma = 0
cont = 0
notas = [0.0]*100
for i in range(0,100):
	nota = float(input("nota: "))
	notas[i] = nota
	soma += notas[i]
media = soma/100
print "media: ", media
for j in range(0,100):
	if notas[j]>media:
		cont += 1	
print "Quantidade: ", cont		
