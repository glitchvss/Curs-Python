# 1. Pozitiv, negativ sau zero

numar = int(input("Introdu un numar = "))

if numar > 0:
    print("Pozitiv")
elif numar == 0:
    print("ZERO")
else:
    print("negativ")

# 2. Compară două numere

nr1 = int(input("introdu primul numar = "))
nr2 = int(input("introdu al doilea numar = "))

if nr1 > nr2:
    print(f" {nr1} este mai mare decat {nr2}")
elif nr2 > nr1:
    print(f"{nr2} este mai mare decat {nr1}")
else:
    print("numerele sunt egale")

# 3. Nota: admis sau respins

nota = float(input("Introdu nota de la bacalureat(foloseste punct in loc de virgula) = "))

if nota > 5:
    print(f"felicitari, cu nota {nota} este ADMIS")
else:
    print(f"imi pare rau, insa cu nota {nota} esti RESPINS")

# 4. acces in club

print("\033[35mBine ai venit la Club SkillBrain")

numar = int(input("\033[mIntrodu varsta ta sa vedem daca te putem accepta = "))

if numar >= 18:
    print(f"\033[32mFelicitari, avand {numar} ani esti binevenit in Club!")
else:
    print(f"\033[31mImi pare rau, la {numar} ani nu ai ce cauta in Club.")

# defect profesional sa ma pierd in detalii, iata ca am facut si date colorate :))

# 5. Nume care începe cu litera A

nume = input("Cum te numesti? = ")

if nume.startswith("A"):
    print(f"Numele {nume} incepe cu \033[35mA.")
else:
    print(f"Cautam doar nume care incep cu litera \033[35mA \033[m, din pacate {nume}, \033[31mnu esti eligibil")

