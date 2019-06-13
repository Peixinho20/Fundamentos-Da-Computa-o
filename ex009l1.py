'''
Crie um algoritmo que apure os votos de uma eleição municipal, numa cidade com
20.000 eleitores, onde concorreram quatro candidatos. Um servidor da Justiça
Eleitoral digitará cada voto individualmente. Cada voto equivale a um número inteiro.
Os votos válidos podem ser 1, 2, 3 e 4, e estão relacionados aos seguintes candidatos:
1 – João da Silva
2 – José Ramalho
3 – Maria Mattos
4 – Pedro Américo
Votos com o valor 0 devem ser contabilizados como votos em branco, e votos com
qualquer outro valor (além de 0, 1, 2, 3 e 4), devem se considerados votos nulos.
Calcule e escreva o total de votos de cada candidato, o total de votos brancos e o total
de votos nulos.
'''

votosjoao=0
votosjose=0 
votosmaria=0 
votospedro=0 
votosbranco=0
votosnulo=0 
voto='vazio'

while voto!='fim':
  voto=raw_input('Digite o seu voto:')
  if voto=='1':
   votosjoao=votosjoao+1
  if voto=='2':
   votosjose=votosjose+1
  if voto=='3':
   votosmaria=votosmaria+1
  if voto=='4':
   votospedro=votospedro+1
  if voto=='0':
   votosnulo=votosnulo+1
  if voto!='0' and voto!='1' and voto!='2' and voto!='3' and voto!='4': votosbranco=votosbranco+1
  if voto=='fim':
   print('Votos para João da Silva:'),votosjoao
   print('Votos para José Ramalho:'),votosjose
   print('Votos para Maria Mattos:'),votosmaria
   print('Votos para Pedro Américo:'),votospedro
   print('Votos Brancos:'),votosbranco
   print('Votos Nulos:'), votosnulo
  
