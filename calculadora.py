n1 = float(input("Introduce un numero: "))
n2 = float(input("Introduce un segundo numero: "))

def suma (numero1, numero2):
    resultado = numero1 + numero2
    return resultado
    
def resta (numero1,numero2):
    resultado = numero1-numero2
    return resultado

def multiplicacion (juanito1, juanito2):
    return juanito1*juanito2

def division (pollito1, pollito2):
    plato = pollito1/pollito2
    return plato

def cambiar_valor():
    n1 = float(input("Introduce un numero: "))
    n2 = float(input("Introduce un segundo numero: "))

    return n1,n2


condicion = True
opcion = 0
while condicion == True:
    print("""
    ¿Que operacion desea utilizar?
    
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Cambiar Valores
    6) Cerrar Calculadora
    """)
    opcion = int(input("Elige una de estas operaciones: "))

    if opcion == 1:
        print(" ")
        print("La suma es: {}".format(suma(n1,n2)))
    elif opcion == 2:
        print(" ")
        print(resta(n1,n2))
    elif opcion == 3:
        print(" ")
        print(multiplicacion(n1,n2))
    elif opcion == 4:
        print(" ")
        print(division(n1,n2))
        if n2 == 0:
            print("No se puede dividir entre cero")
    elif opcion == 5:
        n1,n2 = cambiar_valor()
    elif opcion == 6:
        print("Cerrando programa")
        condicion = False
    else:
        print("Opcion incorrecta")
    
    