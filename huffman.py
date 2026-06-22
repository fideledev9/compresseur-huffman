# fonction pour compter la fréquence d'un caractère
def compter_frequence(texte):
    frequence = {}
    for caractere in texte:
        if caractere in frequence:
            frequence[caractere] += 1
        else:
            frequence[caractere] = 1
    return frequence

# construction de l'arbre de huffman
class Noeud:
    def __init__(self, caractere, frequence):
        self.caractere = caractere
        self.frequence = frequence
        self.gauche = None
        self.droite = None

def construire_arbre(frequences):
    liste = []
    for caractere, frequence in frequences.items():
        liste.append(Noeud(caractere, frequence))
    for noeud in liste:
        print(noeud.caractere, noeud.frequence)
    while len(liste) > 1:
        liste.sort(key=lambda n: n.frequence)
        gauche = liste.pop(0)
        droite = liste.pop(0)
        parent = Noeud(None, gauche.frequence + droite.frequence)
        parent.gauche = gauche
        parent.droite = droite
        liste.append(parent)

    return liste[0]

# ZONE DE TEST
frequences = compter_frequence("abracadabra")
racine = construire_arbre(frequences)
print(racine.frequence)