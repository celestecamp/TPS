"""Cómo hacer una función???"""


# Vamos a hacer una que sume dos números que se le da.

def funcion(n1, n2): # cuando le pones los parámetros así, desp cuando llames a la función vas a poder ponerle los números que quieras.
    suma = n1 + n2
    return suma

""" Nunca va a funcionar si no la llamas. No pasa absolutamente nada. """

print(funcion(2,3)) # = 5

# entre los paréntesis sustituis los parámetros por el valor que le quieras dar vos. Python toma como que el primer número que metes
# corresponde al primer argumento que le diste a la función, el segundo que metes lo relaciona con el segundo que le diste, etc.

print(funcion(5,6)) # = 11



"""NO podes hacer una función sin parámetros y pasarle alguno, o al revés. Siempre le tenes que pasar la misma cantidad de parámetros
que le dijiste que le ibas a pasar."""

def funcionsinparametros():
    suma = n3 + n4
    return suma

n3 = 2
n4 = 1

print(funcionsinparametros()) # retorna el resultado de la suma entre los números que pusimos afuera de la función, o adentro

print(funcionsinparametros(2,1)) # te va a decir que la función espera 0 parámetros y le pasaste 2.


# por lo general en el examen te dicen tipo "hace una función que recibe tal y tal como parámetro" así que no te vas a confundir tanto.