planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
planets.append("pluton")
print("hay " , str(len(planets)) , "planetas incluido " , str(planets[-1]))

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
busqueda = input("planeta a buscar ")

posicionPlaneta = planets.index(busqueda)

planeta = planets[posicionPlaneta]

print("estos son los planetas mas cercanos a", planeta)

print(planets[0:posicionPlaneta])

print("estos son los planetas mas lejanos a", planeta)

print(planets[posicionPlaneta + 1:])