import numpy as np
import matplotlib.pyplot as plt

# 1. Paramètres physiques
R = 25   # Terme de rappel (k/m)
A = 0.1   # Terme d'amortissement / frottement
x0 = 1.0  # Position initiale
y0 = 0.0  # Vitesse initiale

# 2. Paramètres de simulation (n et dt)
dt = 0.0001           # Pas de temps
T_max = 20          # Temps total de la simulation
n = int(T_max / dt) # Nombre total d'itérations

# 3. Initialisation des tableaux de stockage
x = np.zeros(n)
y = np.zeros(n)
t = np.zeros(n)

# 4. Conditions initiales (à t=0, indice 0)
x[0] = x0
y[0] = y0
t[0] = 0.0

# 5. Boucle d'intégration (Méthode d'Euler)
for i in range(n - 1):
    # a. Calcul des dérivées à l'instant i
    dxdt = y[i]
    dydt = -R * x[i] - A * y[i]
    
    # b. Mise à jour de x et y pour l'instant suivant (i + 1)
    x[i+1] = x[i] + dxdt * dt
    y[i+1] = y[i] + dydt * dt
    
    # c. Avancement du temps
    t[i+1] = t[i] + dt

# 6. Affichage avec Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Position (x)', color='blue')
plt.plot(t, y, label='Vitesse (y)', color='orange', linestyle='--')

plt.title("Oscillateur harmonique amorti (Méthode d'Euler)")
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# 6.5 Sauvegarde et affichage
chemin_sauvegarde = "out/simulation_ressort.png"
plt.savefig(chemin_sauvegarde, dpi=300, bbox_inches="tight")
print(f"Graphique sauvegardé avec succès dans : {chemin_sauvegarde}")

plt.show()
