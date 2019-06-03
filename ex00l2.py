import random
soma1 = 0
soma2 = 0
print('a carta do jogador é:')
for jogador in range(0,1):
    jogadar = random.randint(1,10)
    print(jogadar)
    soma1 +=jogadar

print('a carta do banca é:')
for banca in range(0,1):
    banca = random.randint(1,10)
    print(banca)
    soma2 += banca
    
resposta = input('O jogador deseja receber mais cartas (se não, é a vez da banca)? ')

if resposta == 'sim':
    while resposta == 'sim':
        for jogador in range(0,1):
            jogador = random.randint(1,10)
            print (jogador)
            soma1 +=jogador
            resposta = input('Deseja receber mais? Se não, é a vez da banca. ')

if resposta == 'sim':
    while soma2 <= 18:
        for banca in range(0,1):
            banca = random.randint(1,10)
            print(banca)
            soma2 += banca
                
print('A soma do jogador é', soma1)
print('A soma da banca é', soma2)

'''
Incompleto!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
não consigo fazer a banca jogar, o código q eu montei pra ela não é executada
'''
