#----------------------------------Librerías----------------------------------#
import random as ran
import matplotlib.pyplot as plt
import numpy as np
#-----------------------------------Reglas---------------------------------#
APUESTAS = (1,2,3,4,6,12,18,24) 
PAGOS = (36,17,11,8,5,2,1,0.5)
#-----------------------------------Métodos-----------------------------------#
def jugada(cantidad_perdida):
    """
    INPUT: la cantidad de pasta que llevas palmad
    
    OUTPUT: una tupla que te dice  el indice de la
    apuesta que tienes que jugar y cuanto tienes que apostar 
    """
    if cantidad_perdida != 0:
        for i,p in enumerate(PAGOS[:-1]):
            if cantidad_perdida % p == 0:
                return (i, cantidad_perdida / p)
    else:
        return (7,1)

def juego(tupla_apuesta_cantidad):
    """
    INPUT: Recibe una tupla con el indice de la apuesta que se va a realizar y
    la pasta que vas a echar
    
    OUTPUT: Devuelve el resultado de la apuesta
    """
    ruleta = ran.randint(0,36)
    if 0 < ruleta and ruleta <= APUESTAS[tupla_apuesta_cantidad[0]]:
        return tupla_apuesta_cantidad[1] * PAGOS[tupla_apuesta_cantidad[0]]
    else:
        return -tupla_apuesta_cantidad[1]

def estrategia(total, juegos=100, cantidad_minima=1):

    dinero_actual = total    
    cantidad_perdida = 0
    historial = [total]

    while dinero_actual >= jugada(cantidad_perdida)[1] \
    and dinero_actual < 5 * cantidad_minima + total \
    and juegos > 0:
        j = juego(jugada(cantidad_perdida))
        juegos += -1
        if j < 0:
            cantidad_perdida += -j
        else:
            cantidad_perdidad = 0
        dinero_actual += j
        historial.append(dinero_actual)
#    plt.plot(historial)
#    print(juegos)
    return dinero_actual
    
def simulador(total, cantidad_minima=1, juegos=1000, numero_de_simulaciones=500):
    res = []   
    for i in range(numero_de_simulaciones):
        estrategia(total,cantidad_minima,juegos)
        res.append(estrategia(total,cantidad_minima,juegos))
    return np.average(res)
    
def calibrador():
    res = []
    total = 1    
    for i in range(1,20000):
        print(i)
        total += 1
        res.append(simulador(total)/float(total))
    plt.plot(res)
    return max(res)
