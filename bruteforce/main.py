from objet_action import action
from objet_action import possibilite
from test import rajout_action
from test import remise_a_zero

# Définition des différentes actions
action1 = action("Action-1",20,5,False,0)
action2 = action("Action-2",30,10,False,0)
action3 = action("Action-3",50,15,False,0)
action4 = action("Action-4",70,20,False,0)
action5 = action("Action-5",60,17,False,0)
action6 = action("Action-6",80,25,False,0)
action7 = action("Action-7",22,7,False,0)
action8 = action("Action-8",26,11,False,0)
action9 = action("Action-9",48,13,False,0)

# Définition des paramètres de base
liste_action = [action1, action2, action3, action4, action5, action6, action7, action8, action9]
action_max = len(liste_action)-1
montant_depart = 200
montant_actuel = 0
numero_possibilite = 1
simulation = {}
# Initialisation de la première possibilité
simulation[numero_possibilite] = possibilite ()

# Boucle de départ
for action in liste_action:
    # Tant que le montant actuel est inférieur au montant de départ, on boucle
    # Balaie toutes les actions
    for action_actuel in liste_action:
        # Si le montant est dépassé, on enleve la dernière recherche
        if simulation[numero_possibilite].fin_de_boucle == True :
            action_a_supprimer = simulation[numero_possibilite].liste_action[-1]
            numero_possibilite = numero_possibilite + 1
            simulation[numero_possibilite] = possibilite(0,[],0,1,False)
            simulation[numero_possibilite].reprise(simulation[numero_possibilite-1],simulation[numero_possibilite-1].numero_boucle)
            remise_a_zero(liste_action,simulation[numero_possibilite-1].numero_boucle)
        # Tant que le montant actuel est inférieur au montant de départ, on boucle
        elif simulation[numero_possibilite].montant < montant_depart and liste_action[action_max].utilisee != True:
            rajout_action(action_max, action_actuel,simulation[numero_possibilite],montant_depart)
            print(len(simulation[numero_possibilite].liste_action))
        # si le montant n'est pas atteint, on recommence à zéro
        else:
            remise_a_zero(liste_action,2)
            simulation[numero_possibilite] = possibilite(0,[],0,1)
            break


print("fin du programme")
