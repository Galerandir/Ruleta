#----------------------------------Librerías----------------------------------#
import random as ran
import matplotlib.pyplot as plt
import numpy as np

#-----------------------------------Reglas-----------------------------------#

combinaciones = {}
combinaciones["rojo"] = ((1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36),1)
combinaciones["negro"] = ((2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35),1)
combinaciones["par"] = ((2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36),1)
combinaciones["impar"] = ((1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35),1)
combinaciones["falta"] = ((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),1)
combinaciones["pasa"] = ((19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36),1)
combinaciones["1d12"] = ((1,2,3,4,5,6,7,8,9,10,11,12),2)
combinaciones["2d12"] = ((13,14,15,16,17,18,19,20,21,22,23,24),2)
combinaciones["3d12"] = ((25,26,27,28,29,30,31,32,33,34,35,36),2)
combinaciones["1C"] = ((1,4,7,10,13,16,19,22,25,28,31,34),2)
combinaciones["2C"] = ((2,5,8,11,14,17,20,23,26,29,32,35),2)
combinaciones["3C"] = ((3,6,9,12,15,18,21,24,27,30,33,36),2)
for i in range(1,37):
    combinaciones[str(i)] = (tuple([i]),35)
    

#-----------------------------------Métodos-----------------------------------#
def juego(apuesta,cantidad):
    """
    INPUT: Recibe una lista con los numeros a los que se apuesta y otra con la 
    cantidad apostada
    
    OUTPUT: Devuelve el resultado de la apuesta
    """

    
    if combinaciones.has_key(apuesta):
        ruleta = ran.randint(0,36)
        if ruleta in combinaciones[apuesta][0]:
            return cantidad*combinaciones[apuesta][1]
        else:
            return -cantidad
    else:
        print("ERROR: Introduzca una apuesta válida")
        
def estrategia(total,cantidad_minima,juegos):
    dinero_actual = total    
    apuesta_obligada = cantidad_minima    
    manos_perdidas = 0
    historial = []
    
    while dinero_actual > apuesta_obligada and dinero_actual <1.1*total and juegos >= 0:
        j = juego("1",apuesta_obligada)
        juegos += -1
        if j<0:
            manos_perdidas += 1
        else:
            manos_perdidas = 0
        dinero_actual += j    
        apuesta_obligada = cantidad_minima * ( 2**(manos_perdidas/36))
        historial.append(dinero_actual)
    plt.plot(historial)
    return dinero_actual
    
def simulador(total,cantidad_minima,juegos,numero_de_simulaciones):
    res = []   
    for i in range(numero_de_simulaciones):
        estrategia(total,cantidad_minima,juegos)
        res.append(estrategia(total,cantidad_minima,juegos))
    return np.average(res)
    
def calibrador():
    res = []
    total = 1    
    for i in range(1,20):
        total += 1
        res.append(float(total)/simulador(total,0.2,9999,500))
    plt.plot(res)
    return max(res)

def estrategia1(total,juegos):
    dinero_actual = total    
    apuesta_obligada = 1    
    manos_perdidas = 0
    historial = []
    
    while dinero_actual > apuesta_obligada and dinero_actual <1.1*total and juegos >= 0:
        
    
    
    
