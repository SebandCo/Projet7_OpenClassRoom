class action:
    def __init__(self,
                 nom = "",
                 montant = 0,
                 benefice = 0,
                 utilisee = False,
                 boucle_utilisee = 0):
        self.nom = nom
        self.montant = montant
        self.benefice = self.calcul_benefice(benefice)
        self.utilisee = utilisee
        self.boucle_utilisee = boucle_utilisee
    
    def calcul_benefice(self,benefice):
        self.benefice = self.montant + (benefice/100)*self.montant
        return self.benefice

class possibilite:
    def __init__(self,
                 montant = 0,
                 liste_action = [],
                 benefice = 0,
                 numero_boucle = 1,
                 fin_de_boucle = False):
        self.montant = montant
        self.liste_action = liste_action
        self.benefice = benefice
        self.numero_boucle = numero_boucle
        self.fin_de_boucle = fin_de_boucle
    
    def reprise (self, simulation, jalon):
        for action in simulation.liste_action[0:(jalon-3)]:
            self.montant = self.montant + action.montant
            self.liste_action.append (action)
            self.benefice = self.benefice + action.benefice
            self.numero_boucle = self.numero_boucle+1
        self.fin_de_boucle = False
