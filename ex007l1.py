# Crie um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma de todos os números compreendidos entre
# eles. Os valores A e B não devem ser considerados no somatório. Caso A seja maior do que B deve ser enviada uma mensagem 
# para o usuário informando que a soma não será realizada.
a = int(input('Digite um inteiro positivo: '))
b = int(input('Digite outro inteiro positivo: '))
if a > b:
    print('A soma não será realizada!')    
else:
    for i in range(a+1,b):
        soma += i
print(soma)        
