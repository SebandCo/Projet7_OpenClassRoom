class action:
    def __init__(self,
                 numero=0,
                 nom="",
                 montant=0,
                 benefice=0):
        self.numero = numero
        self.nom = nom
        self.montant = montant
        self.benefice = self.calcul_benefice(benefice)

    def calcul_benefice(self, benefice):
        self.benefice = (benefice/100)*self.montant
        return self.benefice


class possibilite:
    def __init__(self,
                 montant=0,
                 liste_action=[],
                 benefice=0):
        self.liste_action = liste_action
        self.montant = self.calcul_montant(montant)
        self.benefice = self.calcul_benefice(benefice)

    def calcul_montant(self, montant):
        # Si le montant est de 0, alors on le calcul 
        if montant == 0:
            for action in self.liste_action:
                montant += action.montant
        return (montant)

    def calcul_benefice(self, benefice):
        # Si le benefice est de 0, alors on le calcul 
        if benefice == 0:
            for action in self.liste_action:
                benefice += action.benefice
        return (benefice)
    
    def impression_liste_action(self):
        for action in self.liste_action:
            print(action.nom)
