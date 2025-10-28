nome1 = input("Nome da primeira persoa: ")
peso1 = float(input("Peso de " + nome1 + ": "))

nome2 = input("Nome da segunda persoa: ")
peso2 = float(input("Peso de " + nome2 + ": "))

if peso1 > peso2:
    print(nome1, "pesa máis que", nome2)
    print("Diferenza de peso:", peso1 - peso2, "kg")
elif peso2 > peso1:
    print(nome2, "pesa máis que", nome1)
    print("Diferenza de peso:", peso2 - peso1, "kg")
else:
    print("Pesan o mesmo.")
