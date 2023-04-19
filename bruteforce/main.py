from objet_action import action
from objet_action import possibilite

# Action nul pour permettre le lancement de la boucle
action0 = action(0,"Action-0",0,1)
# Définition des différentes actions
action1 = action(1,"Action-1",20,5)
action2 = action(2,"Action-2",30,10)
action3 = action(3,"Action-3",50,15)
action4 = action(4,"Action-4",70,20)
action5 = action(5,"Action-5",60,17)
action6 = action(6,"Action-6",80,25)
action7 = action(7,"Action-7",22,7)
action8 = action(8,"Action-8",26,11)
action9 = action(9,"Action-9",48,13)
action10 = action(10,"Action-10",34,27)
action11 = action(11,"Action-11",42,17)
action12 = action(12,"Action-12",110,9)
action13 = action(13,"Action-13",38,23)
action14 = action(14,"Action-14",14,1)
action15 = action(15,"Action-15",18,3)
action16 = action(16,"Action-16",8,8)
action17 = action(17,"Action-17",4,12)
action18 = action(18,"Action-18",10,14)
action19 = action(19,"Action-19",24,21)
action20 = action(20,"Action-20",114,18)

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
                action9,
                action10,
                action11,
                action12,
                action13,
                action14,
                action15,
                action16,
                action17,
                action18,
                action19,
                action20]
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
    for action in liste_action:
        if action.numero > action_precedente.numero:
            simulation[possibilite].append(action)
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

# Début du programme
print (f"Début de l'analyse des {len(liste_action)-1} actions\n")

# Boucle de départ
for action_actuelle in liste_action:
    rajout_action(liste_action,
                  action_actuelle,
                  simulation,
                  numero_possibilite)

# Premier compte-rendu
print (f"Il y a {numero_possibilite-1} combinaisons d'action possible\n")

for possibilites in simulation:
    # Rajout du montant de l'action au montant provisoire
    for action_possible in simulation[possibilites]:
        montant_provisoire += action_possible.montant

    # Controle si le montant_provisoire est inférieur au montant possible
    if montant_provisoire <= montant_maximum:
        simulation_valide[numero_possible] = possibilite (montant_provisoire,
                                                          simulation[possibilites],
                                                          0)
        for action_valide in simulation_valide[numero_possible].liste_action:
            simulation_valide[numero_possible].benefice += action_valide.benefice

        numero_possible += 1
    
    # Remise à zéro du montant_provisoire avant la prochaine boucle
    montant_provisoire = 0

# Deuxième compte-rendu
print (f"Sur les {numero_possibilite - 1} combinaison possible\n"
       f"Seules {numero_possible - 1} sont conforme avec la limite de {montant_maximum} euros\n")

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
    elif  simulation_valide[action_possible].benefice > meilleur_benefice:
            meilleur_valeur = action_possible
            meilleur_benefice = simulation_valide[action_possible].benefice
            meilleur_montant_base = simulation_valide[action_possible].montant

# Compte-rendu final
print (f"Le meilleur montage possible est la numéro {meilleur_valeur}\n"
       f"Le benefice attendu est de {simulation_valide[meilleur_valeur].benefice} euros\n"
       f"Pour un investissement de départ de {simulation_valide[meilleur_valeur].montant} euros\n"
       f"Il faudra utiliser les actions :")
simulation_valide[meilleur_valeur].impression_liste_action()


print("fin du programme")