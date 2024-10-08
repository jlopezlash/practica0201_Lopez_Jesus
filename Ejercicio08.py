#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la
#<n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
#y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n = int(input('Dime el 1er número'))
m = int(input('Dime el 2o número'))
c = int(n / m)
r = int(n - (m * c))
print('El cociente es', c)
print('El resto es', r)