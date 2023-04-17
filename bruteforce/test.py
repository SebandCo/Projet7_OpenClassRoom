# Rajout de l'action à la simulation
def rajout_action(action_max, action, simulation, montant_depart):
    if action.utilisee == False:
        montant_intermediaire = simulation.montant + action.montant
        if montant_intermediaire <= montant_depart:
            # Modifie les paramètres de l'action (numéro de boucle et utilisation)
            action.boucle_utilisee = simulation.numero_boucle
            action.utilisee = True
            # Modifie les paramètres de la simulation en cours
            simulation.montant = montant_intermediaire
            simulation.liste_action.append(action)
            simulation.benefice = simulation.benefice + action.benefice
            simulation.numero_boucle = simulation.numero_boucle + 1
            # Si le montant de départ est atteint, on arrete la boucle
            if montant_intermediaire == montant_depart:
                simulation.fin_de_boucle = True
        else:
            simulation.fin_de_boucle = True

    # Si on est sur la dernière action, on arrete la boucle
    if int(action.nom[-1]) == action_max:
            simulation.fin_de_boucle = True


def remise_a_zero(liste_action, numero_boucle):
    for action in liste_action:
        if action.boucle_utilisee > numero_boucle:
            action.utilisee = False