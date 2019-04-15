#Lista 1. ex001

entrardados='sim'
conthomens=0
contmulheres=0
salariohomens=0
salariomulheres=0
maiorsalario=0
while entrardados=='sim':
  idade=input('Digite a idade')
  sexo=input('Digite o sexo M ou F:')
  salario=input('Digite o salario:')
  if salario>=maiorsalario:
    if idade<30:
     maiorsalario=salario
  if sexo=='m':
   conthomens=conthomens+1
   salariohomens=salariohomens+salario
  if sexo=='f':
    contmulheres=contmulheres+1
    salariomulheres=salariomulheres+salario
  entrardados=input('Deseja adicionar dados? Sim ou nao:')
  if entrardados=='nao':
    if conthomens==0:
      conthomens=1
    if contmulheres==0:
      contmulheres=1
    print('A media salarial dos homens desta pesquisa é:'), salariohomens/conthomens
    print('A media salarial das mulheres desta pesquisa é:'), salariomulheres/contmulheres
    print('O maior salario entre pessoas com menos de 30 anos é:'), maiorsalario
    
