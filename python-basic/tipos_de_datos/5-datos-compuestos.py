# Datos compuestos
"""
Son datos que a dentro tienen datos simples o compuestos
lista =  ["Andres","Cepeda",28,True,1.80]
tupla = ("Andres","Cepeda",28,True,1.80)
conjusto = {"Andres","Cepeda",28,True,1.80}
"""
# Ejemplo de datos compuestos
""" Lista = Mutable, permite ser modificada """
# Se crea una lista y se almacena en la variable
lista_uno = ["Andres","Cepeda",28,True,1.80]
print(lista_uno) # ["Andres","Cepeda",28,True,1.80]

# Accediendo a un valor en la lista index
print(lista_uno[0]) # Andres
print(lista_uno[1]) # Cepeda
print(lista_uno[2]) # 28
print(lista_uno[3]) # True
print(lista_uno[4]) # 1.80
print(len(lista_uno)) # Imprime la cantidad de elementos 5


"""Tupla 
Es inmutable,
NO permite ser modificada desde su indice
Permite acceder a su indice
Es ordenada
"""
tupla_uno = ("Andres","Cepeda",28,True,1.80)

# No se puede modificar un valor
# tupla_uno[2] = 5;  Saldra error ya no es mutable es un set


"""Conjumto
son colecciones desordenadas, 
que se pueden redefinir
no se puede modificar con su indice,
no se puede acceder desde el indice
No admite elemntos repetidos.
Son mutables """
conjunto = {"Andres","Cepeda",28,True,1.80}


"""Diccionarios
Son desordenados
Se basa clave valor
No se puede repetir una clave
"""
diccionario = {
    "nombre": "Andres",
    "apellido": "Cepeda",
    "estatura": 1.80,
    "esta_emocinado" : True
}

# para mostrar el valor se accede a la clave
print(diccionario["nombre"])
