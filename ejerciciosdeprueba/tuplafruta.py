frutas_fijas = ('manzana', 'banana','naranja')
frutas_lista = []
while True:

    print('1. Añadir fruta')
    print('2. Cambiar fruta')
    print('3. Borrar fruta')
    print('4. Mostrar frutas')
    print('5. Salir')

    opcion = int(input('Elige la opción: '))



    if opcion == 1:
        fruta = input('Introduce la fruta que quieras: ')
        frutas_lista.append(fruta)
        print('Fruta añadida')

    elif opcion == 2:
        posicion = int(input('Elige la posición que deseas cambiar: '))
        NuevaFruta = input('Introduce la fruta que quieras: ')
        frutas_lista[posicion] = NuevaFruta
        print(frutas_lista)

    elif opcion == 3:
        posicion = int(input('Elige la posición de la fruta que deseas eliminar: '))
        frutas_lista.pop(posicion)
        print('Fruta eliminada')

    elif opcion == 4:
        print(frutas_lista,frutas_fijas)

    elif opcion == 5:
        print('Programa finalizado')
        break

    else:
        print('Opcion no valida')
