#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#  calcule el índice de masa corporal y lo almacene en una variable,
#  y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc>
#  es el índice de masa corporal calculado redondeado con dos decimales.
kg = float (input('¿Cuanto pesas?'))
m = float (input('¿cuanto mides?'))
imc = (kg /(m ** 2))
imc = round(imc,2)  #Round es un comando para redondear
print('Tu índice de masa corporal es', imc)