#Solucion Misión Kit Seguro
# Autor: Dayana Pérez V. 6/10/2026

nombre = input("Nombre:").strip().upper()
kit = input("Tipo de kit:").strip().lower()
autorizacion = input("Tiene autorizacion? (Si/No):").strip().lower() == "si"


try:
    cantidad = int(input("Ingrese la cantidad:"))
except ValueError:
    print("Error cantidad invalida, asignada -1")
    cantidad = -1
    
try:
    dias = int(input("Días de prestamo:"))
except ValueError:
    print("Error dias invalido se asigna -1")
    dias = -1
  
resultado = ""
if nombre == "" or not kit or cantidad < 1 or dias < 1:
    resultado = "Registro rechazado:Datos Inválidos"
elif autorizacion and cantidad <=3 and not dias > 7:
    resultado = f"Solicitud aprobada para {nombre}: {cantidad} kit(s) de {kit}"
elif cantidad > 3 or dias > 7:
    resultado = "Solicitud enviada a revisión!"
else :
    resultado = "Solicitud rechazada, se requiere autorización"
print(resultado)
