class action:
    def __init__(self,
                 numero=0,
                 nom="",
                 montant=0,
                 benefice=0):
        self.numero = numero
        self.nom = nom
        self.montant = self.transformation_nombre(montant)
        self.benefice = self.calcul_benefice(benefice)

    def calcul_benefice(self, benefice):
        self.benefice = self.transformation_nombre(benefice)

        self.benefice = (self.benefice/100)*self.montant
        return self.benefice
    
    def transformation_nombre(self, nombre):
        if isinstance(nombre, str):
            nombre.replace(".", ",")
            nombre_transforme = float(nombre)
            return nombre_transforme
        else:
            return nombre



class possibilite:
    def __init__(self,
                 montant=0,
                 liste_action=[],
                 benefice=0):
        self.montant = montant
        self.liste_action = liste_action
        self.benefice = benefice

    def impression_liste_action(self):
        for action in self.liste_action:
            print(action.nom)
