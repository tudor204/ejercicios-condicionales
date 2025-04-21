bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6

puntos = float(input("Cuál es tu puntuación?"))
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos == meritorio:
    nivel = "Meritorio"
else:
    nivel = ""
if nivel == "":
    print("Ésta puntuación no es válda")
else:
    print("Tu nivel de rendimieto es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))