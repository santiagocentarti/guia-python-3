#Escribir un programa en Python que lea números enteros hasta que se ingrese un 0, y muestre el máximo, el mínimo y el promedio de todos ellos. 
#santiago centarti
#aplicaciones informaticas
#santiagocentarti@gmail.com

suma = 0
mayor = 0
menor = 0
numero = 1

while(numero != 0):
    numero = int(input("Ingrese un numero entero, ponga 0 si desea terminar: "))
    suma += numero
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero
promedio = suma / 10

print(f"El promedio es {promedio}, el mayor numero es {mayor}, el menor numero es {menor}")