cars = ['audi', "bmw", "chebrolet", "corvette", "tesla"]
for car in cars:

    if car == "bmw" or car=="tesla" or car=="audi":
        print(car.upper())
    else:
        print(car)

# condisionales true
car = "Audi"
print(car == "audi")  # salida --> False

# condicionales false
car_2 = "Audi"
print(car_2.lower() == "audi") # salida --> True

# condisional != para determinar desigualdad
requested_topping = "mushrooms"
if requested_topping != "anchovies": # -> True
    print("Hold the anchovies!")

# comparaciones numéricas
age = 18 # -> int 
print(age==18)  # -> True

answer = 17 
if answer != 42:  # -> True
    print("Esa no es la respuesta correcta. Intenta de nuevo!")

age = 19 
print(age < 21)  # -> True
print(age <= 21) # -> True
print(age > 21)  # -> False
print(age >= 21) # -> False


# Multiple conditions

