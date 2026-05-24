empleados = [
    ["Andrea", 8, 8, 9, 8, 10],
    ["Dilan", 7, 8, 8, 7, 8],
    ["Luna", 9, 9, 8, 8, 9],
    ["Andi", 6, 7, 8, 7, 6]
]
def clasificar(suma_horas):
    if suma_horas > 40:
        return "Sobretiempo."
    else:
        return "Horario Estandar."

for empleado in empleados:
    print("Empleado: ", empleado[0]);
    horas = empleado[1:]
    suma_horas = sum(horas)
    print("------------------------------")
    print("Total de horas trabajadas: ", suma_horas)
    resultado = clasificar(suma_horas)
    print(resultado)



