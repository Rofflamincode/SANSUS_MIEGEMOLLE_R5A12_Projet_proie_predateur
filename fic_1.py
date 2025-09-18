# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 11:35:05 2025

@author: Mathys SANSUS & Romain MIEGEMOLLE
"""

"""
def malthus1(nombre_individu_initial, nombre_periode, taux_reproduction):
    nombre_individu = nombre_individu_initial
    print("Initial : ", nombre_individu, "individus")
    for i in range(nombre_periode):
        nombre_individu += nombre_individu * taux_reproduction
        print("Période n° ", i+1, " : ", nombre_individu, " individus")"""
        

import matplotlib.pyplot as plt

def malthus(nombre_individu_initial, nombre_periode, taux_reproduction):
    individus = [nombre_individu_initial]
    
    nombre_individu = nombre_individu_initial
    for _ in range(nombre_periode):
        nombre_individu += nombre_individu * taux_reproduction
        individus.append(nombre_individu)
    
    # Visualisation
    plt.figure(figsize=(10, 6))
    plt.plot(individus, label="Population", linewidth=2, color="blue")
    plt.title("Modèle Malthusien de Croissance")
    plt.xlabel("Période")
    plt.ylabel("Nombre d'individus")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()
    
def verhulst(nombre_individu_initial, nombre_periode, taux_reproduction, carrying_capacity):
    individus = [nombre_individu_initial]
    
    nombre_individu = nombre_individu_initial
    for _ in range(nombre_periode):
        nombre_individu += nombre_individu * taux_reproduction * (1 - (nombre_individu/carrying_capacity))
        individus.append(nombre_individu)
    
    # Visualisation
    plt.figure(figsize=(10, 6))
    plt.plot(individus, label="Population", linewidth=2, color="blue")
    plt.title("Modèle Verhulstien de Croissance")
    plt.xlabel("Période")
    plt.ylabel("Nombre d'individus")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()
    
def comparaison_malthus_verhulst(nombre_individu_initial, nombre_periode, taux_reproduction, carrying_capacity):
    individus_malthus = [nombre_individu_initial]
    individus_verhulst = [nombre_individu_initial]
    
    nombre_individu_malthus = nombre_individu_initial
    nombre_individu_verhulst = nombre_individu_initial
    for _ in range(nombre_periode):
        nombre_individu_malthus += nombre_individu_malthus * taux_reproduction
        nombre_individu_verhulst += nombre_individu_verhulst * taux_reproduction * (1 - (nombre_individu_verhulst/carrying_capacity))
        individus_malthus.append(nombre_individu_malthus)
        individus_verhulst.append(nombre_individu_verhulst)
    
    # Visualisation
    plt.figure(figsize=(10, 6))
    plt.loglog(individus_malthus, label="Malthus", linewidth=2, color="blue")
    plt.loglog(individus_verhulst, label="Verhulst", linewidth=2, color="red")
    plt.title("Comparaison du modèle Malthusien et Verhulstien")
    plt.xlabel("Période")
    plt.ylabel("Nombre d'individus")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()



malthus(10, 10, 0.5)
"""
verhulst(100, 200, 0.05, 10000)
"""

"""comparaison_malthus_verhulst(100, 200, 0.05, 10000)"""