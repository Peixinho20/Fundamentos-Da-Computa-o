'''
4. Faça um algoritmo que leia o preço de um produto, calcule o seu aumento e mostre a sua classificação.
•	Se o preço for menor ou igual a 50, o produto receberá um aumento de 5% 		
•	Se o preço for maior do que 50 e menor ou igual a 100, o aumento será de 10% 
•	Se o preço for maior do que 100, o aumento será de 15%

A classificação do produto deve ser:	
Barato: até 80 reais (inclusive) 
Normal: entre 80 reais e 120 reais (inclusive) 
Caro: entre 120 reais e 200 reais (inclusive) 
Muito Caro: maior do que 200 reais
'''
preco = input("Digite o valor do produto: ")
if preco <= 50:
  Npreco = preco + (preco*5)/100
  print Npreco  
else:
  if 50 < preco <= 100:
    Npreco = preco + (preco*10)/100
    print Npreco
  else:
    Npreco = preco + (preco*15)/100
    print Npreco 
if Npreco <= 80:
  print 'Barato'   
else:
  if 80 < Npreco <= 120:
    print 'Normal'
  else: 
    if 120 < Npreco <= 200:
      print 'Caro'
    else: 
      print 'Muito Caro'  

