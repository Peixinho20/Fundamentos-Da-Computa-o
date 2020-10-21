'''
Um funcionário recebe um salário fixo mais 4% de comissão sobre as suas vendas. Faça um algoritmo que receba o valor do salário fixo do funcionário, o valor das suas vendas e que calcule e mostre o salário final do funcionário.
'''
salario = input("Entre com seu salario: ")
vendas = input("Entre com a quantidade de vendas: ")
total = salario + vendas*0.04
print "O seu salario final é R$", total
