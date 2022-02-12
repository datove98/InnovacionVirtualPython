dimension = 0
velocidad =26
entroATierra = True
if isinstance(dimension, int):
    if dimension < 25:
        print("el asteroide se desintegrara antes de golpear la tierra")
    elif dimension >= 25 and dimension < 1000:
        print("el asteroide hara mucho daño a la tierra")

if velocidad > 25:
    print("el asteroide llega a alta velocidad")
else:
    print('Nada que ver aquí :)')

if  entroATierra and velocidad > 20:
    print("el asteroide producira un rayo de luz")
else:
    print('Nada que ver aquí :)')
