# Tuples

"""
    Las tuplas son listas de elementos que no
    cambian de tamaño. las tuplas son INMUTABLES.

    Se utilizan los () para definir una tupla.

"""
rectangle_measurements = (200, 50) # (largo, ancho)
print(rectangle_measurements[0])
print(rectangle_measurements[1])

for measures in rectangle_measurements:
    print(measures)

# print(dir(rectangle_measurements)) # built-in dir para  ver las 

# Regrresando tantito a las listas
cars = ['bwm', 'porche', 'masda']
print(cars)

cars[0]="bmw"
cars[1]="porshe"
cars[2]="mazda"
print(cars)

rectangle_measurements = (200, 50) # (largo, ancho)
# rectangle_measurements[0]=300 #No se puede 
# rectangle_measurements[0]=100 #No se puede
rectangle_measurements = (300,100)

"""
    No podemos modificar una tupla directamnetnte 
    lo que si podemos hacer es cambiar la asignacion 
    a una variable que almacena una tupla
"""
