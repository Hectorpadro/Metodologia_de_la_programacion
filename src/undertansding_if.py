
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

age_0 = 22
age_1 = 18

print("Multiples condiciones")
print( "Operacion and- PSInt (Y)")
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 and age_1 >= 18)


print("Multiples condiciones")
print( "Operacion or- PSInt (O)")
print(age_0 >= 21 or age_1 >= 21)
print(age_0 >= 21 or age_1 >= 18)

# verificar si un elemento esta en una lista
requested_toppings = ['mushrooms', 'onions', 'pineapple']   
print ('\n-----Verificar si un valor esta en la lista-----')
print("mushrooms" in requested_toppings)  # -> True
print("pepperoni" in requested_toppings)  # -> False

# a value nos in a list 
banned_users = ["gabriel", "max", "andrik", "quebedo", "christopher"]
user = "pedro"
print(user not in banned_users)  # -> True

# varaiables de tipo boleanos
game_active = True
can_edit = False

""" 
   if statement

   if condition:
         do something

    If condition 
        do something(true)

    else:
        do something(false)
"""

#Preguntar la edad del usuario
# y decirle  si tiene edad
# suficiente para votar
# input("") -> str
age = int(input("\n\nEscribe tu edad: "))
print(f"tu edad es: {age}")

if (age) >= 18:
    print("Tu tienes edad para votar") 
else:
    print("Lo siento eres demasiado joven para votar")
