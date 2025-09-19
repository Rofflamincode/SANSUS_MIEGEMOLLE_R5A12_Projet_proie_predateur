import numpy as np

# -----------------------------------------
# Fontion Euler -> permet d'approximer numériquement la solution d'une équation
#
# Paramètres
# f(t, y) -> focntion qui définit le système différentiel (le second membre)
# t1 -> temps final
# y0 -> condition initiale (peut être scalaire ou un vecteur), exemple : nombre d'individu au début de l'expérience
# h -> pas de discrétisation
#
# Retour
# le vecteur des temps et les solutions approchées Y
# -----------------------------------------
def euler(f, t1, y0, h):
    N = int(round(t1 / h))
    t_vals = np.linspace(0.0, N*h, N+1)
    y = np.array(y0)
    Y = np.zeros((t_vals.size, y.size if y.ndim else 1))
    for i, t in enumerate(t_vals):
        Y[i] = y if y.ndim else [y]
        y = y + h * np.array(f(t, y))
    return t_vals, Y.squeeze()

# -----------------------------------------
# Fonction malthus_rhs -> Fournit le membre de droite de l'équation de Malthus
#
# Paramètre
# r -> taux de croissance
#
# Retour
# f(t, x) = r * x
# -----------------------------------------
def malthus_rhs(r):
    return lambda t, x: r * x

# -----------------------------------------
# Fonction malthus_analytic -> Calcul la solution analytique exacte du modèle de Malthus
#
# Paramètre
# x0 -> population initiale
# r -> taux de croissance
# t -> vecteur de temps
#
# Retour
# valeur exacte N(t)
# -----------------------------------------
def malthus_analytic(x0, r, t):
    return x0 * np.exp(r * t)

# -----------------------------------------
# Fonction verhulst_rhs -> Donne le membre de droite de l'équation de verhulst
#
# Paramètre
# r -> taux de croissance
# K -> capacité de charge (seuil maximal stable)
#
# Retour
# f(t, x) = r * x(1 - x/K)
# -----------------------------------------
def verhulst_rhs(r, K):
    return lambda t, x: r * x * (1.0 - x / K)

# -----------------------------------------
# Fonction lotka_volterra_rhs -> Donne le système différentiel du modèle proie-prédateur de Lotka-Volterra
#
# Paramètre
# a -> taux de croissance naturel des proie
# b -> taux de prédation du prédateur sur la proie
# c -> taux de mortalité du prédateur en l'absence de proie
# d -> taux de croissance du prédateur du fait de sa prédation
#
# Retour
# un fonction qui, à partir de (t, [x, y]), renvoie le vecteur (N', P')
# -----------------------------------------
def lotka_volterra_rhs(a, b, c, d):
    def f(t, XY):
        x, y = XY
        return np.array([a * x - b * x * y, -c * y + d * x * y])
    return f
