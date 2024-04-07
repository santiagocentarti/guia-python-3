#Mostrar las tablas de multiplicar (entre 1 y 10) del número 3. ¿Qué cambios harías en el algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?
#santiago centarti
#aplicaciones informaticas
#santiagocentarti@gmail.com

numerotabla = int(input("Ingrese el numero del que desea saber su tabla de multiplicar: "))
for i in range(1,11):
    print(f"{numerotabla} x {i} = {numerotabla*i}")


