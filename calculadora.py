# Calculadora simple en Python

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

def mostrar_menu():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    mostrar_menu()
    
    # Tomar la entrada del usuario
    operacion = input("Introduce el número de la operación (1/2/3/4/5): ")
    
    if operacion == '5':
        print("¡Gracias por usar la calculadora!")
        break
    
    if operacion in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            
            if operacion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif operacion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif operacion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif operacion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
        except ValueError:
            print("Por favor, ingresa números válidos.")
    else:
        print("Opción no válida. Intenta de nuevo.")
