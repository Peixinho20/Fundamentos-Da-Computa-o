#Aula2 - SELECAO E REPETICAO

'''
Comando de seleção simples em python

sintaxe do comando de seleção simples

if = Condição

 exemplo:
    if a > b
        print a
    else:
        print b
'''
#Fazer um programa que leia um número inteiro e diga se ele é Ímpar
'''
n = int(input('n:'))
if n%2==1:
    print('Ímpar',n)
'''

#Fazer um programa para ler duas notas e imprimir a sua situação de acordo
#com os critérios da uerj.

a = float(input('Digite a nota da p1:'))
b = float(input('Digite a nota da p2:'))
c = (a + b)/2
if c >= 7:
    print(c,'Aprovado')
if c >= 4:
    print(c,'Prova final')
else:
    print(c,'Reprovado por nota')


#Fazer um algoritmo para ler a idade de uma pessoas e imprimir sua situação
#de acordo com os critérios abaixo:
'''
idade <=0 Erro
1 <= idade <=3 Bebe
4 <= idade <= 11 Criança
12 <= idade <= 17 --> Adolescente
18 <= idade <= 30 --> Jovem
31 <= idade <= 64 --> Adulto
idade >= 65 --> Senior

idade = int(input('Digite sua idade:'))
if idade <0:
    print('Erro', idade)
else:
    if idade <=3:
        print('Bebe de', idade, 'anos')
    else:
        if idade <= 11:
            print('Criança de', idade, 'anos')
        else:
            if idade <= 17:
                print('Adolescente de', idade, 'anos')
            else:
                if idade <= 30:
                    print('Jovem de', idade, 'anos')
                else:
                    if idade <= 64:
                        print('Adulto de', idade, 'anos')
                    else:
                        print('Senior de', idade, 'anos')

'''
#Debugger mostra tudo o que está acontecendo no código

#Fazer um algoritimo para ler o peso de oito bolas. Assumindo que todas tem
# o mesmo peso e apenas uma tenha peso diferente, imprimir a bola de peso
# diferente.
'''

b1 = int(input('b1:'))
b2 = int(input('b2:'))
b3 = int(input('b3:'))
b4 = int(input('b4:'))
b5 = int(input('b5:'))
b6 = int(input('b6:'))
#b7 = int(input('b7:'))
#b8 = int(input('b8:'))

#FUNCIONANDO, FALTA INCLUIR AS OUTRAS BOLAS

#Para três bolas:
'''
if b1 == b2:
    print ( ' b3: ' , b3)
elif b1 == b3: #b1 e b3 são iguais
    print ( ' b2: ' , b2)
else: #b2 e b3 são iguais
    print ( ' b1: ' , b1)

'''

#Para qutro ou cinco bolas:
'''
if b1 == b2:# b1 e b2 são iguais
    if b3 != b2:
        print('b3:',b3)
    else:# b1, b2 e b3 são iguais
        print('b4:',b4)
# se nenhuma das condiçoes acima forem atendidas, ele executará o bloco de baixo
if b3 == b4:
    if b2 != b4:
        print('b2:',b2)
    else:# b2 e b3 são iguais
        print('b1:',b1)    
else:
    print('b5:',b5)
# até b5 essa estrutura funciona
'''

#Para seis bolas:
'''
if b1 + b2 == b3 + b4:
    if b6 != b1:  # sem essa segunda condição, ele imprimirá mais de uma resposta
        print('b6:', b6)
    else:
        print('b5:', b5)
    if b1 == b2:
        print('b4:', b4)
    else:
        print('b3:', b3)
    if b2 != b1:
        print('b2:', b2)
else:
    print('b1:',b1)
'''

#Para oito bolas
#INCOMPLETO

if b1 + b3 + b5 == b2 + b4 + b6:
    if b8 != b1:
        print('b8:', b8)
    else:
        print ('b7', b7)
if b1 + b3 == b2 + b4:
    if b6 != b1:
        print('b6:', b6)
    else:
        print('b5:', b5)
if b1 == b2:
    print('b4:', b4)
else:
    print('b3:', b3)
if b2 != b1:
    print('b2:', b2)
else:
    print('b1', b1)
    
    
#While
'''
SINTAXE:
while CONDIÇÃO:
 COMANDOS
'''

'''
Fazer um programa em PYTHON para ler o nome, sexo e duas notas dos alunos de uma turma até que seja digitado o nome FIM.
Imprimir a média pessoal APENAS das alunas. Imprimir também a média aritmética dos homens.
'''

cont = 0
soma = 0
nome = raw_input('nome: ')
while nome != 'fim':
 sexo = str(input('sexo: '))  
 n1 = input('n1: ')
 n2 = input('n2: ')
 mediaPessoal = (n1+n2)/2
 if sexo == 'f':
  print 'media f:', mediaPessoal
 else:
  cont += 1
  soma = soma + mediaPessoal
 nome = str(input('nome: '))
print 'media homens: ', soma/(cont)

#Faça um programa que mostre os números ENTRE 100 e 200 que divididos por 7 dão resto 4.

num = 101
while num < 200:
 if num % 7 == 4:
  print ' ', num
 num += 1

'''
Comando for
• Quando queremos percorrer os ITENS ou ELEMENTOS de uma lista OU quando sabemos a quantidade de repetições a ser executada
podemos utilizar o for.
SINTAXE:
for variavel in objeto_sequencial:
  Comando1
  ...
  Comando n
'''
