cadena_uno = "Hola soy Andres"

# Funcion DIR, nos permite ver que metodos estan disponibles para el objeto
print(dir(cadena_uno))

""" Metodos de cadena """
########################################################
""" Upper - Nos devuelve todo a mayuscula """
resultado_upper = cadena_uno.upper() 
print(resultado_upper) # Imprime toda la cadena en mayuscula
########################################################

########################################################
""" Lower - Nos restorna todo en minuscula """
resultado_lower = cadena_uno.lower() 
print(resultado_lower) # Imprime  toda la cadena en minuscula
########################################################

########################################################
""" Capitalize - Nos retorna la primera letra de la cadena en mayuscula """
cadena_nueva = "hola mor"
resultado_capitalize = cadena_nueva.capitalize()
print(resultado_capitalize) # Imprime la primera letra en Mayuscula (Hola mor)
########################################################

########################################################
""" Find, buscamos una cadena en otra cadena """
# Retorna el indice donde encuentra la cadena, y -1 no encuentra la cadena
cadena = "hola mor"
cadena_buscar = "a"
retorno = cadena.find(cadena_buscar) # busca en caracter (a) en la cadena
print(retorno) # Imprime 3 (type) --> int
# Si al cadena a buscar, no la encuera retorna -1 
########################################################

########################################################
""" Index --> Este metodo de cadena busca la posicion de la subcadena en la cadeba
es parecido a find, pero no no encuentra el valor, retirna error """
cadena_index = "hola mor"
cadena_buscar_index = "o"
retorno_index = cadena_index.index(cadena_buscar_index)
print(f" Ejemplo index {retorno_index}")
########################################################

########################################################
""" Isnumeric - Nos retorna True, si los caracteres solo son numericos """
# Por solo un caracter que sea del alfabeto devuelve false o si tiene un espacio.
cadena = "hola1"
retorno = cadena.isnumeric()
print(retorno) # Imprime False por que en la cadena no son de caracter numericos.

cadena = "12345"
retorno = cadena.isnumeric()
print(retorno) # Imprime True, ya que todos los caracter son numericos.
########################################################

########################################################
""" Isalpha - Retorna True si son caracteres del alfabeto """
# Nos retorna false, si tiene caracteres con espacio o esta vacia la cadena
cadena_uno = "HolaAndres"
cadena_dos = "Hola Andres"
cadena_tres = ""
print(cadena_uno.isalpha()) # True
print(cadena_dos.isalpha()) # False
print(cadena_tres.isalpha()) # False
########################################################

########################################################
""" Count - Nos retorna la cantidad de veces que conincide la cadena que se pasa como parametro """
cadena = "hola andres a"
print(cadena.count("b")) # Imprime (3) ya que es la cantidad de veces que coincide el caracter en la cadena.
# Si no encuentra coincidencia retorna (0).
########################################################

########################################################
""" len - retorna la cantidad de caracteres que tiene la cadena """
cadena = "hola andres"
print(len(cadena)) # Imprime (11) cantidad de caracteres
########################################################

########################################################
"""Stratwith -  Verificamos si una cadena inicia con una cadena enviada como parametro """
cadena = "hola andres"
print(cadena.startswith("H")) # Imprime (False), ya que distingue entre mayusculas y minusculas
print(cadena.startswith("h")) # Imprime (True)
########################################################

########################################################
"""endwith - Varifica si una cadena finaliza con una cadena enviada como parametro """
cadena = "hola andres"
print(cadena.endswith("e")) # Imprime (False) ya que no ternima con el caracter enviado
print(cadena.endswith("s")) # Imprime (True) ya que ternima con el caracter enviado
########################################################

########################################################
""" Replace --> Remplaza un fragmento de la cadena dada, por otra dada"""
cadena = "Hola andres"
nueva_cadena = cadena.replace(" ", "-")
print(nueva_cadena) # Imprime (Hola-andres)
nueva_cadena = cadena.replace("andres", "usuario")
print(nueva_cadena) # Imprime (Hola usuario)
########################################################

########################################################
""" Split -->Retorna una lista, separa cadenas con el parametro enviado por parametro """
cadena = "Hola andres como estas?"
retorna_lista = cadena.split(" ")
print(retorna_lista) # ["Hola","Andres","como","estas?"]
########################################################

########################################################
"""join --> Permite unir iterable y convertirlos en una cadena explicando el separador """
lista = ["Hola","Andres","como","estas?"]
unir_todo_cadena = " ".join(lista)
print(unir_todo_cadena) # Imprime (Hola andres como estas?)
# apartir de un iterador, los une en una cadena 
########################################################