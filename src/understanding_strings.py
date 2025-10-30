"""
    String variables

    Un string es de manera sencilla una serie de caracteres. 
    En Python, todo lo que esté entre comillas simples (' ') o dobles (" ")
    se considera un string.

    Ejemplos: 
        "Este es un string"
        'Este tambien es un string'

    'Le dije a un amigo "Python es mi lenguaje favorito"'
    " El lenguaje 'Python' lleva el nombre de monty python "

"""
name = "clase de programacion"
print(name)

# title 
print(name.title())

print(name)

"""
Un metodo es una ccion que python puede realizar en un fragmento de datos o sobre una variable.

    El punto . despues de ina variable 
seguido del metodo title () dice que 
se tiene que ejecutar el metodo title() 
de la variable name.

    Todo los metodos van segudos de parentesisi 
porque n ocasiones necesitan informacion adisional 
para funcionar, la cual ira dentro de los parantesis.
En esta ocasion, el metodo .title() no requiere informacion 
adicional para funconar.

"""

print("Metodo upper: ", name.upper())
print("Metodo lower: ", name.lower())

# Concatenasion de STRINGS
first_name = "charly"
last_name = "mercury"

full_name = first_name + " " + last_name
print(full_name)
print(full_name.title())

# Whitespace 

"""
    UN whitespace se refiere a cualquier caracter que no
    se imprime, es decir, un espacio, tabuladores y 
    finales de linea. LOs whitespace se utilizan 
    comunemnte para organizar las salidas de tal manera 
    que sea mas amigable de ller o ver para el usuario.

    Ejemplo:

        -Tabulador: \t
        salto de linea: \n

"""

print("Whitespace Tabulador")
print("Python")
print("\tPython")
print("\t\tPython")


print("Whitespace Salto de linea")
print("Languages: \n\tPython\nC\n\tJavascripts")

# Eliminacion de espacios en blanco

programin_languages = " Python "

print(programin_languages)
print(programin_languages.rstrip())
print(programin_languages.lstrip())
print(programin_languages.strip())


# Syntax Error con Strings 

message = "Una fortaleza de python es su comunidad"
print(message)
message = "Una fortaleza de "python" es su comunidad"
