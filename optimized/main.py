from objet_action import action
from objet_action import possibilite

import csv

# Action nul pour permettre le lancement de la boucle
action0 = action(0, "Action-0", 0, 1)
liste_action = [action0]

# Dictionnaire provisoire pour stocker les actions
dico_provisoire = {}

# Définition des différentes actions
# 1er étape : récupération du fichier CSV
with open('dataset1.csv', mode='r', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv, delimiter=';')
    i = 0
    # 2eme étape : Lecture du fichier csv
    for ligne in lecteur_csv:
        # Sauf la premiere ligne
        if i != 0:
            # Séparation des données
            provisoire = ligne[0].split(",")
            # 3eme étape : Création de l'objet action dans un dictionnaire
            dico_provisoire["action{}".format(i)] = action(i,
                                                           provisoire[0],
                                                           provisoire[1],
                                                           provisoire[2])
            # 4eme étape : Récupération des benefices
            liste_action.append(dico_provisoire["action{}".format(i)])
        i += 1



# Définition des paramètres de base
numero_possibilite = 1
simulation = {}


# Définition des paramètres montant
montant_provisoire = 0
montant_maximum = 500

# Définition des paramètre pour les simulations valides
numero_possible = 1
simulation_valide = {}

# Initialisation de la première possibilité
simulation[numero_possibilite] = []


def rajout_action(liste_action,
                  action_precedente,
                  simulation,
                  possibilite):
    for numero_action in liste_action:
        if numero_action.numero > action_precedente.numero:
            simulation[possibilite].append(numero_action)
            global numero_possibilite 
            numero_possibilite += 1
            if numero_action.numero != len(liste_action)-1:
                simulation[numero_possibilite] = creation(simulation[possibilite])
            else:
                simulation[numero_possibilite] = []
            rajout_action(liste_action,
                          numero_action,
                          simulation,
                          numero_possibilite)
            return ()


# Reprise de l'historique de l'action précedente
def creation(simul_precedente):
    simulation = []
    for i in simul_precedente:
        simulation.append(i)
    return simulation


# Début du programme
print(f"Début de l'analyse des {len(liste_action)-1} actions\n")

# Boucle de départ
for action_actuelle in liste_action:
    rajout_action(liste_action,
                  action_actuelle,
                  simulation,
                  numero_possibilite)

# Premier compte-rendu
print(f"Il y a {numero_possibilite-1} combinaisons d'action possible\n")

for possibilites in simulation:
    # Rajout du montant de l'action au montant provisoire
    for action_possible in simulation[possibilites]:
        montant_provisoire += action_possible.montant

    # Controle si le montant_provisoire est inférieur au montant possible
    if montant_provisoire <= montant_maximum:
        simulation_valide[numero_possible] = possibilite(montant_provisoire,
                                                         simulation[possibilites],
                                                         0)
        for action_valide in simulation_valide[numero_possible].liste_action:
            simulation_valide[numero_possible].benefice += action_valide.benefice

        numero_possible += 1

    # Remise à zéro du montant_provisoire avant la prochaine boucle
    montant_provisoire = 0

# Deuxième compte-rendu
print(f"Sur les {numero_possibilite - 1} combinaison possible\n"
      f"Seules {numero_possible - 1} sont conforme avec la limite de "
      f"{montant_maximum} euros\n")

# Analyse du benefice attendu
meilleur_valeur = 0
meilleur_benefice = 0
meilleur_montant_base = 0

# Recherche du meilleur bénéfice
for action_possible in simulation_valide:
    # Si deux bénéfices sont équivalent, recherche le plus petit investissement
    if simulation_valide[action_possible].benefice == meilleur_benefice:
        if simulation_valide[action_possible].montant < meilleur_montant_base:
            meilleur_valeur = action_possible
            meilleur_benefice = simulation_valide[action_possible].benefice
            meilleur_montant_base = simulation_valide[action_possible].montant
    elif simulation_valide[action_possible].benefice > meilleur_benefice:
        meilleur_valeur = action_possible
        meilleur_benefice = simulation_valide[action_possible].benefice
        meilleur_montant_base = simulation_valide[action_possible].montant

# Compte-rendu final
print(f"Le meilleur montage possible est la numéro {meilleur_valeur}\n"
      f"Le benefice attendu est de {simulation_valide[meilleur_valeur].benefice} euros\n"
      f"Pour un investissement de départ de {simulation_valide[meilleur_valeur].montant} euros\n"
      f"Il faudra utiliser les actions :")
simulation_valide[meilleur_valeur].impression_liste_action()

print("fin du programme")