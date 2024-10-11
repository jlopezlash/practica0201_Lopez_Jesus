#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses,
#que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
#Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
#Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
#Redondear cada cantidad a dos decimales.
Dinero = float(input('¿Cuanto quieres depositar?'))
Interés = float((Dinero * 4)/ 100)
Primero = float(Dinero + Interés)
Segundo = float(Dinero + (Interés * 2))
Tercero = float(Dinero + (Interés * 3))
Primero = round(Primero,2)
Segundo = round(Segundo,2)
Tercero = round(Tercero,2)
print('Despues de 1 año tienes', Primero)
print('Despues de 2 años tienes', Segundo)
print('Despues de 3 años tienes', Tercero)