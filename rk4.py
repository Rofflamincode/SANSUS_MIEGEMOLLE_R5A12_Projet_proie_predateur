from euler_population_models import *
import matplotlib.pyplot as plt


def malthus_rk4():
    x0, r, t1, h = 10.0, 0.5, 10.0, 0.05
    t, x_rk4 = rk4(malthus_rhs(r), t1, x0, h)
    x_exact   = malthus_analytic(x0, r, t)   # solution fermée pour comparer:contentReference[oaicite:3]{index=3}
    
    plt.plot(t, x_exact, label="Analytique")
    plt.plot(t, x_rk4,  "--", label="RK4")
    plt.legend(); plt.xlabel("t"); plt.ylabel("N(t)"); plt.grid(); plt.show()
    
malthus_rk4()
    
def verhulst_rk4():
    x0, r, K, t1, h = 10.0, 0.5, 200.0, 20.0, 0.05
    t, x_rk4 = rk4(logistic_rhs(r, K), t1, x0, h)
    
    plt.plot(t, x_rk4)
    plt.axhline(K, color="gray", linestyle=":", label="Capacité K")
    plt.legend(); plt.xlabel("t"); plt.ylabel("N(t)"); plt.grid(); plt.show()
    
verhulst_rk4()

def lotka_volterra_rk4():
    x0, y0 = 10.0, 5.0
    a, b, c, d = 1.0, 0.1, 1.5, 0.075
    t1, h = 60.0, 0.01
    
    f = lotka_volterra_rhs(a,b,c,d)
    t, XY = rk4(f, t1, [x0, y0], h)
    x, y = XY[:,0], XY[:,1]
    
    plt.plot(t, x, label="Proies x(t)")
    plt.plot(t, y, label="Prédateurs y(t)")
    plt.legend(); plt.xlabel("t"); plt.grid(); plt.show()
    
lotka_volterra_rk4()