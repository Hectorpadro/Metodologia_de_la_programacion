# While
"""
    El while es un ciclo coontrolado/comando
    por condicion.

    La estructura basica de un while es:

        while condicion:
            actions
"""

# while infinito

"""
    Programa si el usuario escribe un numeros
    entre 25 y 50, entonces estar dentro del rango
    y salirme de while,
    de otro modo pidiendo el numero
"""
while True:
    try:
        number = int(input("Ingresa otro numero: "))

        if number >= 25 and number <= 50:
            print("Estas en el rango, lo hciste bien")
            break
        else:
            print("Estas fuera de rango, intenta de nuevo")

    except ValueError:
        print("Se ha introducido una variable no valida.")
    

       