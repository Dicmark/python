'''Pedir 3 valores enteros por consola, guardarlos en una variable y luego hacer los siguientes calculos
calculo1: La suma del valor 1 con el valor 3
calculo2: La division del calculo1 con el valor 2
Imprimir ambos resultados y el tipo de dato correspondiente a cada calculo'''

n1=int(input("Ingrese el primer valor: "))
n2=int(input("Ingrese el primer valor: "))
n3=int(input("Ingrese el primer valor: "))

calculo1= n1 + n3
calculo2= float(calculo1/n2)

print(f"El resultado de sumar el valor 1 ",n1," + el valor 3 ",n3, " es: ",calculo1, " el resultado es de tipo ",type(calculo1))
print(f"El resultado de dividir el valor ",calculo1," dividido el valor ",n2," es: ",calculo2," el resultado es de tipo ",type(calculo2))