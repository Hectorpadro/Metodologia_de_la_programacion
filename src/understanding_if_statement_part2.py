"""
try:
    age = int(input("Escribe tu edad: "))
except:
    age = -1
    print("Error, ingresaste un caracter no valido")



if age >=100:
    print("Tienes mas de un siglo")
elif age >= 18 and age < 100:
     print("Eres mayor de edad")
elif age >= 0 and age < 18:
    print("Eres menor de edad") 
else:
    print("Tuviste un error") 

print("Hola Charly")
"""



try:
    age = int(input("Escribe tu edad: "))
except:
    age = -1
    print("Error, ingresaste un caracter no valido")


if age <=4 and age>=0:
    print("Entonces la entrada es gratuita")
elif age < 18 and age > 4:
     print("la entrada cuesta $200")
elif age >= 18 :
    print("Entonces la entrada cuesta $400") 
elif age >=0 and age <=100:
    print("Tienes mas de un siglo")
else:
    print("Tuviste un error") 


#  Multiple if 
guisos = ["deshebrada", "asado", "salsa verde", "pozole"]
if "asado" in guisos:
    print("Si hay asado")
else: 
    print("No hay asado")
if "tamales" in guisos:
    print("Hay tamales")
else: 
    print("No hay tamales")
if "salsa verde" in guisos:
    print("Si hay salsa verde")
else: 
    print("No hay salsa verde")

# Utilizando varias listas

guisos_disponinles = ["salsa verde", "deshebrada", "mole"]
guisos_a_ordenar = ["deshebrada", "caldo de iguana"]

print("¿Que guiso desea ordenar")
for guiso in guisos_a_ordenar:
    print(f"Deseo{deseo}")
    if guisos_disponinles:
        print(f"Si tenemos ese guiso{guiso}")
    else:
        print("No tenemos ese guiso")
print("Realizando pedido....")
