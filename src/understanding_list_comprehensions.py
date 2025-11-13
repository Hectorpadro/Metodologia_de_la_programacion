
"""

squares=[]
for value in range(o,11):
    square = value**2
    squares.appedn(square)
print(squares)
"""
"""
    Una lista comprehention combins el cislo for 
    y la creacion de nuevos elementos en una sola 
    linea y automaticamente agrega cada nuevos elemento
    a la lista, es dedir, sin utilizar el metodo append.
"""

squares = [value**2 for value in range(0,11)]
print("\n",squares)

# para los numeros pares entre o a 100
evens_range = [value for value in range(0,101,2)]
print("\n",evens_range)


evens_if = [value for value in range(0,101) if value % 2 ==0]
print("\n",evens_if)


