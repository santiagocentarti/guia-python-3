#Leer 10 números enteros e imprimir el promedio, el mayor y menor ingresado.
#santiago centarti
#aplicaciones informaticas
#santiagocentarti@gmail.com

suma = 0
mayor = 0
menor = 0

for i in range(10):
    numero = int(input("Ingrese un numero entero: "))
    suma += numero
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero

promedio = suma / 10

print(f"El promedio es {promedio}, el mayor numero es {mayor}, el menor numero es {menor}")
