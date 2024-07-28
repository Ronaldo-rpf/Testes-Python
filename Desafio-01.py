A = int(input("Valor do início do intervalo (valores não negativos): "))
B = int(input("Valor do final do intervalo (valores não negativos): "))
if A < 0 or B < 0 or A > B:
    print("Valor inválido")

soma = 0

for i in range(A, B+1):
    if i%5 == 0:
        soma += i

print(f"A soma dos valores divisíveis por cinco nesse intervalo é {soma}")