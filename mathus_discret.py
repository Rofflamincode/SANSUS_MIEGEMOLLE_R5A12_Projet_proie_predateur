from euler_population_models import *
import matplotlib.pyplot as plt

# -----------------------------------------
# Récupération des valeurs via Euler et analytique
# -----------------------------------------
x0 = 10.0                                       # population initiale
r = 0.5                                         # taux de reproduction
t1 = 10                                         # temps final
h = 0.05
K = 200                                      # pas de temps
t, x_euler = euler(malthus_rhs(r), t1, x0, h)   # résultat de la solution numérique de malthus
x_exact = malthus_analytic(x0, r, t)            # résultat de la solution analytique de malthus
x_euler_verhulst = euler(logistic_rhs(r,K), t1, x0, h)[1]   # résultat de la solution numérique de malthus

# -----------------------------------------
# Affichage graphique des résultat
# -----------------------------------------
plt.figure()
plt.plot(t, x_exact, label="Solution analytique", color="black")
plt.plot(t, x_euler, label="Méthode d'Euler", color="red")
plt.plot(t, x_euler_verhulst, label="Méthode d'Euler Verhulst", color="purple")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Malthus : comparaison Euler vs analytique")
plt.legend()
plt.grid()
plt.show()