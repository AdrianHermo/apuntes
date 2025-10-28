def encaixan(ficha1, ficha2):
    """
    Comproba se dúas fichas de dominó encaixan.

    Parámetros:
        ficha1 (tuple): Primeira ficha, por exemplo (3, 4)
        ficha2 (tuple): Segunda ficha, por exemplo (5, 4)

    Retorna:
        bool: True se encaixan, False se non encaixan
    """

    # Comprobamos se algún dos valores da primeira ficha está presente na segunda
    if ficha1[0] in ficha2 or ficha1[1] in ficha2:
        # Se teñen un número igual, devolvemos True
        return True
    else:
        # Se non teñen ningún número igual, devolvemos False
        return False


# ---- PROBAS ----

print(encaixan((3, 4), (5, 4)))  # True → comparten o número 4
print(encaixan((2, 6), (5, 1)))  # False → non teñen ningún número igual
print(encaixan((6, 6), (6, 3)))  # True → comparten o número 6
print(encaixan((1, 2), (2, 1)))  # True → comparten o número 2
