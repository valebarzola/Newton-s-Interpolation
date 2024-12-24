

import numpy as np

#esta funcion me permite obtener los puntos x,y del usuario.
def obtener_puntos():
    x=[]
    y=[]
    while True:
        punto=input()
        
        if punto.lower() == "e":

            break

        try:
            x_i, y_i = map(float, punto.split(','))
            x.append(x_i)
            y.append(y_i)

        except ValueError:
            print("Entrada inválida. Por favor, ingrese el punto en el formato 'x, y'.")

    
    return x,y 


#calculo de las diferencias y devolucion de tabla
def diferencias_dividas(x, y):
    n = len(x)
    #creo una matriz f cuadrada llena de 0
    f = np.zeros((n, n))
    # La primera columna de f son los elementos de y
    f[:,0] = y
    
    # Calcular las diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x[i + j] - x[i])
    

    
    return f

#formacion del polinomio y aproximacion de xi 
def polinomio(x, y, xi):
    f = diferencias_dividas(x, y)
    n = len(x)
    result = f[0, 0]
    product_term = 1.0
    
    for i in range(1, n):
        #diferencia de valor xi(usuario) y xij
        product_term *= (xi - x[i - 1])
        #suma de terminos de los productos formados y elementos de la tabla
        result += f[0, i] * product_term
    
    return result
        

    


