"""

    Docstring for understanding_while_loop_centinel 

    Un programa que:
        -Cuente cuantos numeros a ingresado el usuario
        -Realice la suma de todos los numeros ingresados
        -Me diga caul es el minimo de los numeros ingresados
        -Me diga caul es el maximo de los numeros ingresados 

"""

counter = 0
sum_quantities = 0.0
minimun = None
maximun = None

while True:
    print("Escribe exit para salir")
    user_input = input("Ingresa una cantidad (MXN): ")
    
    if user_input == 'exit':
        break

    try:
        value = float(user_input)
    except ValueError:
        print("Caracter invalido. Por favor ingresa un numero.")
        continue
    except KeyboardInterrupt:
        print("Salida manual")
        break
    
    counter = counter + 1 # (contador) counter += 1
    sum_quantities = sum_quantities + value # (sumador) sum_quantities += value

    if minimun is None or value < minimun:
        minimun = value

    if maximun is None or value > maximun:
        maximun = value

print("cantidad de numeros ingresados:", counter)
print("")
print(f"El minimo es: {minimun} MXN")
print(f"El maximo es: {maximun} MXN")


