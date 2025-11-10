"""
    Las listas tambien pueden almacenar 
    numeros ybde hecho, son ideales para esto.
    Python ofrece una gran cantidad de 
    herramientas que ayudan a trabajar
    eficientemnete con listas de numeros.
"""
# Metodo built_in range()

"""
    El metodo range() nos ayuda a crear facilmente
    una serie de numeros:

    Ejemplo:
"""
print("Numeros del 0 al 9:")
for value in range(10): # 10 numeros, del 0-9
    print(value)

print("Numeros del 1 al 9:")
for value in range(1,10): # 10 numeros, del 1-9
    print(value)

print("Numeros Impares del 1 al 9:")
for value in range(1,10,2): # 10 numeros entre 1-9
    print(value)


print("Numeros Pares del 1 al 9:")
for value in range(0,10,2): # 10 numeros entre 1-9
    print(value)

print("Numeros Impares del 1 al 9:")
for value in range(1,10,2): # 10 numeros entre 1-9
    print(value)
event_numbers = list(range(0,10,2))
print(event_numbers)

print("Tabla del 9:")
for value in range(0,91,9): # 10 numeros entre 1-9
    print(value)
tabla_del_9 = list(range(0,91,9))
print(tabla_del_9)


# Cuadrados de los priemros 10 numeros
squares = []
for number in range(1,11):
    square = number ** 2
    squares.append(square)
print(squares)

## Mas metodos bilit_in
# Metodo min()

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # Salida: 0

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits)) # Salida: 9

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(sum(digits)) # Salida: 45