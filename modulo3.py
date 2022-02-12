text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

dividirOracion = text.split(".")
encontrarOracion = "The Moon is Earth's only satellite" in text
palabras = ["average", "temperature", "distance"]

for oracion in dividirOracion:
    for palabra in palabras:
        if palabra in oracion:
            print(oracion)

for oracion in dividirOracion:
    for palabra in palabras:
        if palabra in oracion:
            print(palabra.replace(" C", "Celcius"))



name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

print(f'la gravedad de la tierra es de {gravity}')
plantilla = "acerca de la gravedad \n nombre del planeta:{planeta} \n gravedad:{gravedad} m/s2 nombre:{nombre} "
gravedadMetros = gravity * 1000
print(plantilla.format(planeta = planet,gravedad = gravedadMetros,nombre = name))
print(f"acerca de la gravedad \n nombre del planeta: {planet} \n gravedad: {gravity *1000} m/s2 nombre: {name}")