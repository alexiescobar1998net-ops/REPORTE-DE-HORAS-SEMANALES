# Función para calcular el total de horas y clasificar la jornada
def calcular_jornada(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion


# Matriz de recursos
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Ana", 8, 8, 8, 9, 9],
    ["Carlos", 8, 8, 8, 8, 8],
    ["María", 7, 8, 7, 8, 7],
    ["Luis", 9, 9, 8, 9, 8]
]

print("===== REPORTE DE HORAS SEMANALES =====\n")

for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_jornada(horas)

    print(f"Recurso: {nombre}")
    print(f"Total de horas: {total}")
    print(f"Clasificación: {clasificacion}")
    print("-" * 35)
