import random

class Personne:
    def __init__(self, nom, sexe, age, couleur):
        self.nom = nom
        self.sexe = sexe
        self.age = age
        self.couleur = couleur

    def majeur(self):
        return self.age > 18

class Femme(Personne):
    def __init__(self, nom, age, couleur, dominance):
        super().__init__(nom, "F", age, couleur)
        self.dominance = dominance

    def enfant(self, homme, age_enfant=0):
        if homme.sexe == "M" and self.majeur() and homme.majeur():
            dominance_enfant = (self.dominance + homme.dominance) / 2
            sexe_enfant = random.choice(["fille", "garçon"])
            return f"{sexe_enfant} ({dominance_enfant})"
        else:
            return "Impossible d'avoir un enfant."

class Homme(Personne):
    def __init__(self, nom, age, couleur, dominance):
        super().__init__(nom, "M", age, couleur)
        self.dominance = dominance

# Exemple d'utilisation
homme1 = Homme("John", 25, "brun", 0.7)
femme1 = Femme("Alice", 22, "blond", 0.6)

enfant_resultat = femme1.enfant(homme1)
print(enfant_resultat)
