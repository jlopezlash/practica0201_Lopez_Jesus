#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
Dinero = int(input('¿Cuánto quieres invertír?'))
Interes = float(input('¿Cuánto es el interes anual?'))
Años = int(input('¿Durante cuantos años?'))
Capital = (((Dinero * Interes) / 100) * Años)
print('Inversion obtenida es de', Capital)