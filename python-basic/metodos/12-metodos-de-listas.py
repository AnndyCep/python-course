#############################
""" len() --> Retorna la cantidad de elementos en nuestra lista """
lista = ["Hola","Andres","como","estas?"]
lista_len = len(lista) # Imprime (4) la cantidad de elementos en la lista
print(f"Ejemplo len {lista_len}")
print(dir(lista))
#############################

#############################
""" append --> Agrega elemtentos a la lista al final """
lista.append("nuevo_valor")
print(f"Ejemplo append {lista}") # Imprime --> ["Hola","Andres","como","estas?","nuevo_valor"]
lista.append([1,2,3,4,5])
print(f"Ejemplo append {lista}") 
# Se puede agrega un objeto lista con el metodo append
# Imprime --> ["Hola","Andres","como","estas?","nuevo_valor", [1,2,3,4,5]]
#############################

#############################
""" Insert --> Agrega un valor a la lista en un indiice """
lista.insert(2,"otro_valor")
print(f"Ejemplo insert {lista}") 
# Imprime --> ["Hola","Andres","otre_valor","como","estas?","nuevo_valor"]
# El valor que estaba en ese indice se corre una a la derecha.
#############################

#############################
""" Extend --> Agrega una lista a otra lista"""
otra_lista = [1,2,5,True,2.9]
lista.extend(otra_lista)
print(f"Ejemplo extend {lista}") # Imprime --> ["Hola","Andres","otre_valor","como","estas?","nuevo_valor",1,2,5,True, 2.9]
#############################

#############################
""" Pop --> Elimina un elemento con el indice """
lista.pop(2) # Elimina el valor que este en el indice (2)
lista.pop(-1) # Para eliminar el ultimo elemento
print(f"Ejemplo pop {lista}")  # Imprime la lista sin el elemento eliminado
# ["Hola","Andres","como","estas?","nuevo_valor",1,2,5,True, 2.9]
#############################

#############################
""" Remove --> Elimina el elemneto por su valor """
lista.remove("nuevo_valor") # Se debe saber cual es el valor, ya que si no esta retorna error
print(f"Ejemplo remove {lista}")  
# Imprime --> ["Hola","Andres","como","estas?",1,2,5,True, 2.9]
# Warning --> Manejo de exeptions, ya que no esta el elemento en la lista, se genera error
#############################

#############################
""" Sort --> Ordena la coleccion de elementos en orden acendente """
 # Warning --> Solo se podran ordenar datos si no tiene combinaciones de String y numeros generar error
lista_numeros = list(range(10,0,-1))
print(lista_numeros) # Imprime --> [10,9,8,7,6,5,4,3,2,1]
lista_numeros.sort() # Ordena de forma ascendente los numeros de la lista
print(f"Ejemplo sort {lista_numeros}")  # Imprime --> los numeros de la lista
lista_numeros.sort(reverse = True) # Ordena de forma descendente los numeros de la lista
print(f"Ejemplo sort descendente {lista_numeros}")  # Imprime --> los numeros de la lista e forma descendente
#############################

#############################
""" Reverse --> revierte los elementos de la lista, solo los revierte no los ordena, es decir que nos los ordena"""
lista_reverse = [1,5,2,4,3]
lista_reverse.reverse() # Revierte la lista de numeros
print(f"Ejemplo reverse {lista_reverse}") 
# Imprime --> [3,4,2,5,1] No ordena los numeros (asc , desc) solo los revierte
#############################

#############################
""" Index --> retorna el indice del valor encontrado """
lista_index = list(range(1,11)) # Se crea una lista del  1-10
valor_index = lista_index.index(3) # Pasamos como pametro el valor 2 al metodo index, para retornar un valor
print(f"Ejemplo Index --> {valor_index}") # Imprime el indice del valor encontrado (2)
# Warnig --> Si no encuentra el valor retorna valor.
#############################

set("arroz","lente","papa")
