########################
""" Keys --> Retorna un objeto dict_items (que se puede iterar) con las llaves del diccionario,
 tambien nor sirve para iterar los elementos"""
diccionario_keys = {
    "nombre" : "Andres",
    "apellido" : "Cepeda",
    "edad" : 28
}
retorno_keys = diccionario_keys.keys()
print(f"Ejemplo keys --> {retorno_keys}") # Imprime --> dict_keys(["nombre","apellido","edad"])
########################

########################
""" Get --> Retorna el valor de la clave enviada por parametro, al no ser encontrada no retorna error """
diccionario_get = {"modelo": "ford" , "añor" : 2024 , "kilometraje" : 0}
valor = diccionario_get.get("modelo")
print(f"Ejemplo get --> {valor}") # Imprime --> ford
########################

########################
""" pop --> Elinama el valor de la clave que se pase como parametro,
Warning --> Al no encontrar la clave salta error KeyError, siempres se debera pasar por lo menos un argumento"""
diccionario_pop = {"ciudad": "Bogota" , "barrio": "perdono", "estrato": 3}
valor_eliminado = diccionario_pop.pop("ciudad")
print(f"Ejemplo pop valor --> {valor_eliminado}")
print(diccionario_pop)
########################

########################
""" Items --> Itera sobre la coleccion de objetos del diccionario, y retorna un objeto iterable"""
diccionario_items = {
    "nombre" : "Andres",
    "apellido" : "Cepeda",
    "edad" : 28
}
diccionario_iterable = diccionario_items.items()
print(f"Ejemplo items --> {diccionario_iterable}")
########################

########################
""" update --> Actualiza el diccionario con la clave y valor de tro diccionario """
diccionario_base = {
    "nombre" : "Andres",
    "apellido" : "Cepeda",
    "edad" : 28
}
diccionario_update = {"ciudad": "Colimbia"}
diccionario_base.update(diccionario_update)
print(f"Ejemplo uptade --> {diccionario_base}") # Imprime el diccioario base , agregando el otro diccionario.

# Otra forma de agragar mas elementos al diccionario , seria de una forma mas directa
diccionario_base["estrato"] = 3
print(f"Ejemplo insertando datos directos --> {diccionario_base}") # Imprime el diccionario junto con el nuevo clave valor
########################

########################
""" Clear --> eliminar todos los elementos del diccionario, dejando el diccionario vacio"""
diccionario_base.clear() # Retorna el diccionariol vacio {}
########################