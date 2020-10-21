'''
Faça um algoritmo que leia os valores de anos, meses e dias e imprima tudo em dias.
'''

ano = input("Quantos anos: ")
mes = input("Quantos meses: ")
dia = input("Quantos dias: ")
dias = ano*365 + mes*30 + dia
print "Um total de", dias,"dias."
