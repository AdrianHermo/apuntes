DNI = int(input('Introdece tu DNI: '))
l = 'TRWAGMYFPDXBNJZSQVHLCKE'
letra= l[DNI % 23]
print(letra)