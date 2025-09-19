from euler_population_models import *
import matplotlib.pyplot as plt

# -----------------------------------------
# Récupération des valeurs via Euler et analytique
# -----------------------------------------
x0 = 10.0                                       # population initiale (proies)
y0 = 5.0                                        # population initiale (prédateur)
r = 0.5                                         # taux de reproduction
t1 = 60                                         # temps final
h = 0.01                                        # pas de temps
K = 15000                                       # capacité de charge (seuil maximal stable)
a = 1                                           # taux de croissance naturel des proie
b = 0.1                                         # taux de prédation du prédateur sur la proie
c = 1.5                                         # taux de mortalité du prédateur en l'absence de proie
d = 0.075                                       # taux de croissance du prédateur du fait de sa prédation
t, x_euler = euler(malthus_rhs(r), t1, x0, h)                           # résultat de la solution numérique de malthus
x_exact = malthus_analytic(x0, r, t)                                    # résultat de la solution analytique de malthus
x_euler_verhulst = euler(verhulst_rhs(r,K), t1, x0, h)[1]               # résultat de la solution numérique de malthus
XY = euler(lotka_volterra_rhs(a, b, c, d), t1, [x0, y0], h)[1]          # résultat de la solution numérique de malthus
x_lv = XY[:, 0]
y_lv = XY[:, 1]

# -----------------------------------------
# Affichage graphique des résultat
# -----------------------------------------
plt.figure()
plt.loglog(t, x_exact, label="Solution analytique", color="black")
plt.loglog(t, x_euler, "--", label="Méthode d'Euler", color="red")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Malthus : comparaison Euler vs analytique")
plt.legend()
plt.grid()
plt.show()

# -----------------------------------------
# Verhulst
# -----------------------------------------
plt.figure()
plt.plot(t, x_euler_verhulst, label="Méthode d'Euler Verhulst", color="purple")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Verhulst")
plt.legend()
plt.grid()
plt.show()

# -----------------------------------------
# Lotka–Volterra
# -----------------------------------------
plt.figure()
plt.plot(t, x_lv, label="Méthode d'Euler Lotka Volterra - proies", color="green")
plt.plot(t, y_lv, label="Méthode d'Euler Lotka Volterra - prédateurs", color="blue")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Lotka Volterra")
plt.legend()
plt.grid()
plt.show()