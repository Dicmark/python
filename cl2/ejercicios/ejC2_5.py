'''5-	Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales. round(numero, 2) 
'''
peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en metros: "))
imc = round((peso/altura),2)

print(f"Su indice de IMC es de: ",imc)