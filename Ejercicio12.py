#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
#Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca
#y la ganancia final total.
Pan = int(input('¿Cuantas barras de pan tienes?'))
print('El precio de cada barra es de 3.49')
print('El descuento es del 60%')
Ganancia = float((3.49 * 60) / 100) * Pan
Ganancia = round(Ganancia,2)
print('La ganancia total es de', Ganancia)