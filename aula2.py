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
b7 = int(input('b7:'))
b8 = int(input('b8:'))
(interrompido)
'''
b1 = int(input('b1:'))
b2 = int(input('b2:'))
b3 = int(input('b3:'))
#b4 = int(input('b4:'))
#b5 = int(input('b5:'))
#b6 = int(input('b6:'))
#b7 = int(input('b7:'))
#b8 = int(input('b8:'))

#FUNCIONANDO, FALTA INCLUIR AS OUTRAS BOLAS
if b1 == b2:
    print('b3:',b3)
elif b1 == b3: #b1 e b3 são iguais
    print('b2:',b2)
else: #b2 e b3 são iguais4
    print('b1:',b1)
