#----------------------------------Librerías----------------------------------#
import random as ran
import matplotlib.pyplot as plt
import numpy as np
#-----------------------------------Reglas-----------------------------------#
APUESTAS = (1,2,3,4,6,12,18) 
PAGOS = (35,17,11,8,5,2,1)
#-----------------------------------Métodos-----------------------------------#
def juego(apuesta,cantidad):
    """
    INPUT: Recibe un indice que indica que apuesta se quiere realizar y la 
    cantidad que se va a apostar
    
    OUTPUT: Devuelve el resultado de la apuesta
    """
    ruleta = ran.randint(0,36)
    if 0 < ruleta and ruleta <= APUESTAS[apuesta]:
        return cantidad * PAGOS[apuesta]
    else:
        return -cantidad
         
def estrategia(total,cantidad_minima,juegos):
    dinero_actual = total    
    apuesta_obligada = cantidad_minima    
    manos_perdidas = 0
    cantidad_perdida = 0
    proxima_apuesta = 1
    historial = []
    
    while dinero_actual > apuesta_obligada and dinero_actual < 5 + total \
    and juegos >= 0:
        j = juego(proxima_apuesta,apuesta_obligada)
        juegos += -1
        if j<0:
            manos_perdidas += 1
            cantidad_perdida += -j
            proxima_apuesta = decisordeapuesta(manos_perdidas)
            apuesta_obligada = cantidad_perdida/PAGOS[proxima_apuesta]
        else:
            manos_perdidas = 0
            cantidad_perdidad = 0
            proxima_apuesta = 1
            apuesta_obligada = cantidad_minima
        dinero_actual += j
        historial.append(dinero_actual)
    #"plt.plot(historial)"
    #"print(juegos)"
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
    for i in range(1,200):
        print(i)
        total += 1
        res.append(float(total)/simulador(total,1,9999,500000))
    plt.plot(res)
    return max(res)
    

def decisordeapuesta(a):
    if a != 0:
        for i,p in enumerate(PAGOS):
            if a % p == 0:
                return i
    else:
        return 6

"""
def estrategia(limite_economico,limite_temporal):

    dinero_actual = limite_economico
    apuesta_obligada = 1
    manos_perdidas = 0
    historial = []

    while apuesta_obligada < dinero_actual and dinero_actual < 1.1 * limite_economico and 0 <= juegos:
        j = juego(decisordeapuesta(manos))
        """
        
        
        
        
        

     
        
        
        
    
    
