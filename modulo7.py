newPlanet = ""
planetas = []

print("hola")

while newPlanet != "done":
    newPlanet = input("igrese un planeta, si quiere salir del ciclo escriba 'done'")
    if newPlanet != "done":
        planetas.append(newPlanet)

for planeta in planetas:
    print(planeta)