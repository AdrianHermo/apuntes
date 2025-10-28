# Programa de gestión de películas
# - Lista 'peliculas' para almacenar los nombres de las películas.
# - Muestra un menú con varias opciones y se repite hasta que el usuario elija salir.
# Menú de opciones:
# 1. Añadir película: añade una película a la lista.
# 2. Cambiar película por posición: reemplaza la película que está en la posición indicada.
# 3. Borrar película por posición: elimina la película que está en la posición indicada.
# 4. Mostrar películas: muestra todas las películas ordenadas alfabéticamente.
# 5. Buscar película: verifica si una película existe en la lista.
# 6. Añadir varias películas: permite añadir varias películas de golpe.
# 7. Cambiar película por nombre: busca la película por su nombre y la reemplaza por otra.
# 8. Borrar película por nombre: elimina una película indicando su nombre.
# 9. Contar cuántas películas hay: muestra el número total de películas en la lista.
# - Se practican listas, condicionales, bucles while y for, índices, búsqueda, ordenación y manejo de strings.

peliculas = []

while True:
    print('1. Añadir pelicula')
    print('2. Cambiar pelicula por posicion')
    print('3. Borrar pelicula por posicion')
    print('4. Mostrar peliculas')
    print('5. Buscar pelicula')
    print('6. Añadir varias peliculas')
    print('7. Cambiar pelicula por nombre')
    print('8. Borrar pelicula por nombre')
    print('9. Contar cuantas peliculas hay')

    opcion = int(input('Elige la opción: '))
    if opcion == 1:
        pelicula = input('Añade la pelicula que quieras: ')
        peliculas.append(pelicula)
        print('Pelicula añadida')

    elif opcion == 2:
        print(peliculas)
        posicion = int(input('Introduce la posicon de la pelicula que deseas cambiar: '))
        Nuevapelicula = input('Introduce el nombre de la nueva pelicula: ')
        peliculas[posicion] = Nuevapelicula
        print(peliculas)


    elif opcion == 3:
        posicion = int(input('Elige la posicion de la pelicula que deseas cambiar: '))
        peliculas.pop(posicion)
        print(peliculas)

    elif opcion == 4:
        print(sorted(peliculas))

    elif opcion == 5:
        nombre = input('Introduce el nombre de la pelicula: ')
        if nombre in peliculas:
            print('La pelicula ya esta en la lista')
        else:
            print('La pelicula no esta en la lista')

    elif opcion == 6:
        cantidad = int(input('Cuantas peliculas quieres añadir?: '))
        for i in range(cantidad):
            nueva = int(input('Introduce el nombre de la nueva pelicula: '))
            peliculas.append(nueva)
            print(peliculas)

    elif opcion == 7:
        if peliculas:
            nombre_actual = input("Introduce el nombre de la película a cambiar: ")
            if nombre_actual in peliculas:
                nueva = input("Introduce el nuevo nombre: ")
                indice = peliculas.index(nombre_actual)
                peliculas[indice] = nueva
                print("Película cambiada correctamente.")
            else:
                print("La película no está en la lista.")
        else:
            print("No hay películas para cambiar.")

    elif opcion == 8:
        if peliculas:
            nombre_actual = input('Introduce el nombre de la pelicula a borrar: ')
            if nombre_actual in peliculas:
                peliculas.remove(nombre_actual)
                print('Pelicula eliminada')

    elif opcion == 9:
        print(len(peliculas))
