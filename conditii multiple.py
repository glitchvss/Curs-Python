# 1. Verificare vârstă și aptitudini de muncă

#Cere vârsta utilizatorului.

#Verifică dacă este între 18 și 65 de ani (inclusiv).

# Afișează un mesaj corespunzător.

varsta = int(input("care este varsta ta?"))

if varsta >= 18 and  varsta <= 65:
    print(f"ai {varsta} esti apt de munca")
else:
    print("esti minor. stai pe banii parintilor!")