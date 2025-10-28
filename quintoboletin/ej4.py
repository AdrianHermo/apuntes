Numero1 = int(input('Introduce el primer numero: '))
Numero2 = int(input('Introduce el segundo numero: '))
for i in range(Numero1 + 1, Numero2):
    if i %2 == 0:
        print(i)