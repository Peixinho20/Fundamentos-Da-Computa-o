'''
Faça um algoritmo que leia os valores em hora, minuto e segundo e imprima tudo em segundo.
'''
hora = input("Quantas horas: ")
minuto = input("Quantos minutos: ")
segundo = input("Quantos segundos: ")
total = hora*3600 + minuto*60 + segundo
print "Tempo total em segundos: ",total
