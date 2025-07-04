# tema suplimentara de tip calculator
numar1 = int(input("Primul numar="))
numar2 = int(input("Al doilea numar="))

op = input("Introdu operatia (+, -, *, /,): ")

if  op == '+':
    print(numar1 + numar2)
elif op == '-':
    print(numar1 - numar2)
elif op == '*':
     print(numar1 * numar2)
elif op == '/':
    if  numar2 != 0:
        print(numar1 / numar2)
