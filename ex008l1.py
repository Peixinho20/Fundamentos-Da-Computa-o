'''
 Crie um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma
de todos os números múltiplos de 4 compreendidos entre eles. Os valores A e B não
devem ser considerados no somatório. Caso A seja maior do que B deve ser enviada
uma mensagem para o usuário informando que a soma não será realizada.
'''
soma = 0
a = int(input('Digite um inteiro: '))
b = int(input('Digite outro inteiro: '))
if a > b:
    print('A soma não será realizda!')
else:
    for i in range(a+1,b):
        if i%4==0:
            soma += i
print(soma)
