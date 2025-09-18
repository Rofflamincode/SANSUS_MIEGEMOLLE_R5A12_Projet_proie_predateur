# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 09:06:19 2025

@author: mathy
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Paramètres du modèle
# ----------------------------
r = 0.5        # taux de croissance
N0 = 10        # population initiale
T = 10         # temps final
h = 1      # pas de temps
n_steps = int(T/h)  # nombre d'itérations

# ----------------------------
# Méthode d'Euler pour Malthus
# ----------------------------
t_vals = np.linspace(0, T, n_steps+1)
print(t_vals)
N_euler = np.zeros(n_steps+1)
N_euler[0] = N0

for k in range(n_steps):
    N_euler[k+1] = N_euler[k] + h * (r * N_euler[k])  # Euler

# ----------------------------
# Solution analytique
# ----------------------------
N_exact = N0 * np.exp(r * t_vals)

# ----------------------------
# Affichage
# ----------------------------
plt.figure(figsize=(8,5))
plt.plot(t_vals, N_exact, 'g-', label="Solution analytique")
plt.plot(t_vals, N_euler, 'ro--', label="Méthode d'Euler")
plt.xlabel("Temps t")
plt.ylabel("Population N(t)")
plt.title("Modèle de Malthus : comparaison Euler vs analytique")
plt.legend()
plt.grid()
plt.show()