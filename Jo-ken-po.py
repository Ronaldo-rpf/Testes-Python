A = int(input("Jogador A (0: pedra, 1: papel, 2: tesoura) = "))
B = int(input("Jogador B = "))

if A > 2 or A < 0:
    print("Número inválido...")
elif B > 2 or B < 0:
    print ("Número inválido...")
elif A == 0 and B == 0:
    print ("Empate")
elif A == 1 and B == 1:
    print ("Empate")
elif A == 2 and B == 2:
    print ("Empate")
elif A == 0 and B == 1:
    print ("Vitória do B")
elif A == 0 and B == 2:
    print ("Vitória do A")
elif A == 1 and B == 0:
    print ("Vitória do A")
elif A == 1 and B == 2:
    print ("Vitória do B")
elif A == 2 and B == 0:
    print ("Vitória do B")
else:
    print ("Vitória do A")
