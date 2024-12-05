# Variables=  declaracion / definicion
# Son espacios que se almacenan en la memoria de nuestro programa.
# Son contenedores que nos permiten almacenar distintos tipos de datos
# que pueden variar, texto, numeros, listas, diccionatios, etc
###################
"""Variable tipo numero"""
# declaracion = definicion
entero = 4
flotante = 4.0
###################

###################
"""Variable boleano"""
valor_boleano = True 
valor_boleano = False
###################

################### 
"""Variable cadena (String)"""
nombre = "Pepe"
# Se concatena con + a la cadena en una variable
bienvenida = "Hola " + nombre + " como estas?"
print(bienvenida) # Se imprime la cadena

# Pero si deseamos integrar un numero o un boleano.
nombre = True # 5
# Concatena con (f string)
bienvenida = f"Hola {nombre} como estas?"
# Uso de f string para concatenar valores numericos o bolenos a String
###################

###################
# Hacer que una variable no este mas declarada
"""Usamos la palabra reservada (del)"""
# Ejemplo
nombre = 5
bienvenida = f"Hola {nombre} como estas?"
print(bienvenida)
del nombre # Eliminamos los datos que estan en la memoria
###################



