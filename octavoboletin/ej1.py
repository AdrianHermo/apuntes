# 1.Escribir unha función que reciba unha tupla de elementos e indique si se encontran ordeados de menor
# a maior ou non.


def comparacion_maxmin(listanum):
    if listanum == sorted(listanum,reverse=True):
        return ('Los numeros estan ordenados')
    else:
        return ('Los numeros no estan ordenados')


print(comparacion_maxmin([37, 29, 30, 40, 84, 71, 46, 53, 97, 52]))
print(comparacion_maxmin([29, 30, 37, 40, 46, 52, 53, 71, 84, 97]))
print(comparacion_maxmin([97, 84, 71, 53, 46, 40, 37, 30, 29]))

#sorted lee todo de menor a maior
#y poniendo reverse = true hace lo contrario los ve de maior a menor