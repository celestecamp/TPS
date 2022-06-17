# Escriba una función en Python que permita procesar el título y la cantidad de visualizaciones de 150 videos de Youtube. Por ejemplo, una
# entrada válida del programa sería "Manejo de Listas" para el título y 2500 para las visualizaciones. Una vez procesados todos los
# videos, el programa debe informar:
# a) el promedio de visualizaciones de los videos
# b) indicar (por sí o por no) si algún video posee como título "Boca Campeón 2022"
# c) el título del video con mayor cantidad de visualizaciones.

def videos_youtube():
    contador = 1 # para contar la cantidad de veces que vamos a iterar
    promedioSuma = 0 # donde vamos a ir sumando las visualizaciones de cada video para después sacar el promedio.
    visualizaciones_mayor = 0 # la mayor cantidad de visualizaciones que le pasas.
    s = "Boca Campeón 2022" # esto podes ponerlo acá como una variable o adentro del código pero a mi me dio paja y quería que quede más prolijo así que lo puse en una variable y adentro del código lo único que puse fue s.
    while contador <= 3: # la consigna te pide que lo hagan 150 veces, pero para poder probar el código y no tener q andar metiendo 150 títulos y visualizaciones le puse 3. En el parcial escribis el número q te dieron.
       
        titulo = input("Título del video:")
        visualizaciones = int(input("Número de visualizaciones:"))
        contador += 1
        promedioSuma = promedioSuma + visualizaciones # ahora la suma va a ser el valor que ya tenía + las visualizaciones de este nuevo video.
        
        if s in titulo: # si en el título aparece "Boca Campeón 2022" se ejecuta lo siguiente:
            existe = "Si" # creé una variable a la cual le asigné este string "sí", ya que sí se encuentra ese string en el título.
        else: # si no está ese string en el título, se ejecuta:
            existe = "No"
        
        if visualizaciones > visualizaciones_mayor: # Si la cantidad de visualizaciones que le pasaste en este video es mayor a la cantidad ya establecida como mayor:
            visualizaciones_mayor = visualizaciones # ahora esta va a ser la nueva cantidad mayor de visualizaciones
            titulo_mayor = titulo # y su título va a ser el título del video con la mayor cantidad de visualizaciones.
    
    promedioFinal = promedioSuma / 3 # cuando ya se iteró todas las veces que le dijimos, agarra la suma que se fue haciendo durante el ciclo y lo divide por la cantidad de videos ingresados (debería ser 150)
    
    return promedioFinal, existe, titulo_mayor

print(videos_youtube())


# Escriba una función que reciba un string como parámetro y retorne un booleano que identifique si existe la letra "a" en el mismo. Por
# ejemplo, si la función recibe "Programación" retornará True.

def existe_a(s):

    existe = False # lo inicializamos en False ya que esto cambiará solo si se cumple la siguiente condición:
    contador = 0

    for letra in s: # se fija en cada letra del string que le damos:
        if letra == "a": # si la letra es A
            contador += 1 # le agrego 1 al contador. es lo mismo que contador = contador + 1
    
    if contador > 0: # una vez que se fijó en todas las letras, si por lo menos una fue a, o sea que el contador sumó 1 por lo menos una vez,
        existe = True # cambiamos el booleano de "existe"
    
    return existe

print(existe_a("Hola")) # le damos el string que queramos y lo analiza. Si tiene A retorna True.


# Escriba una función en Python que reciba como parámetro una lista y retorne la cantidad de elementos positivos y negativos. Así, si
# por ejemplo la función recibe la lista L = [5, 9, -10, 11, 3, 8, 21, -2] deberá retornar 6 y 2 respectivamente.

"""NO FUNCIONA"""
lista = [1,2,3,-5,-9]

def pos_o_neg(L):
    
    lista = []
    cantidad_negativos = 0
    cantidad_positivos = 0
    
    for numero in lista:
        if numero > 0:
            cantidad_positivos += 1
        if numero < 0:
            cantidad_negativos += 1

    return cantidad_positivos, cantidad_negativos


print(pos_o_neg(lista))