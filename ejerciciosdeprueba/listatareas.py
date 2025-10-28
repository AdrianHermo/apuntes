list_tareas=["Matematicas","Lengua","Biologia","Religion"]


def añadir_tarea(lista):
    tarea= input('Dime la tarea :')
    lista.append(tarea)
    print(lista)

def tarea_completada(lista):
    terminada = str(input("Que tarea has terminado : "))
    if terminada in lista:
        lista.remove(terminada)

def enseñar_tarea(lista):
    print("tus tareas son :")
    for tarea in lista:
        print(tarea)



def menu():
    while True:
        print(
            '''Opciones:
            1 Añadir tarea
            2 Tarea terminada
            3 mostrar tareas
            4 salir ''')
        opcion = int(input("Elije la opcion: "))
        if opcion == 1:
            añadir_tarea(list_tareas)
        elif opcion == 2:
              tarea_completada(list_tareas)
        elif opcion == 3:
            enseñar_tarea(list_tareas)
        elif opcion == 4:
            break
menu()






