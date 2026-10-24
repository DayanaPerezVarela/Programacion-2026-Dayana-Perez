#Microreto: ¿nos conviene la promoción?

productos = [0,"Café",5000,20]


indice_productos = (productos[0])

producto = (productos[1])
precio= (productos[2])
unidades_actuales =(productos[3])

#2Calculen el descuento: precio actual × 15 ÷ 100.
#Réstenlo al precio actual para obtener el precio promocional.

descuento = precio * 15 / 100
precio_descuento = precio - descuento

#Calculen el ingreso actual: precio actual × unidades actuales.
ingreso_actual = precio * unidades_actuales

# 4 proyección, supongan que se venderá un 20 % más.
#Calculen ese aumento: unidades actuales × 20 ÷ 100.
#Súmenlo a las unidades actuales.
#El resultado proyectado es 24 unidades; no es una venta confirmada.

aumento = unidades_actuales * 20 / 100 #aumento que tendra la empresa en sus unidades
proyeccion_unidades =  unidades_actuales + aumento #unidades de proyeccion

#Calculen el ingreso proyectado: precio promocional × unidades proyectadas.
#Réstenle el ingreso actual.
ingreso_proyeccion = precio_descuento * proyeccion_unidades

diferencia = ingreso_proyeccion - ingreso_actual

#Si la diferencia es mayor que cero, recomienden “lanzar”. Si es cero o menor, recomienden “no lanzar”.

if diferencia > 0 :
    recomendacion = "Lanzar"
else:
    recomendacion = "NO lanzar"
    
    
    
print("ANÁLISIS DE PROMOCIÓN")
print(f"Producto: {producto}\nPrecio actual: ₡{precio}\nUnidades actuales: {unidades_actuales}")
print("Ingreso actual:", ingreso_actual)
print("Descuento: 15%")
print(f"Precio promocional:{precio_descuento}\nUnidades proyectadas: {proyeccion_unidades}\nIngreso con promoción: {ingreso_proyeccion}\nDiferencia: {diferencia}")
print(recomendacion)
