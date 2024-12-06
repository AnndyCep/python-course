###################
"""Operadores de Pertenencia
Este se una para confirmar si un valor no esta presente
en una coleccion como listas, tuplas, diccionarios, cadenas etc..
(in --> devuelve True si el valor si esta en la coleccion)
(not in --> devuelve True si el valor NO esta en la coleccion)
"""
# Ejemplo in
lista1 = [1,2,3,4,5]
print(2 in lista1) # True, 
# Ya que el elemento 2 si esta en la coleccion

lista2 = [1,2,3,4,5]
print(6 in lista2) # False,
# Ya que el elemento 6 No esta en la coleccion.

# Ejemplo not in

lista1 = [1,2,3,4,5]
print(2 not in lista1) # Falso,
# Ya que el elemento 2 si esta en la coleccion

lista2 = [1,2,3,4,5]
print(6 not in lista2) # True,
# Ya que el elemento 6 No esta en la coleccion.