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

code_actuel = ""
codes = {}

def generer_codes(noeud, code_actuel, codes):
    if noeud is None:
        # on s'arrête
        return
    if noeud.caractere is not None:
        # c'est une feuille, on sauvegarde le code
        codes[noeud.caractere] = code_actuel
    else:
        # ce n'est pas une feuille, on continue à gauche et à droite
        generer_codes(noeud.gauche, code_actuel + "0", codes)
        generer_codes(noeud.droite, code_actuel + "1", codes)

def compresser(texte, codes):
    chaine_bits = ""
    for caractere in texte:
        chaine_bits += str(codes[caractere])
    #Ajoutez le padding pour avoir un multiple de 8
    padding = 8 - len(chaine_bits) % 8
    chaine_bits += "0" * padding

    #Conversion en octets
    octets = bytearray()
    for i in range(0, len(chaine_bits), 8):
        octet = chaine_bits[i:i + 8] 
        octets.append(int(octet, 2))
    return octets, padding


# ZONE DE TEST
texte = "abracadabra"
frequences = compter_frequence(texte)
racine = construire_arbre(frequences)
codes = {}
generer_codes(racine, "", codes)
octets, padding = compresser(texte, codes)
print(octets)
print("padding:", padding)