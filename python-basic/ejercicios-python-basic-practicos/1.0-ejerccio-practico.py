""" Si una persona se tarda 1 segundo en decir dos palabras.
Hacer, 
a) pedirle a un usuario que diga cualquier texto real y
calcular cuanto tardaria en decir esa frase, Cuantas palabras dijo ?
b) si esta toma mas de un minuto decir al usuario que (No era tan larga la frase)
c) Si Andres hablar 30% mas rapido que otras personas, cuanto tardaria Andres en decir esa frase
"""
def calcular_tiempo_frase(palabra):
    """Esta funcion ayuda a calcular el tiempo que tarda una persona en decir una frase"""
    cantidad_palabra = calcular_cantidad_palabras(palabra)
    resultado_tiempo = cantidad_palabra / 2
    return cantidad_palabra , resultado_tiempo

def calcular_cantidad_palabras(palabra):
    """Esta funcion nos ayuda a retornar la cantidad de palabras que tiene la frase"""
    lista = palabra.split(" ")
    cantidad = len(lista)
    return cantidad

def tarda_andres(tiempo):
    """Esta funcion ayuda a retornar el tiempo que tarda una persona que habla 30% mas rapido que una persona normal"""
    tiempo_andres = tiempo - (tiempo * 30 / 100)
    return tiempo_andres

texto_usuario = input("Ingrese el texto para hacer los calculos ")
cantidad_palabra , resultado_tiempo = calcular_tiempo_frase(texto_usuario)
tiempo_andres = tarda_andres(resultado_tiempo)
print(f" La cantidad de palabra {cantidad_palabra}")
print(f" La cantidad de tiempo {resultado_tiempo} segundos")
print(f" La cantidad de tiempo que tarda Andres es  {tiempo_andres} segundos")

if resultado_tiempo > 60:
    print(f"No era tan larga la frase bro¡")
