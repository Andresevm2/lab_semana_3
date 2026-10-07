"""
EJERCICIO 05: Menú de cómputo geométrico.

Complete las funciones para que al ejecutar el programa, se muestre el menú y se le pida al usuario ingresar una de las opciones
(1 - 4). 
    - Si escoge 1, se pide ingresar el valor del radio, se calcula el área del círculo y se muestra en pantalla
    - Si se escoge 2, se pide ingresar el valor de la base y la altura, se calcula el área del triángulo y se muestra en pantalla
    - Si se escoge 3, se pide ingresar el valor de la base y la altura, se calcula el perímetro del rectángulo y se muestra en pantalla
    - Si se escoge 4, se sale del menú y termina el programa
    - Si se ingresa cualquier otra opción, se imprime "Opción inválida. Intente de nuevo."
"""

def area_circulo(radio):
    # Calcular el área (π * r^2)
    area = 3.1416 * (radio ** 2)
    print(f"El área del círculo es: {area}")

def area_triangulo(base, altura): 
    # Calcular el área ((base * altura) / 2)
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")

def perimetro_rectangulo(base, altura):
    # Calcular el perímetro (2 * (base + altura))
    perimetro = 2 * (base + altura)
    print(f"El perímetro del rectángulo es: {perimetro}")

def menu():
    activo = True
    while activo:
        print("\nCALCULADORA GEOMÉTRICA")
        print("1. Área de un Círculo")
        print("2. Área de un Triángulo")
        print("3. Perímetro de un Rectángulo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        match opcion:
            case "1":
                x = float(input("Ingrese el radio del círculo: "))
                area_circulo(x)
            case "2":
                x = float(input("Ingrese la base del triángulo: "))
                y = float(input("Ingrese la altura del triángulo: "))
                area_triangulo(x, y)
            case "3":
                x = float(input("Ingrese la base del rectángulo: "))
                y = float(input("Ingrese la altura del rectángulo: "))
                perimetro_rectangulo(x, y)
            case "4":
                print("Saliendo...")
                activo = False
            case _:
                print("Opción inválida. Intente de nuevo.")

menu()