'''
Elabore um algoritmo que calcule e imprima a média de um aluno em uma disciplina com as seguintes características: Duas provas (P1 e P2), um trabalho (T) e 5 listas de exercícios (L1..L5). A média será dada por: média = 0,3xP1 + 0,4xP2 + 0,2x(média das listas) + 0,1xT.
'''
p1 = input('Insira a nota da P1: ')
p2 = input('Insira a nota da P2: ')
l1 = input('Insira a nota do L1: ')
l2 = input('Insira a nota do L2: ')
l3 = input('Insira a nota do L3: ')
l4 = input('Insira a nota do L4: ')
l5 = input('Insira a nota do L5: ')
t = input('Insira a nota do T: ')
L = (l1 + l2 + l3 + l4 + l5)/float(5)
media = (0.3*p1 + 0.4*p2 + 0.2*L + 0.1*t)/ float(4)
print "media: ", media
