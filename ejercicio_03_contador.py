"""
EJERCICIO 03: Contador de vocales

Dada una frase escrita por el usuario, recorre cada letra e indica la cantidad de vocales (a, e, i, o, u) que tiene la palabra.
"""
frase = input("Ingrese una frase: ")

cantidad_vocales = 0

vocales = "aeiouáéíóú"

for letra in frase.lower():
    if letra in vocales:
        cantidad_vocales += 1

print(f"\nLa frase contiene {cantidad_vocales} vocal(es).")