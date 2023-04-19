class action:
    def __init__(self,
                 numero = 0,
                 nom = "",
                 montant = 0,
                 benefice = 0):
        self.numero = numero
        self.nom = nom
        self.montant = montant
        self.benefice = self.calcul_benefice(benefice)
    
    def calcul_benefice(self,benefice):
        self.benefice = (benefice/100)*self.montant
        return self.benefice

class possibilite:
    def __init__(self,
                 montant = 0,
                 liste_action = [],
                 benefice = 0):
        self.montant = montant
        self.liste_action = liste_action
        self.benefice = benefice
