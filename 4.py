"""
4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. 
Ejemplo:

contactos = {"Juan": "123456", "Ana": "987654"}
"""

agenda = {}

for i in range(2):
    nombre = input("ingrese nombre: ")
    numero = int(input("ingrese numero de cel: "))
    agenda[nombre] = numero

consulta = input("nombre a consultar?: ")
telefono = agenda.get(consulta)

if telefono:
    print(f"El numero de {consulta} es {numero}")
else:
    print("Contacto no encontrado.")