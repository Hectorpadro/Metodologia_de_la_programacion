# Empty Dictionary
"""
homer_0 = {"Color": "yellow", "bag": "homer-donut", "hair": "blue", "dress": "casual", "mom": False }
print(homer_0)
print(type(homer_0))


marge = {"Color": "yellow", "bag": "homer-donut", "hair": "blue", "dress": "green", "mom": True }
gun_0 = {"scar": "yellou_orange",  "headshot": 1.5}


## Add element to dictionary
print(homer_0)
homer_0["x-position"] = 15
homer_0["y-position"] = 25
homer_0["z-position"] = 10
print(homer_0)

marge["x-position"] = 16
marge["y-position"] = 26
marge["z-position"] = 10 

alien_0={'color': 'yellow'}
print(alien_0['color'])

# Modifying values in a dictionary
alien_0=['color']='green'
print(alien_0['color'])

# Add elements to a dictionary
alien_0['x_position']=0
alien_0['y_position']=0
alien_0['name']='Paul'

print(alien_0)

## looping though items
print("Looping through homer_0 dictionary:")
for key, value in alien_0.items():
    print(f"The key {key} Has value: {value}")


"""







#NESTING
#Listas de diccionarios
# listas en diccionarios
# diccionarios en diccionarios


covenant_grunt = {
    "color": "orange",
    "weapon": "plasma-gun",
    "arament": "plasma-grande",
    "health": 2,
}


covenant_elite = {
    "color": "blue",
    "weapon": "plasma-sword",
    "arament": "plasma-grande",
    "health": 7,
}

covenant_jackal = {
    "color": "gray",
    "weapon": "plasma-gun",
    "arament": "plasma-grande",
    "health": 5,
}

# Lista de diccionarios

covenants = [
    covenant_grunt, 
    covenant_elite, 
    covenant_jackal
]

for covenant in covenants:
    print(covenant)
    for key, value in covenant.items():
        print(key, value)
    print()


# Lista en diccionarios
students = {
    "santiago": ["reprobado", "prepa1", "rebelde"],
    "jorge-crack": ["aprobado", "cbtis271", "goleador"],
    "gabriel": ["aprobado", "119muerte", "crack-fornite"],
}

# Diccionarios en diccionarios
sensors = {
    "temperature": {
        "id": "temp_1",
        "location": "aula 105",
        "value": 25, 
        "unit": "celsius",
    },
 "humedad": {
        "id": "hum_1",
        "location": "aula 105",
        "value": 60, 
        "unit": "porcentaje",
    },
}


print("Temperatura")
print(sensors["humedad"]["value"])
print("Ubicacion")
print(sensors["humedad"]["location"])

# Estudar metodo get