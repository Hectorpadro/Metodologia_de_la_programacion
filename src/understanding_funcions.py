### FUNCIONES
# Las funciones son bloques de codigo para realizar
# una tarea en espesifico 

# Cuando queremos realizar la tarea que se ha definido
# en la funcion, tenemos que llamar el nombre de la 
# funcion 

""" 
    Sintaxis de una funcion

    def nombre_funcion()
    acciones

    Ejemplo: vamos a definir una funcion que de un saludo 
    a christofer.

"""

def gretting_christopher():
    """
        Funcion para saludar a una persona
        llamada Christopher
    """
    for i in range(0,5):
        print("Hello christopher")

gretting_christopher()


# Ejemplo de una funcion que genere el nombre completo
# de una persona y lo regrese 

def create_full_name(first_name, middle_name,  last_name):
    full_name = f"{first_name} {middle_name} {last_name}".title()
    return full_name
    
first_name = input("Dame tu primer nombre: ")
middle_name = input("Dame tu segundo nombre: (Si no tiene segundi nombre dar enter) ")
last_name = input("Dame tu apellido: ")

# Argumentisos posicionales
generated_fullname = create_full_name(
    first_name.lower().strip(), 
    middle_name.lower().strip(), 
    last_name.lower().strip())
print(generated_fullname)

# Argumentos llave
generated_fullname2 = create_full_name(
    middle_name= middle_name,
    first_name= first_name,
    last_name= last_name
)
print(generated_fullname2)

# args en funciones
# kwargs en funciones
# Manejo de datos (.txt, .csv, json, exel, works, pdf)
# args via consola (sys)
#
#
