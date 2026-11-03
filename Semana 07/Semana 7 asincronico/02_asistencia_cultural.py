"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

total = 0
bloques_superan = 0

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
for asistencia in asistencias:
    total += asistencia

    # 70 % de 300 = 210
    # 210 NO cuenta, por eso usamos >
    if asistencia > capacidad * 0.70:
        bloques_superan += 1
# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total / len(asistencias)
porcentaje = (promedio / capacidad) * 100
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje >= 80:
    estado = "alta"
elif porcentaje >= 50:
    estado = "media"
else:
    estado = "baja"
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
print("Total de asistencias:", total)
print("Promedio de asistencia:", promedio)
print("Porcentaje de ocupación:", porcentaje, "%")
print("Bloques que superan el 70%:", bloques_superan)
print("Estado de ocupación:", estado)
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
