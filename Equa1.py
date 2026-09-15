import os
import matplotlib.pyplot as plt

# 1. Création du dossier de sortie s'il n'existe pas
os.makedirs("out", exist_ok=True)

# 2. Paramètres du système
k = 0.5
A0 = 2.0
B0 = 0.0
N = 100
dt = 0.1

# 3. Initialisation des listes pour l'historique
t_val = [0.0]
A_val = [A0]
B_val = [B0]

# 4. Résolution de l'équation différentielle (Euler explicite)
for step in range(N):
    # Récupération de la valeur à l'instant k
    A_k = A_val[-1]
    B_k = B_val[-1]
    
    # Calcul de la valeur à l'instant k+1
    A_k_plus_1 = A_k - dt * k * A_k
    B_k_plus_1 = B_k + dt * k * A_k
    
    # Enregistrement
    t_val.append(t_val[-1] + dt)
    A_val.append(A_k_plus_1)
    B_val.append(B_k_plus_1)

# 5. Visualisation avec Matplotlib
plt.figure(figsize=(8, 5))
plt.plot(t_val, A_val, label="A(t)", linewidth=2, color="blue")
plt.plot(t_val, B_val, label="B(t)", linewidth=2, color="orange")

# Mise en forme du graphique
plt.xlabel("Temps (s)")
plt.ylabel("Concentration")
plt.title(f"Évolution de A vers B (Méthode d'Euler, k={k}, dt={dt})")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# 6. Sauvegarde sous out/ et affichage
chemin_sauvegarde = "out/simulation_cinetique.png"
plt.savefig(chemin_sauvegarde, dpi=300, bbox_inches="tight")
print(f"Graphique sauvegardé avec succès dans : {chemin_sauvegarde}")

# Affichage dans le notebook
plt.show()