'''
Uma empresa lançou um novo produto no mercado e fez uma pesquisa para saber se os  consumidores  estavam  satisfeitos,  para  
isso  eles  deveriam  responder  sim ‘S’ou não ‘N’. Crieum algoritmoque  leia  a  resposta  de  todas as pessoas  e  escreva  a 
porcentagem dos que disseram sim e dos que disseram não.Obs: O final da leitura de dados é marcado pela resposta ‘F’
'''

sim = 0
nao = 0
psim = 0
pnao = 0
soma_sim = 0
soma_nao = 0

while sim == 's':
    a = str(input('Está satisfeito com os serviços? (s ou n): '))
    soma_sim = sim + 1
    psim = soma_sim/100
    a = str(input('Está satisfeito com os serviços? (s ou n): '))
while nao == 'n':
    a = str(input('Está satisfeito com os serviços? (s ou n): '))
    soma_nao = nao + 1
    pnao = soma_nao/100
    a = str(input('Está satisfeito com os serviços? (s ou n): '))

print('A porcentagem que disse sim é', psim, '%, e a porcentagem que disse não é', pnao, '%.')    
