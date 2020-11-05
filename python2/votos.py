'''
Faça um programa que leia o número de eleitores de um município, o número de votos brancos, nulos e validos. Calcule e escreva o percentual que cada um representa em relação ao total de eleitores.
'''

total = valido = branco = nulo  = 0
print "Apuracao dos votos: \nValidos: [1] \nBranco: [2] \nNulo: [3] \nParar: [0]"
escolha = input("Digite sua escolha: ")
while escolha != 0:
  print "\nApuracao dos votos: \nValidos: [1] \nBranco: [2] \nNulo: [3] \nParar: [0]"
  escolha = input("Digite sua escolha: ")  
  if escolha == 1:
    valido += 1
  elif escolha == 2:
    branco += 1  
  elif escolha == 3:
    nulo += 1   
total = valido + branco + nulo
print total
