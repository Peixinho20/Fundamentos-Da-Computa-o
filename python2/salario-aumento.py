'''
Faça um algoritmo que receba o salário de um funcionário, calcule e mostre o novo salário,
 sabendo-se que este sofreu um aumento de 25%.
'''
salario = input("Digite seu salario: ")
novoSalario = (salario + (salario*25)/float(100))
print "Novo Salario: ", novoSalario
