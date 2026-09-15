import numpy as np
import matplotlib.pyplot as plt

# 1. Paramètres physiques
R = 25.0   # Terme de rappel (k/m)
A = 0.1   # Terme d'amortissement / frottement
x0 = 1.0  # Position initiale
y0 = 0.0  # Vitesse initiale

# 2. Paramètres de simulation (n et dt)
dt = 0.05           # Pas de temps
T_max = 50          # Temps total de la simulation
n = int(T_max / dt) # Nombre total d'itérations

# 3. Initialisation des tableaux de stockage
x = np.zeros(n)
y = np.zeros(n)
t = np.zeros(n)

# 4. Conditions initiales (à t=0, indice 0)
x[0] = x0
y[0] = y0
t[0] = 0.0

# 5. Boucle d'intégration (Méthode de Runge-Kutta 2 - Point milieu)
for i in range(n - 1):
    # a. Pentes au début de l'intervalle (k1)
    k1_x = y[i]
    k1_y = -R * x[i] - A * y[i]
    
    # b. Estimation de l'état au point milieu (t + dt/2)
    x_mid = x[i] + 0.5 * dt * k1_x
    y_mid = y[i] + 0.5 * dt * k1_y
    
    # c. Pentes au point milieu (k2)
    k2_x = y_mid
    k2_y = -R * x_mid - A * y_mid
    
    # d. Mise à jour de x et y pour l'instant suivant (i + 1)
    x[i+1] = x[i] + dt * k2_x
    y[i+1] = y[i] + dt * k2_y
    
    # e. Avancement du temps
    t[i+1] = t[i] + dt

# 6. Affichage avec Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Position (x)', color='blue')
plt.plot(t, y, label='Vitesse (y)', color='orange', linestyle='--')

plt.title("Oscillateur harmonique amorti (Méthode RK2)")
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# 6.5 Sauvegarde et affichage
chemin_sauvegarde = "out/simulation_ressort_rk2.png"
plt.savefig(chemin_sauvegarde, dpi=300, bbox_inches="tight")
print(f"Graphique sauvegardé avec succès dans : {chemin_sauvegarde}")

plt.show()
