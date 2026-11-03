"""Caso 1: cambio del consumo diario de agua. Complete el programa."""


consumos_litros = [120, 115, 108, 102, 96]

print("Días de consumo registrados:", len(consumos_litros))
print("Primer consumo:", consumos_litros[0])
print("Último consumo:", consumos_litros[-1])

print("\nAnalisis de consumo de agua")



# TODO: Calcule el consumo total y el promedio diario.
total_consumo = sum(consumos_litros)
promedio_diario = total_consumo / len(consumos_litros)

ultimo_consumo = consumos_litros[-1]


# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día. 
for consumo in consumos_litros:

    litros_ahorrados = consumo - ultimo_consumo
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
    if consumo != 0:
        porcentaje_reduccion = (litros_ahorrados / consumo) * 100
    else:
        porcentaje_reduccion = 0

    if porcentaje_reduccion >= 15:
        clasificacion = "reducción alta"
    elif porcentaje_reduccion > 0:
        clasificacion = "reducción moderada"
    else:
        clasificacion = "sin reducción"
# TODO: Muestre los cinco resultados.


    print(f"\nConsumo: {consumo} L")
    print(f"Ahorro respecto al último día: {litros_ahorrados} L")
    print(f"Reducción: {porcentaje_reduccion:.0f}%")
    print(f"Clasificación: {clasificacion}")

print(f"\nTotal de consumo: {total_consumo} L")
print(f"Promedio diario: {promedio_diario:.1f} L")
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
