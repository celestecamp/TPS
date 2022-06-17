# Escriba una función en Python que permita procesar la información sobre n webinars (charlas online). 
# La función recibirá como parámetro la cantidad de webinars que deben ser procesados (n).
# Por cada webinar, el programa debe solicitar ingresar el título de la actividad y el número de inscriptos. 
# Por ejemplo, una entrada válida del programa sería el valor 77 para el número de inscriptos e 
# “Introducción a Redes Neuronales” para el título.
# Una vez procesados todos los webinars, el programa debe informar:
# El promedio de inscriptos entre todos los webinars.
# Además, la función debe retornar el título del webinar con la menor cantidad de inscriptos y el 
# título del webinar con la mayor cantidad de inscriptos

k = int(input("Cantidad de webinars a procesar:")) #cantidad de veces que se va a iterar el ciclo

def info_webinars(n):
    contador = 1
    sumaInscriptos = 0
    menor = 999 # cantidad menor de inscriptos
    mayor = -1 # cantidad más grandes de inscriptos
    tituloMayor = 0 # el título del webinar con más inscriptos
    tituloMenor = 0 # el título del webinar con menor inscriptos
    while contador <= n: # así se itera la cantidad de veces que pidió el usuario
        titulo = input("Título de la actividad:")
        inscriptos = int(input("Número de inscriptos:"))
        contador +=1 # para ir contando la cantidad de veces que se itera el ciclo
        sumaInscriptos = sumaInscriptos + inscriptos # cada vez que se itera se suma la cantidad de inscriptos a la sumatoria de los de las iteraciones anteriores
        if inscriptos < menor: # si los inscriptos de esta iteración son menos que la cantidad menor ya establecida,
            menor = inscriptos # la nueva cantidad menor de inscriptos será la cantidad que hubo en esta iteración
            tituloMenor = titulo # el título de esta iteración será el título del webinar de cantidad menor de inscriptos
        if inscriptos > mayor: # si los inscriptos son más que los que antes estaban establecidos como la mayor cantidad
            mayor = inscriptos # esta es ahora la mayor cantidad de inscriptos
            tituloMayor = titulo # y el título de este webinar será el título del webinar con mayor cantidad de inscriptos
    promedio = sumaInscriptos / n # la suma de todos los inscriptos dividida por la cantidad de webinars que se registraron (cantidad de iteraciones)
    return (f"El promedio es {promedio}. El webinar con la mayor cantidad de inscriptos es {tituloMayor}, y el webinar con la menor cantidad es {tituloMenor}.")

print(info_webinars(k))

# Escriba una función en Python que reciba como parámetros dos números naturales n y m, 
# donde n < m, (no hace falta validar) y retorne el producto de todos los números entre 
# n y m ellos incluidos. 
# E1: n=2, m=4, resultado=2*3*4=24
# E2: n=1, m=2, resultado=1*2=2

def producto_entre_numeros(n, m):
    """NO le des bola a donde te dice que n < m si te dice que no hace falta validar, lo ponen para que te marees?"""
    producto = 1 # inicializo la variable. Con 1 ya que no me cambia nada, cualquier numero multiplicado por 1 da lo mismo, pero si pusiera 0 las multiplicaciones me darían 0.
    for i in range(n,m+1): # va a recorrer cada elemento que se encuentra entre los dos números que le dimos.
        """ponemos m+1 ya que en la función RANGE no se incluye al último número, si pongo de 1 a 4 me va a contar 1, 2 y 3"""
        producto = producto * i # en cada iteración se sustituye el valor de PRODUCTO por el resultado de su multiplicación por el elemento que se está recorriendo.
    return producto

print(producto_entre_numeros(2,4)) # elegimos 2 valores cualquiera. elegi estos pq en la consigna está el resultado y quería ver si me daba bien.
