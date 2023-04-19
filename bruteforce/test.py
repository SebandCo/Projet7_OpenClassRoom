from objet_action import action

# Action nul pour permettre le lancement de la boucle
action0 = action(0,"Action-0",0,1,False)
# Définition des différentes actions
action1 = action(1,"Action-1",20,5,False)
action2 = action(2,"Action-2",30,10,False)
action3 = action(3,"Action-3",50,15,False)
action4 = action(4,"Action-4",70,20,False)
action5 = action(5,"Action-5",60,17,False)
action6 = action(6,"Action-6",80,25,False)
action7 = action(7,"Action-7",22,7,False)
action8 = action(8,"Action-8",26,11,False)
action9 = action(9,"Action-9",48,13,False)

# Définition des paramètres de base
liste_action = [action0,
                action1,
                action2,
                action3,
                action4,
                action5,
                action6,
                action7,
                action8,
                action9]
numero_possibilite = 1
simulation = {}

# Initialisation de la première possibilité
simulation[numero_possibilite] = []


def rajout_action(liste_action,
                  action_precedente,
                  simulation,
                  possibilite):
    for action in liste_action:
        if action.numero > action_precedente.numero:
            simulation[possibilite].append(action)
            print(simulation[possibilite])
            global numero_possibilite 
            numero_possibilite += 1
            if action.numero != len(liste_action)-1:
                simulation[numero_possibilite]=creation(simulation[possibilite])
            else:
                simulation[numero_possibilite]=[]
            rajout_action(liste_action,
                          action,
                          simulation,
                          numero_possibilite)
            return ()

# Reprise de l'historique de l'action précedente
def creation (simul_precedente):
    simulation = []
    for i in simul_precedente:
        simulation.append(i)
    return simulation


# Boucle de départ
for action_actuelle in liste_action:
    rajout_action(liste_action,
                  action_actuelle,
                  simulation,
                  numero_possibilite)



print("fin du programme")