from objet_action import actions
from objet_action import possibilite
import csv

# Dictionnaire provisoire pour stocker les actions
dico_provisoire = {}
# Dictionnaire ne contenant que le benefice par action(clé)
dico_tri_benefice = {}
# Permet de stocker les valeurs une fois triées
liste_tri = []
# Montant maximum à ne pas dépasser
montant_maximum = 500
# Valeur en dessous duquel une action est considérée comme non valide
action_minimum = 0
montant_provisoire = 0
solution = []

# Définition des différentes actions
# 1er étape : récupération du fichier CSV
with open('dataset1.csv', mode='r', encoding='utf-8') as fichier_csv:
#with open('dataset1.csv', mode='r', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv, delimiter=';')
    i = 0
    # 2eme étape : Lecture du fichier csv
    for ligne in lecteur_csv:
        # Sauf la premiere ligne (en-tête de colonne)
        if i != 0:
            # Séparation des données
            provisoire = ligne[0].split(",")
            # 3eme étape : Création de l'objet action dans un dictionnaire
            # En supprimant les actions gratuites (montant d'achat > action_minimum)
            if float(provisoire[1]) > action_minimum:
                dico_provisoire["action{}".format(i)] = actions(i,
                                                                provisoire[0],
                                                                float(provisoire[1]),
                                                                float(provisoire[2]))
                dico_tri_benefice["action{}".format(i)] = dico_provisoire["action{}".format(i)].pourcentage
        i += 1

# Début du programme
print(f"\nDébut de l'analyse des {len(dico_tri_benefice)} actions\n")


# 2eme étape : Tri des actions par ordre décroissant de bénéfice
liste_tri = sorted(dico_tri_benefice.items(), key=lambda action:action[1],reverse=True)


# 3eme étape : Recherche des meilleurs action vis à vis du montant globale
for action in liste_tri:
    if (montant_provisoire + dico_provisoire[action[0]].montant) <= montant_maximum:
        montant_provisoire += dico_provisoire[action[0]].montant
        print(montant_provisoire)
        solution.append(dico_provisoire[action[0]])

# 4eme étape : mise en forme de la réponse
resultat = possibilite(0,solution,0)

# Compte-rendu final
print(f"\nLe meilleur montage possible a été trouvé\n"
      f"Le benefice attendu est de {resultat.benefice} euros\n"
      f"Pour un investissement de départ de {resultat.montant} euros\n\n"
      f"Il faudra utiliser les actions :")
resultat.impression_liste_action()

print("fin du programme")