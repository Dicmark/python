'''3-	Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''
hora = int(input("¿Cuantas horas trabaja? "))
importe = int(input("¿Cuanto vale la hora? "))

resultado = hora * importe

print(f"Se le deben abonar $",resultado)