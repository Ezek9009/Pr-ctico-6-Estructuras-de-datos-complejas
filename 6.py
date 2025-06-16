"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. 
Ejemplo: 

alumnos = {"sofia": (10,9,8),
           "luis": (6,7,7)                
}
"""
alumnos = {}

#2 bucles para ingresar alumnos y sus notas
for i in range(3):
    nombre = input("ingrese nombre de alumno: ")
    notas = [] 
    for j in range(3):
        nota = int(input(f"ingrese nota: {j+1} de {nombre}:"))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

#mostrar el promedio de cada alumno:
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Promedio = {promedio:.2f}")
