"""
5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra. 
Ejemplo:

Palabras_unicas: {'hola', 'mundo'}
Recuento: {'hola': 2, 'mundo': 1}
"""
#convertimos todo a minusculas para evitar duplicados
frase = input("ingrese una frase: ").lower()

#divide la frase en palabras
palabras = frase.split()

#set de palabras unicas
palabras_unicas = set(palabras)

#diccionario para contar apariciones
recuento = {}

for i in palabras:
    if i in recuento:
        recuento[i] += 1
    else:
        recuento[i] = 1
print(f"Palabras unicas: {palabras_unicas}")
print(f"Recuento: {recuento}")