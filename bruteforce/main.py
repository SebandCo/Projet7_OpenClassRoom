from objet_action import action
from objet_action import possibilite
# Permet d'afficher une barre de de progression
from tqdm import tqdm
import csv
from itertools import combinations

# Liste avec les différentes actions
liste_action = []
# Dictionnaire provisoire pour stocker les actions
dico_provisoire = {}
# Liste avec les différentes simulations
liste_simulation = []
# Montant maximum à ne pas dépasser
montant_maximum = 500
# Action 0
action0 = action(0, "Action-0", 0, 1)
meilleur_simulation = possibilite(0.1, action0, 0.1)


# 1er étape : récupération du fichier CSV
with open('Liste_action.csv', mode='r', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv, delimiter=';')
    i = 0
    # 2eme étape : Lecture du fichier csv
    for ligne in lecteur_csv:
        # Sauf la premiere ligne (en-tête de colonne)
        if i != 0:
            # Séparation des données
            provisoire = ligne[0].split(",")
            # 3eme étape : Création de l'objet action dans un dictionnaire
            dico_provisoire["action{}".format(i)] = action(i,
                                                           provisoire[0],
                                                           float(provisoire[1]),
                                                           float(provisoire[2]))
            # 4eme étape : Mise de l'objet dans une liste
            liste_action.append(dico_provisoire["action{}".format(i)])
        i += 1
print(f"\nDébut de l'analyse des {len(liste_action)} actions\n")


# 2eme étape : Recherche du nombre de combinaison possible
i = 1
while i < len(liste_action):
    liste_simulation.extend(list(combinations(liste_action, i)))
    i += 1
print(f"Il y a {len(liste_simulation)} combinaisons d'action possible\n")


# 3eme étape : Recherche de la meilleur solution
for combinaison in tqdm(liste_simulation, desc="Analyse en cours", unit="combinaison"):
    provisoire = possibilite(0, combinaison, 0)
    # Controle pour voir si le montant maximum n'a pas été dépassé
    if provisoire.montant <= montant_maximum:
        # Comparaison par rapport à la meilleur simulation
        if meilleur_simulation.benefice < provisoire.benefice:
            meilleur_simulation = possibilite(provisoire.montant,
                                              provisoire.liste_action,
                                              provisoire.benefice)
        # Si les deux benefices sont identique, on prend le plus petit montant d'action
        elif meilleur_simulation.benefice == provisoire.benefice:
            if meilleur_simulation.montant > provisoire.montant:
                meilleur_simulation = possibilite(provisoire.montant,
                                                  provisoire.liste_action,
                                                  provisoire.benefice)


# Compte-rendu final
print(f"\nLe meilleur montage possible a été trouvé\n"
      f"Le benefice attendu est de {meilleur_simulation.benefice:.2f} euros\n"
      f"Pour un investissement de départ de {meilleur_simulation.montant} euros\n\n"
      f"Il faudra utiliser les actions :")
meilleur_simulation.impression_liste_action()

print("fin du programme")
