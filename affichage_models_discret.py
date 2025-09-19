from population_models import *
import matplotlib.pyplot as plt

# -----------------------------------------
# Récupération des valeurs via Euler et analytique
# -----------------------------------------
x0 = 10.0                                       # population initiale (proies)
y0 = 5.0                                        # population initiale (prédateur)
r = 0.5                                         # taux de reproduction
t1 = 60                                         # temps final
h = 0.1                                         # pas de temps
K = 15000                                       # capacité de charge (seuil maximal stable)
a = 1                                           # taux de croissance naturel des proie
b = 0.1                                         # taux de prédation du prédateur sur la proie
c = 1.5                                         # taux de mortalité du prédateur en l'absence de proie
d = 0.075                                       # taux de croissance du prédateur du fait de sa prédation

t, x_malthus_euler = euler(malthus_rhs(r), t1, x0, h)                       # résultat de la solution numérique de malthus avec Euler
t, x_malthus_rk4 = rk4(malthus_rhs(r), t1, x0, h)                           # résultat de la solution numérique de malthus avec rk4
x_malthus_exact = malthus_analytic(x0, r, t)                                # résultat de la solution analytique de malthus

t, x_verhulst_euler = euler(verhulst_rhs(r,K), t1, x0, h)                   # résultat de la solution numérique de Verhulst avec Euler
t, x_verhulst_rk4 = rk4(verhulst_rhs(r,K), t1, x0, h)                       # résultat de la solution numérique de Verhulst avec rk4

t, XY_euler = euler(lotka_volterra_rhs(a, b, c, d), t1, [x0, y0], h)        # résultat de la solution numérique de Lotka Volterra avec Euler
t, XY_rk4 = rk4(lotka_volterra_rhs(a, b, c, d), t1, [x0, y0], h)            # résultat de la solution numérique de Lotka Volterra avec rk4
x_lv_euler = XY_euler[:, 0]
y_lv_euler = XY_euler[:, 1]
x_lv_rk4 = XY_rk4[:, 0]
y_lv_rk4 = XY_rk4[:, 1]

t, x_phase_euler, y_phase_euler = simulate_lotka_volterra_euler(a, b, c, d, x0, y0, t1, h)  # résultat du portrait de phase de Lotka Volterra avec Euler
t, x_phase_rk4, y_phase_rk4 = simulate_lotka_volterra_rk4(a, b, c, d, x0, y0, t1, h)        # résultat du portrait de phase de Lotka Volterra avec rk4

# -----------------------------------------
# Malthus - Euler
# -----------------------------------------
plt.figure()
plt.loglog(t, x_malthus_exact, label="Solution analytique", color="black")
plt.loglog(t, x_malthus_euler, "--", label="Méthode d'Euler", color="red")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Malthus : comparaison Euler vs analytique")
plt.legend()
plt.grid()
plt.show()

# -----------------------------------------
# Malthus - rk4
# -----------------------------------------
plt.figure()
plt.loglog(t, x_malthus_exact, label="Solution analytique", color="black")
plt.loglog(t, x_malthus_rk4, "--", label="Méthode RK4", color="red")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Malthus : comparaison RK4 vs analytique")
plt.legend()
plt.grid()
plt.show()

# -----------------------------------------
# Verhulst - Euler
# -----------------------------------------
plt.figure()
plt.plot(t, x_verhulst_euler, color="black")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Verhulst - Euler")
plt.grid()
plt.show()

# -----------------------------------------
# Verhulst - rk4
# -----------------------------------------
plt.figure()
plt.plot(t, x_verhulst_rk4, color="black")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Verhulst - rk4")
plt.grid()
plt.show()

# -----------------------------------------
# Lotka–Volterra - Euler
# -----------------------------------------
plt.figure()
plt.plot(t, x_lv_euler, label="Méthode d'Euler Lotka Volterra - proies", color="black")
plt.plot(t, y_lv_euler, label="Méthode d'Euler Lotka Volterra - prédateurs", color="red")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Lotka Volterra - Euler")
plt.legend()
plt.grid()
plt.show()

# -----------------------------------------
# Lotka–Volterra -rk4
# -----------------------------------------
plt.figure()
plt.plot(t, x_lv_rk4, label="Méthode rk4 Lotka Volterra - proies", color="black")
plt.plot(t, y_lv_rk4, label="Méthode rk4 Lotka Volterra - prédateurs", color="red")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Lotka Volterra - rk4")
plt.legend()
plt.grid()
plt.show()

# -----------------------------------------
# Portrait de pahse - Euler
# -----------------------------------------
plt.figure()
plt.plot(x_phase_euler, y_phase_euler,  color="orange")
plt.xlabel("proies")
plt.ylabel("prédateurs")
plt.title("Lotka–Volterra — portrait de phase - Euler")
plt.grid()
plt.show()

# -----------------------------------------
# Portrait de pahse - rk4
# -----------------------------------------
plt.figure()
plt.plot(x_phase_rk4, y_phase_rk4,  color="orange")
plt.xlabel("proies")
plt.ylabel("prédateurs")
plt.title("Lotka–Volterra — portrait de phase - rk4")
plt.grid()
plt.show()