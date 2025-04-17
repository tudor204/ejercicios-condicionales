"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
"""
n = float(input("introduce el dividendo "))
n1 = float(input("introduce el divisor "))
if n1 == 0:
    print("No se puede dividir 0")
else:
    print(n/n1)