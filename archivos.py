file = open('alumnos.txt','r')
nombres = file.readlines()
print(nombres)
file.close()

"""for item in nombres:
    print(item, end='')"""

# readline obtiene el primer elemento
# readlines obtiene todos los elementos