# 1. Calculator simplu

# a. Cere două numere de la utilizator (cu input() și int()).

numar1 = int(input("Introdu primul numar= "))
numar2 = int(input("Introdu al doilea numar= "))

# b. Afișează:

print ("Suma= ", numar1 + numar2) # afisare suma
print ("Diferenta= ", numar1 - numar2) #afisare diferenta
print ("Produsul= ",numar1 * numar2) # afisare produsul
print ("Impartire= ", numar1 / numar2) # afisare impartire

# 2. Verificare varsta
# a. Cere varsta utilizatorului
varsta = "Care este varsta ta? ="
varsta_utilizator= int(input(varsta))

# b. Afișează dacă este: major/minor

print (varsta_utilizator > 18)
print (varsta_utilizator < 18)

# nu am inteles exact daca trebuie cum e mai sus sau cum e mai jos

if varsta_utilizator >= 18:
    print("Major")
else:print("minor")

# 3. Compara doua numere
# a. cere numere de la utilizator

numar3 = int(input("primul numar= ")))
numar4 = int(input("al doilea numar= ")))

# b. afiseaza daca sunt egale sau diferite

if numar3 == numar4 and numar3 != numar4:
    print("numerele sunt egale")
else:
    print("numerele sunt diferite")

# 4. verificare numere pare

numar4 = int(input("primul numar= "))
numar5 = int(input("al doilea numar= "))

if numar4 % 2 == 0 and numar5 % 2 == 0:
    print ("numerele sunt pare")
else:
    print ("numerele nu sunt pare")







