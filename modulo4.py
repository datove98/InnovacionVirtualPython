tierra = 149597870
jupiter = 778547200

distancia = jupiter - tierra

distanciaEnMillas = distancia * 0.621

print(distancia)
print(distanciaEnMillas)

planeta1 = input("distancia desde el sol al primer planeta deseado?")
planeta2 = input("distancia desde el sol al segundo planeta deseado?")

valorPlaneta1 = int(planeta1)
valorPlaneta2 = int(planeta2)

distancia = valorPlaneta1 - valorPlaneta2

distanciaEnMillas = distancia * 0.621

print(abs(distanciaEnMillas))

