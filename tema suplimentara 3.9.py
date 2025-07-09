nume = input("Nume = ")
varsta = int(input("Cati ani ai? = "))
permis = input("Ai permis? da/nu = ")

if varsta >= 18 and permis == "da":
    print(f"{nume}, poti conduce!")
else:
    print(f"{nume}, nu ai voie sa conduci ")
