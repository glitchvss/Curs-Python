import random

scor_utilizator = 0
scor_calculator = 0

while True:
    alegere = input("Alegi 'par' sau 'impar'? ").lower()
    numar_tu = int(input("Alege un număr între 0 și 10: "))
    numar_pc = random.randint(0, 10)

    suma = numar_tu + numar_pc
    print(f"Tu ai ales: {numar_tu}, calculatorul: {numar_pc}. Suma este {suma}.")

    if suma % 2 == 0:
        rezultat = 'par'
    else:
        rezultat = 'impar'

    print(f"Suma este {rezultat}.")

    if alegere == rezultat:
        print("Felicitari, runda e a ta")
        scor_utilizator += 1
    else:
        print("Nasol, calculatorul a castigat")
        scor_calculator += 1

    din_nou = input("Vrei să joci din nou? (da/nu): ").lower()
    if din_nou != 'da':
        break

print(f"\nScor final: Tu - {scor_utilizator}, Calculatorul - {scor_calculator}")