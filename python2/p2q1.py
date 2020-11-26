#Fazer um programa em Python para ler uma cadeia e imprimir todos os palíndromos maiores do que 3.

#Uma cadeia é palíndromo quando lida de trás para frente e frente para trás for igual

#EX: 1213121

numero = raw_input("Digite numero: ").strip()
numero2 = numero.split()
junto = ''.join(numero2)
inverso = ''
for algarismo in range(len(junto)-1,-1,-1):
  if len(junto)>=3: 
    inverso += junto[algarismo]
    print '',junto,'',inverso

