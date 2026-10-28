from sedes import emprendimientos

print("Emprendimientos registrados:", len(emprendimientos))
print("Primer emprendimiento:", emprendimientos[0]["nombre"])
print("Primer emprendimiento ventas:", emprendimientos[0]["ventas"])

print("\nAnálisis de Emprendedores")

provincias = set()  # Un set vacío para guardar provincias únicas
#Cada vuelta procesara un diccionario
for empre in emprendimientos:
    total = sum(empre['ventas'])
    porcentaje = total / empre['meta'] * 100

    provincias.add(empre["provincia"])  # Agrega la provincia al set
    
    if porcentaje >= 100:
        estado = "Meta alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atención!"
        
    print(
        f"{empre["nombre"]} | Total: ₡{total:,.2f} | "
        f"Cumplimiento: {porcentaje:.2f}% | {estado}"
    )

    print("\nProvincias registradas:", (provincias))