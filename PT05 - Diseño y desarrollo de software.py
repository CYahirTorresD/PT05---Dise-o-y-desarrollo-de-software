import math
import time
def suma_numeros():
    n = int(input("Ingrese la cantidad de números a sumar: "))
    numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(n)]
    resultado = sum(numeros)
    print(f"La suma de los números es: {resultado}")

def producto_numeros():
    n = int(input("Ingrese la cantidad de números a multiplicar: "))
    numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(n)]
    resultado = 1
    for num in numeros:
        resultado *= num
    print(f"El producto de los números es: {resultado}")

def division_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división de {num1} entre {num2} es: {resultado}")
    else:
        print("No se puede dividir entre cero.")

def factorial_numero():
    n = int(input("Ingrese un número para calcular su factorial: "))
    resultado = math.factorial(n)
    print(f"El factorial de {n} es: {resultado}")

def tablas_multiplicar():
    num = int(input("Ingrese el número para mostrar su tabla de multiplicar (del 1 al 10): "))
    
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def cuadrado_cubo():
    num = float(input("Ingrese un número para calcular su cuadrado y cubo: "))
    cuadrado = num ** 2
    cubo = num ** 3
    print(f"El cuadrado de {num} es: {cuadrado}")
    print(f"El cubo de {num} es: {cubo}")

def promedio_numeros():
    numeros = []
    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        numeros.append(num)
    if numeros:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números es: {promedio}")
    else:
        print("No se ingresaron números.")

def maximo_minimo():
    n = int(input("Ingrese la cantidad de números enteros: "))
    numeros = [int(input(f"Ingrese el número {i + 1}: ")) for i in range(n)]
    if numeros:
        maximo = max(numeros)
        minimo = min(numeros)
        print(f"El valor máximo es: {maximo}")
        print(f"El valor mínimo es: {minimo}")
        print(f"Total de valores introducidos: {len(numeros)}")
    else:
        print("No se ingresaron números.")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Suma de n números")
        print("2. Producto entre n números")
        print("3. División entre 2 números")
        print("4. Factorial de un número")
        print("5. Tablas de multiplicar")
        print("6. Cuadrado y cubo de un número")
        print("7. Promedio de una serie de números")
        print("8. Máximo y mínimo de una serie de números")
        print("0. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == '1':
            suma_numeros()
            time.sleep(3)
        elif opcion == '2':
            producto_numeros()
            time.sleep(3)
        elif opcion == '3':
            division_numeros()
            time.sleep(3)
        elif opcion == '4':
            factorial_numero()
            time.sleep(3)
        elif opcion == '5':
            tablas_multiplicar()
            time.sleep(3)
        elif opcion == '6':
            cuadrado_cubo()
            time.sleep(3)
        elif opcion == '7':
            promedio_numeros()
            time.sleep(3)
        elif opcion == '8':
            maximo_minimo()
            time.sleep(3)
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")


menu()
