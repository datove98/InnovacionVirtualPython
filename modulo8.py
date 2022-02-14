from matplotlib.pyplot import polar


planet = {
    "name": "mars",
    "number" : 42
}

planet["circunferencia"] = {
    "polar" : 6752,
    "equatorial" : 6792
}

print(planet["circunferencia"]["polar"])

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

numeroDeLunas = 0
numeorDePlanetas = 0

#numeroDeLunas += int(lunas)

for lunas in planet_moons.values():
    numeroDeLunas += int(lunas)

numeorDePlanetas = len(planet_moons.keys())

print(numeroDeLunas)
print(numeorDePlanetas)