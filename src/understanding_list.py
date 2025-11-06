# Lists

"""
    Las listas son elemtos mutables

    Las listas nos permiten almacenar infomacion
    en un lugar, la cantidad que tengan: ya sean
    pocos elemtentos o millones de elementos.

    Se recomienda nombrar una variable del tipo lista 
    en plural

    En Python los corchetes [] definen una lista, 
    sus elementos van separasdos por comas. 

"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'giant']
print(bicycles)
 
print(bicycles[0].title())

# Los indices comienzan en 0 y terminan en n-1
print(bicycles[4].title())

# Acceder al ultimo elemento

print(bicycles[-1].title()) # ultimo elemento
print(bicycles[-2].title()) 
print(bicycles[-5].title()) # primer elemento

# Utilizando valoes de la lista 

message = "Mi primer bicicleta favorita fue una " + bicycles[4].upper() + "."
print(message)

message_f = f"Mi primer bicicleta favorita fue una {bicycles[4].title()}."
print(message_f)

# Agregar elemtos a una lista
print("\n")
print("Agregar elementos a una lista")
print(bicycles)

print("Metodo de las listas para agregar elemtos: list_name.append(element)")
bicycles.append("ducatti")
print(bicycles) 

"""
    #LISTAS A-105
    Agregar elementos a una lista
        - append(): Agregar un elemento al final de la lista.

"""

print("\n--- Agregar elementos a una lista metodo append() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""
    Agregar elemntos a una lista en una posicion especifica 
        - insert(): Inserta un elemento en una posicion especifica.
"""
print("\n--- Agregar elementos a una lista metodo insert() ---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1,'ducati')
print(motorcycles) # Salida: ['honda', 'ducati', 'yamaha', 'suzuki']

"""
    Eliminar elementos de una lista
        - del: Elimina un elemento en una posicion especifica.
"""
print("\n--- Eliminar elementos de una lista metodo del ---")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) # Salida: ['yamaha', 'suzuki']

"""
    Eliminar elementos de una lista y usar el valor eliminado
        - pop(): Elimina y devuelve el ultimo elemento de la lista.
"""
print("\n--- Eliminar elementos de una lista y usar el valor eliminado metodo pop() ---")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
last_motorcycle = motorcycles.pop()
print(motorcycles) # Salida: ['honda', 'yamaha']
print(f'La ultima motocicleta que borraste fue {last_motorcycle}.')

"""
    Eliminar un elemento especifico de una lista por valor
        pop(index): Elimina y devuelve el elemento en la posicion especificada.
"""
print("\n--- Eliminar un elemento especifico de una lista por valor metodo pop(index) ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
first_motorcycle = motorcycles.pop(1)
print(motorcycles) # Salida: ['honda', 'suzuki', 'ducati']
print(f'La primera motocicleta que borraste fue {first_motorcycle}.')

"""
    Eliminar un elemento especifico de una lista por valor
        remove(): Elimina la primera aparicion del valor especificado.
"""
print("\n--- Eliminar un elemento especifico de una lista por valor metodo remove() ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']   
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']

"""
    # LISTAS A-105
    Organizar una lista permanentemente
        - sort(): Ordena la lista de forma permanente en orden alfabetico.
"""
print("\n--- Organizar una lista permanentemente metodo sort() ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']   
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.sort()
print(motorcycles) # Salida: ['ducati', 'honda', 'suzuki', 'yamaha']
print("\n")
motorcycles.sort(reverse=True)
print(motorcycles) # Salida: ['yamaha', 'suzuki', 'honda', 'ducati']

"""
    Ejemplo:

"""

students = ["jesus", "josue", "andrik", "jen", "miguel", "africa", "gerardo"]
print(students)
desired_student = input("¿Que estudiante deseas eliminar de la lista?: ")
students.remove(desired_student.strip().lower())
print(students)
print("Tu has eliminado a ", desired_student)
students.reverse()
print(students)


print(len(students))

cars = ["koa", "ford", "tesla", "volvo", "chevrolet"]
print(sorted(cars))
sorted_list = sorted(cars)
print(cars)
print("Lista original:", cars)
