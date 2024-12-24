#este programa muestra como podemos aproximar un punto a travez de una funcion. Dado n puntos formamos un polinomio de n-1 grados, que me permitira obtener la proximacion con cierto grado de error al punto buscado.
from funciones import diferencias_dividas,polinomio,obtener_puntos



print("Por favor, escriba los distintos puntos que usaremos para crear el polinomio. Para ello escriba el valor de X, separado de una coma, y luego Y. Ejemplo: x,y ; 2,23. Para finalizar escriba E")
#obtencion de puntos
x,y= obtener_puntos()

if len(x)==len(y):
    print(f"Formaremos un polinomio de grado {len(x)-1}" )
else:
    print("Error, la cantidad de puntos en x y y no es la misma")
    exit()

print (x,y)

#valor a aproximar
xi=input("Por favor,coloque a que valor le gustaria apoximar el polinomio: ")

matriz=diferencias_dividas(x,y)
print("La matriz de diferencias dividas es:")
print(matriz)


print(f"El punto reemplazado en el polinomio es: {polinomio(x,y,float(xi))}")







