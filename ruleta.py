#----------------------------------Librerías----------------------------------#
import random as ran
import matplotlib.pyplot as plt
import numpy as np

#-----------------------------------Reglas-----------------------------------#

combinaciones = {}
combinaciones["Doble Docena o Doble Columna a Caballo"] = 24
combinaciones["Suertes sencillas"] = 18
combinaciones["Columna o Docena"] = 12
combinaciones["Seisena o Doble fila transversal"] = 6
combinaciones["Cuadro"] = 4
combinaciones["Transversal"] = 3
combinaciones["Caballo o Pareja"] = 2
combinaciones["Pleno"] = 1

APUESTAS = (1,2,3,4,6,12,18) 
PAGOS = (35,17,11,8,5,2,1)
RELACION = zip(APUESTAS,PAGOS)


#-----------------------------------Métodos-----------------------------------#
def juego(apuesta,cantidad):
    """
    INPUT: Recibe una lista con los numeros a los que se apuesta y otra con la 
    cantidad apostada
    
    OUTPUT: Devuelve el resultado de la apuesta
    """

    
    if combinaciones.has_key(apuesta):
        ruleta = ran.randint(0,36)
        if ruleta != 0 and ruleta <= combinaciones[apuesta]:
            return cantidad*(36-combinaciones[apuesta])/combinaciones[apuesta]
        else:
            return -cantidad
    else:
        print("ERROR: Introduzca una apuesta válida")



def selector(perdidas):
    """
    if perdidas == 0:
        return "Doble Docena o Doble Columna a Caballo"
    """
    if perdidas == 0:
        return "Suertes sencillas"
    elif perdidas == 1:
        return "Suertes sencillas"
    elif perdidas == 2:
        return "Columna o Docena"
    elif perdidas >= 3 and perdidas <= 5:
        return "Seisena o Doble fila transversal"
    elif perdidas >= 6 and perdidas <= 8:
        return "Cuadro"  
    elif perdidas >=9 and perdidas <= 11:
        return "Transversal"
    elif perdidas >= 12 and perdidas <= 17:
        return "Caballo o Pareja"
    elif perdidas >= 18 and perdidas <= 35:
        return "Pleno"
    else:
        "Pleno"

          
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
        
        
        
        
        

     
        
        
        
    
    
