"""Microreto: el portero del café."""

energia = int(input("Cuanta energía tienes de 0-100:"))
trae_cafe = input("¿Traes café? (si/no): ") .lower().strip() == "si"
mensaje = "Completa las reglas del portero."
#denegar acceso si trae menos del 30% de energia y no trae cafe no puede entrar 
#si trae más o igual a 30% o tiene cafe puede entrar
#cualquiera otro portero confundido revise las respuestas
 
if energia < 30 and not (trae_cafe):
    mensaje = "Acceso denegado, no puedes soportar la jornada completa"
elif energia >= 30 and energia <= 100 or trae_cafe:
    mensaje = "Puede entrar, puede soportar la jornada"
else :
    mensaje = "Portero confundido, revisa las respuestas"


mensaje = "Completa las reglas del portero."

# TODO: usa and para detectar energía baja sin café.
# TODO: usa or para permitir energía suficiente o café.
# TODO: escribe mensajes claros para cada resultado.

print(mensaje)
