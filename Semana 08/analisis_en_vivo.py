"""Semana 8: la red hospitalaria nos contrata como analistas de datos.

Construimos el informe debajo de este inicio con GUIA_ESTUDIANTE.md.
Leemos la fuente preparada en fuente.py y contamos las menciones recibidas.
"""

from fuente import cargar_datos


USAR_RESPALDO = False  # Lo cambiamos solo si recibimos copias actualizadas.
registros, equivalencias, origen = cargar_datos(USAR_RESPALDO)
print("Fuente:", origen)
print("Registros recibidos:", len(registros))
print("Equivalencias publicadas:", len(equivalencias))

#fase 1 conteo de medicamentos 
conteo_medicamentos = {}
conteo_recetas = 0

# Comencemos aquí con la muestra y después construyamos nuestro contador.
print("\nMuestra de registros:")
for indice in range(3):
    registro = registros[indice]
    print(
            f"\nCédula: {registro['paciente_cedula']}\n - Paciente:{registro['paciente_nombre']}"
            f"\n - Diagnóstico:{registro['diagnostico']}\n - Medicamententos: {registro['medicamentos']}\n"
        ) 
    #conteo 
    for medicamento in registro['medicamentos']:
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
    conteo_recetas += 1


print("\nConteo de medicamentos:")
print("Total de recetas:", conteo_recetas)
print(conteo_medicamentos)


#FASE 1: CONTAR MEDICAMENTOS TOTAL 
conteo_medicamentos = {}
conteo_recetas = 0 
#fase 2 limpieza de datos 
equivalencias = {
    "acetaminofen": "acetaminofén",
    "paracetamol": "acetaminofén",
    "antiácido": "antiacido",
    "losartán": "losartan"
}

for registro in registros:
    for medicamento in registro['medicamentos']:
        nombre = medicamento.strip().lower() 
        #aplicacion de fase 2 
        if nombre in equivalencias:
            nombre = equivalencias[nombre]

        if nombre in conteo_medicamentos:
            conteo_medicamentos[nombre] += 1
        else:
            conteo_medicamentos[nombre] = 1
    conteo_recetas += 1

print("\nConteo de medicamentos:")
print("Total de recetas:", conteo_recetas)
print(conteo_medicamentos)

for medicamento, cantidad in conteo_medicamentos.items():
    print(f" - {medicamento}: {cantidad}")

#fase 3 conteo de pacientes en sedes
conteo_sedes = {}

for registro in registros:
    sede = registro['sede']
    if sede in conteo_sedes:
        conteo_sedes[sede] += 1
    else:
        conteo_sedes[sede] = 1

print("\nPacientes atendidos por Hospital:")

for sede, cantidad in conteo_sedes.items():
    print(f" - {sede}: {cantidad} pacientes")

conteo_diagnosticos = {}

for registro in registros:
    diagnostico = registro['diagnostico']
    if diagnostico in conteo_diagnosticos:
        conteo_diagnosticos[diagnostico] += 1
    else:
        conteo_diagnosticos[diagnostico] = 1

print("\nDiagnosticos de pacientes atendidos:")

for diagnostico, cantidad in conteo_diagnosticos.items():
    print(f" - {diagnostico}: {cantidad} casos")