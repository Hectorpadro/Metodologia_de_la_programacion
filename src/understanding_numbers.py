# Numbers
"""
    Enteros
        los podemos sumar (+), restar(-),
        multiplicar(*), dividir(/).
        Les podemos aplicar potencias(**2, **3, **4, ...)
        modulo (%)

"""

number_1 = 35
number_2 = 35
suma = number_1+number_2
resta = number_1-number_2
multiplicasion = number_1*number_2
division = number_1/number_2
potencia = number_1**2
modulo = number_1%number_2

print("suma: ", suma, type(suma))
print("resta: ", resta, type(resta))
print("multiplicasion: ",  multiplicasion, type(multiplicasion))
print("division: ", division, type(division))
print("potencia: ", potencia, type(potencia))
print("modulo: ", modulo, type(modulo))

"""
    Jerarquia de operaciones 

    2+3*4 -> 14

    (2+3)*4 -> 20

"""

"""
    Floats
        Python llama Floats a cualquier numero con un punto desimal.

        Los podemos sumar (+), restar(-),
        multiplicar(*), dividir(/).
        Les podemos aplicar potencias(**2, **3, **4, ...)
        modulo (%)
"""

print(0.1+0.2)
print(0.2-0.2)

print(2*0.2)


# Imprimir la edad de alguien 
age = 33
message = "Charly tiene " + str(age) + "años."
print(message)

"""
    TypeError: Esto significa que Python
    no puede reconoser el tipo de informacion 
    que se esta utilizando.
"""