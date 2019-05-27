# Crie um algoritmo que leia a quantidade e o preço de 50 produtos comprados
# por uma empresa. Ao final deve ser escrito o total gasto pela empresa.
quantidade = 0
vpreco = [0.0]*2
preco = 0.0
soma_preco = 0.0

while quantidade < 2:
    for i in range(0,2):
        preco = float(input('Digite o preço do produto: '))
        vpreco[i] = preco
        soma_preco = soma_preco + preco
        quantidade = int(input('Digite a quantidide (em inteiros) de um determinado produto: '))
        quantidade += 1
print('Total gasto: ', soma_preco)
