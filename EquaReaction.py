import numpy as np
import matplotlib.pyplot as plt

# 1. Paramètres cinétiques (valeurs arbitraires)
k1 = 0.5
k2 = 2.5
k3 = 0.5
E0 = 1.0
S0 = 2.0

# 2. Paramètres de simulation (n et dt)
dt = 0.1            # Pas de temps 
T_max = 50         # Temps total de la simulation
n = int(T_max / dt) # Nombre total d'itérations

# 3. Initialisation des tableaux de stockage
E = np.zeros(n)
S = np.zeros(n)
ES = np.zeros(n)
P = np.zeros(n)
t = np.zeros(n)

# 4. Conditions initiales (à l'instant t=0, indice 0)
E[0] = E0
S[0] = S0
ES[0] = E0 - E[0]
P[0] = S0 - ES[0] - S[0]
t[0] = 0

# 5. Boucle d'intégration (Méthode d'Euler)
for i in range(n - 1):
    # a. Calcul des dérivées à l'instant i
    dEdt = -k1 * E[i] * S[i] + k2 * (E0 - E[i]) + k3 * (E0 - E[i])
    dSdt = -k1 * E[i] * S[i] + k2 * (E0 - E[i])
    
    # b. Mise à jour de E et S pour l'instant suivant (i + 1)
    # Formule d'Euler : Valeur_suivante = Valeur_actuelle + (Dérivée * dt)
    E[i+1] = E[i] + dEdt * dt
    S[i+1] = S[i] + dSdt * dt
    
    # c. Calcul des autres variables
    ES[i+1] = E0 - E[i+1]
    P[i+1] = S0 - ES[i+1] - S[i+1]
    
    # d. Avancement du temps
    t[i+1] = t[i] + dt

# 6. Affichage avec Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(t, E, label='Enzyme libre (E)', color='blue')
plt.plot(t, S, label='Substrat (S)', color='orange')
plt.plot(t, ES, label='Complexe (ES)', color='red')
plt.plot(t, P, label='Produit (P)', color='green')

plt.title("Cinétique enzymatique (Résolution par la méthode d'Euler)")
plt.xlabel('Temps')
plt.ylabel('Concentration')
plt.legend()
plt.grid(True)

# 6.5 Sauvegarde sous out/ et affichage
chemin_sauvegarde = "out/simulation_catalyse.png"
plt.savefig(chemin_sauvegarde, dpi=300, bbox_inches="tight")
print(f"Graphique sauvegardé avec succès dans : {chemin_sauvegarde}")

plt.show()
