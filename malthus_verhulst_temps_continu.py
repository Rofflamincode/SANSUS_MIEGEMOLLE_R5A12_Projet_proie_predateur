import matplotlib.pyplot as plt

# -----------------------------------------
# Fontion malthus -> permet d'afficher graphiquement les résultats en temps continu du modèle de Malthus
#
# Paramètres
# x0 -> nombre d'individu initial
# t1 -> nombre de période 
# r -> taux de croissance
# -----------------------------------------
def malthus(x0, t1, r):
    individus = [x0]
    
    nombre_individu = x0
    for _ in range(t1):
        nombre_individu += nombre_individu * r
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
    
# -----------------------------------------
# Fontion verhulst -> permet d'afficher graphiquement les résultats en temps continu du modèle de Verhulst
#
# Paramètres
# x0 -> nombre d'individu initial
# t1 -> nombre de période 
# r -> taux de croissance
# K -> capacité de charge (seuil maximal stable)
# -----------------------------------------
def verhulst(x0, t1, r, K):
    individus = [x0]
    
    nombre_individu = x0
    for _ in range(t1):
        nombre_individu += nombre_individu * r * (1 - (nombre_individu/K))
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

# -----------------------------------------
# Fontion comparaison_malthus_verhulst -> permet d'afficher graphiquement les résultats en temps continu des modèles de Malthus et Verhulst
#
# Paramètres
# x0 -> nombre d'individu initial
# t1 -> nombre de période 
# r -> taux de croissance
# K -> capacité de charge (seuil maximal stable)
# -----------------------------------------
def comparaison_malthus_verhulst(x0, t1, r, K):
    individus_malthus = [x0]
    individus_verhulst = [x0]
    
    nombre_individu_malthus = x0
    nombre_individu_verhulst = x0
    for _ in range(t1):
        nombre_individu_malthus += nombre_individu_malthus * r
        nombre_individu_verhulst += nombre_individu_verhulst * r * (1 - (nombre_individu_verhulst/K))
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


# -----------------------------------------
# Test
# -----------------------------------------

"""
malthus(10, 10, 0.5)
verhulst(10, 10, 0.5, 200)
"""

comparaison_malthus_verhulst(10, 10, 0.5, 200)