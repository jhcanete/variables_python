# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
from __future__ import division


print('Ingrese por consola el primer número entero a operar:')
numero_1 = int(input())

print('Ingrese por consola el segundo número entero a operar:')
numero_2 = int(input())

# Alumno: Imprima en pantalla los dos números enteros solicitados
# print(....)



# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma
print ("los numeros seleccionados fueron: ", numero_1, numero_2)
suma = numero_1 + numero_2
print("el resultado de sumar", numero_1, "y", numero_2, "es", suma)

# Resta
print ("los numeros seleccionados fueron", numero_1, numero_2)
resta = numero_1 - numero_2
print("el resultado de restar", numero_1, "y", numero_2, "es", resta)


# División
print ("los numeros seleccionados fueron", numero_1, numero_2)
division = numero_1 / numero_2
print("el resultado de dividir", numero_1, "y ", numero_2, "es", division)

# Multiplicación
print("los numeros seleccionados fueron", numero_1, numero_2)
multiplicacion = numero_1 * numero_2
print("el resultado de multiplicar", numero_1, "y ", numero_2, "es", numero_2, multiplicacion)