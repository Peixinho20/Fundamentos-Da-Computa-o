'''
Elabore um algoritmo que implemente uma calculadora com as operações de soma, subtração, multiplicação e divisão. O algoritmo deve ler os operadores e a operação a ser realizada e mostrar o resultado. Seu algoritmo deve considerar o caso em que o usuário tente dividir um número por zero.
'''
x = input("Digite um valor: ")
y = input("Outro valor: ")
print "\nO que quer fazer com esses valores? \nSomar: [1] \nSubtrair: [2] \nMultiplicar: [3] \nDividir: [4]"
escolha = input("\nDigite sua escolha: ")
if escolha == 1:
  r = x+y
  print 'A soma vale', r
else:  
  if escolha == 2:
    r = x-y
    print 'A diferenca vale', r
  else:  
    if escolha == 3:
      r = x*y
      print 'O produto vale', r 
    else:     
      if escolha == 4:
        if y == 0:
          print 'ERRO: Nao posso dividir por zero'
        else:
          r = x/float(y)
          print 'A divisao vale', r
print '\nFim do programa, volte sempre!' 
