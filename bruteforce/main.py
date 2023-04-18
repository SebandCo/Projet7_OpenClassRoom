from objet_action import action
from objet_action import possibilite

from test import remise_a_zero

# Définition des différentes actions
action1 = action(1,"Action-1",20,5,False,0)
action2 = action(2,"Action-2",30,10,False,0)
action3 = action(3,"Action-3",50,15,False,0)
action4 = action(4,"Action-4",70,20,False,0)
action5 = action(5,"Action-5",60,17,False,0)
action6 = action(6,"Action-6",80,25,False,0)
action7 = action(7,"Action-7",22,7,False,0)
action8 = action(8,"Action-8",26,11,False,0)
action9 = action(9,"Action-9",48,13,False,0)

# Définition des paramètres de base
liste_action = [action1, action2, action3, action4, action5, action6, action7, action8, action9]
action_max = len(liste_action)-1
montant_maximum = 200
montant_actuel = 0
numero_possibilite = 1
simulation = {}
# Simulation 0
simulation[0] =[0]
# Initialisation de la première possibilité
simulation[numero_possibilite] = []


def rajout_action(liste_action,
                  montant_maximum,
                  montant_actuel,
                  numero_possibilite,
                  simulation,
                  rang_actuel):
    for action in liste_action:
        # On regarde si l'action est déjà utilisé
        if action.utilisee == False:
            montant_intermediaire = montant_actuel+ action.montant
            # Si le montant est inférieur ou égale au montant maximum
            if montant_intermediaire <= montant_maximum:
                # On incrémente le nouveau montant_actuel
                montant_actuel = montant_intermediaire
                # On rajoute l'action à l'historique de la simulation
                simulation[numero_possibilite].append(action.numero)
                # On indique que l'action a été utilisée
                action.utilisee = True
                # On indique à quel rang
                action.boucle_utilisee = rang_actuel
                # On incrémente le rang
                rang_actuel += 1

        # Si nous somme sur la dernière action
        if action.numero == len(liste_action) :
            # Controle de la simulation : Si la simulation actuel, reprend la simulation précédente -1
            # alors elle n'apporte rien de mieux. On peux la supprimer
            simulation_controle = []
            simulation_controle = (simulation[numero_possibilite - 1]) [0:((len(simulation[numero_possibilite-1])-1))]
            if simulation[numero_possibilite] != simulation_controle:
                print(simulation[numero_possibilite])
                # On crée une nouvelle simulation
                numero_possibilite += 1
                simulation[numero_possibilite]=[]
                # Si la derniere action n'a pas été utilisé
                if action.utilisee == False:
                    # On relance le programme à partir du rang n-1
                    rang_choisi = rang_actuel - 1
                # Si la dernière action a été utilisé
                else:
                    # On relance le programme à partir du rang n-2
                    rang_choisi = rang_actuel - 2
            else:
                # On relance le programme à partir du rang n-2
                    rang_choisi = rang_actuel - 2
            # On reprend l'historique de la dernière simulation
            simulation[numero_possibilite] = remise_a_zero (liste_action,
                                                            simulation[numero_possibilite],
                                                            simulation[numero_possibilite-1],
                                                            rang_choisi)
            # Ensuite on relance le programme
            montant_actuel = calcul_montant(liste_action,simulation[numero_possibilite])
            rajout_action(liste_action,
                          montant_maximum,
                          montant_actuel,
                          numero_possibilite,
                          simulation,
                          rang_choisi)


def calcul_montant (liste_action, simulation):
    montant_actuel = 0
    # Récupere les actions de la simulation
    for action in simulation:
        # Rajoute le montant des actions au montant courant
        montant_actuel += liste_action[action-1].montant
    return montant_actuel


def remise_a_zero(liste_action,simulation_actuel, simulation_precedente, rang_choisi):
    simulation_actuel = simulation_precedente [0 : (rang_choisi - 1)]
    for action in liste_action:
        if action.boucle_utilisee > rang_choisi:
            action.utilisee = False
    return simulation_actuel

# Boucle de départ
for action in liste_action:
    # Tant que le montant actuel est inférieur au montant de départ, on boucle
    rajout_action(liste_action, montant_maximum, montant_actuel, numero_possibilite, simulation,1)


print("fin du programme")

