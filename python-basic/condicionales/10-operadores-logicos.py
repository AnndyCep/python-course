""" Operadores logicos 
AND, OR , NOT """

# AND
resultado1 = True & True # Devuelve True
resultado2= False & True # Devuelve False
resultado3 = True & False # Devuelve False
resultado4 = False & False # Devuelve False

# OR
resultado5 = True & True # Devuelve True
resultado6 = False & True # Devuelve True
resultado7 = True & False # Devuelve True
resultado8 = False & False # Devuelve False

# NOT
resultado9 = not True  # Devuelve False
resultado10 = not False # Devuelve True

"""Not es de negacion, es decir el valor que retorna lo niega"""
# Ejemplo
valor = not (2 > 48) # Lo que esta en parentesis da falso
# con el not se niega es decir que retorna la contratio (True)
print(valor) # Devuelve True