# Trabajando con listas 
"""
    Recorrer una lista sin importar la cantidad
    de elementos que tenga.
"""

magicians = ["ron", "hermione", "harry", "cedrik"]

for magician in magicians:
    print(magician)
    print(magician.upper())
    print("\n")
    print(f"{magician.title()} ese fue un gran echizo")
    print(f"\t{magician.lower()} No podemos esperar para ver tu siguiente echizo:")

print("Gracias a todos, fue un gran espectaculo")

"""
    Identacion:

    Python usa la identacion para determinar 
    cuando una linbea de codigo esta conecatda a
    la linea de codigo anterior.

    Basicamente, se utilizan 4 espacios en blanco
    para obligarnos a escribir codigo ordenado y 
    estructurado.
"""

# No olvidemos indentar

magicians = ["alice", "david", "carolina"] 
for magician in magicians:
    print(magician)
    

""" 
    error de identacion
"""

# Error de logica 
magicians = ["alice", "david", "carolina"] 
for magician in magicians:
    print(magician)
print(f"I cant't wait to see your next trick, {magician.title()}") 

# Identacion inncesaria
message = "Hello Python world!"
print(message)