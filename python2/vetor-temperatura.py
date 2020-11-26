#Faça um programa para ler 50 valores de temperaturas em graus Celsius. Transformar essas temperaturas em Farenheit e imprimir a media das temperaturas em Celsius e Farenheit e quantas temperaturas ficaram acima da media em Farenheit.

vet=[]
vet2=[]
soma=0
soma2=0
cont=0
cont2=0
cont3=0
for i in range(0,50):
    c=input('Digite a temperatura em ºC: ')
    soma=soma+c
    cont=cont+1
    vet.append(c)
    f=1.8*c+32
    soma2=soma2+f
    cont2=cont2+1
    vet2.append(f)
print'Temperatura em ºC:',vet
print'Temperatura em ºF:',vet2
media=soma/float(cont)
media2=soma2/float(cont2)
for i in range(0,50):
    if vet2[i]>media2:
        cont3=cont3+1
print'Media em ºC:',media
print'Media em ºF:',media2
print'Temperaturas acima da media em ºF: ',cont3	 
