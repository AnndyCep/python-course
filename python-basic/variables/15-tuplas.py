"""Se deben utilizar las tuplas cuando solo necesitan leer los datos"""
#########################
""" Creacion de tuplas """
mi_tupla = tuple(["Andres","Cepeda"]) # Incialmente es un diccionario y se parsea tupla
print(type(mi_tupla)) # Imprime --> class_tuple
print((mi_tupla)) # Imprime --> ("Andres","Cepeda")

#########################
""" Creacion de tupla como si fuera desempaquetado multiples datos"""
multiples_tupla = "valor-Uno", "Valor-dos" # Es otra forma de crear otra tupla
print(multiples_tupla) #Imprime --> ("Valor-Uno", "Valor-dos")
#########################

#########################
""" Creacion de tupla como si fuera desempaquetado solo un dato"""
solo_tupla = "valor-Uno", # Es otra forma de crear otra tupla, recordar que se debe asociar con la (,)
print(solo_tupla) #Imprime --> ("Valor-Uno")
#########################



