
print("-----EJERCICIO 10------")
nombre = input("Escriba el nombre del empleado: ")
valorDia = 43352
print("Valor día:", valorDia)
dias = float(input("¿Cuántos días trabajó el empleado?: "))
total = valorDia * dias
descuento = input("¿Desea aplicar descuento de salud y pensión? Responda 'si' o 'no': ")

if descuento == "si":
    salud = (total * 15) / 100
    pension = (total * 10) / 100
    totalFinal = total - salud - pension
    print("Nombre empleado:", nombre)
    print("Días trabajados:", dias, "días")
    print("Aplica descuento salud y pensión")
    print("Total devengado:", totalFinal, "pesos")
else:
    print("Nombre empleado:", nombre)
    print("Días trabajados:", dias, "días")
    print("No aplica descuento salud y pensión")
    print("Total devengado:", total, "pesos")
