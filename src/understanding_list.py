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