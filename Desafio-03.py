veículos = int(input("Quantidade de veículos: "))
rodas = int(input("Quantidade de rodas no total: "))

if veículos * 4 == rodas or veículos * 4 == rodas - 2:
    carros = rodas / 4
    motos = rodas % 4

if veículos*4 > rodas:
    motos = (4*veículos - rodas) / 2
    carros = veículos - motos

if carros < 0 or motos < 0:
    print ("Valores inválidos.\n")
    quit()

print (f"Carros: {carros} \nMotos: {motos}\n")
