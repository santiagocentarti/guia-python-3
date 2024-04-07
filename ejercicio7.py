#Leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado. Ejemplo: 4*3 = 4 + 4 + 4 (4 sumado 3 veces).
#santiago centarti
#aplicaciones informaticas
#santiagocentarti@gmail.com

a = int(input("Ingrese el numero A(entero positivo): "))
b = int(input("Ingrese el numero B(entero positivo): "))

suma = 0

if a <= 0 or b<= 0:
    print("Ambos números deben ser enteros positivos.")
else:
    for i in range(b):
        suma += a
print(f"El producto de {a} * {b} por sumas sucesivas es: {suma}")

