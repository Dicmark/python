'''7-	Una panadería vende barras de pan a 35$ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
Ejemplo:
Precio del pan:
Descuento:
Precio del pan con descuento incluido: 
'''
pan = int(input("Ingrese la cantidad de panes: "))
totalPan = pan * 35 
desc = totalPan * 0.6

print(f"El precio del pan fresco es de: $",totalPan)
print(f"Al no ser pan del dia de hoy, el mismo tiene un descuento del 60% que equivale a $",desc)
print(f"El precio total a abonar con el descuento incluido es de $",(totalPan - desc))