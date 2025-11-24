# Empty Dictionary

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










#NESTING
#Listas de diccionarios
# listas en diccionarios
# diccionarios en diccionarios
