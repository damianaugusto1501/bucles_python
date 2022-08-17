# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

from operator import truediv
import string


print("Mi Calculadora (^_^)")

# Empezar aquí la resolución del ejercicio

bucle = 1
resultado = 0
pregunta = string


while bucle == 1 :
    numero_1 = int(input('Ingrese el primer número de la calculadora\n'))
    operador = str(input("Ingrese operador matematico : simbolos +,-,*,/,**\n"))

    if operador != "+" and operador != "-" and operador != "/" and operador != "*" and operador != "**" :
        print ("el operador no es correcto")

    numero_2 = int(input('Ingrese el segundo número de la calculadora\n'))

    if operador == "+" :
        resultado = numero_1 + numero_2
        print ("el resultado de sumar es : ",resultado)
    elif operador == "-" :
        resultado = numero_1 - numero_2
        print ("el resultado de restar es : ",resultado)
    elif operador == "*" :
        resultado = numero_1 * numero_2
        print ("el resultado de multiplicar es : ",resultado)
    elif operador == "/" :
        resultado = numero_1 / numero_2
        print ("el resultado de dividir es : ",resultado)
    elif operador == "**" :
        resultado = numero_1 * numero_2
        print ("el resultado de potenciar es : ",resultado)
    
    
    
        
    pregunta = str.lower(input("ingrese fin si desea salir\n"))

    if pregunta == "fin" :
        break
    else :
        print("el bucle comenzara otra vez")
