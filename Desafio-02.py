soma = 0
qntd = 0
maior = 0
menor = 1000
soma_pares = 0
qntdPares = 0
qntdImpar = 0

num = int(input("Número inteiro: "))
while num >= 0:
    soma += num
    qntd += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if num%2 == 0:
        soma_pares += num
        qntdPares += 1
    if num%2 == 1:
        qntdImpar += 1
    num = int(input("Número inteiro (negativo para parar): "))

media = soma / qntd
media_pares = soma_pares / qntdPares
porc = (qntdImpar / qntd) * 100

print (f"Soma = {soma} \nQuantidade = {qntd} \nMédia = {media} \nMaior número = {maior} \nMenor número = {menor} \nMédia dos pares = {media_pares} \nPorcentagem dos ímpares = {porc}%\n")