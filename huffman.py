import pickle
import os

# Etape 1 : compter les fréquences des caractères
def compter_frequence(texte):
    frequence = {}
    for caractere in texte:
        if caractere in frequence:
            frequence[caractere] += 1
        else:
            frequence[caractere] = 1
    return frequence


# Etape 2 : construction de l'arbre de Huffman
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
    while len(liste) > 1:
        liste.sort(key=lambda n: n.frequence)
        gauche = liste.pop(0)
        droite = liste.pop(0)
        parent = Noeud(None, gauche.frequence + droite.frequence)
        parent.gauche = gauche
        parent.droite = droite
        liste.append(parent)
    return liste[0]


# Etape 3 : générer les codes binaires
def generer_codes(noeud, code_actuel, codes):
    if noeud is None:
        return
    if noeud.caractere is not None:
        codes[noeud.caractere] = code_actuel
    else:
        generer_codes(noeud.gauche, code_actuel + "0", codes)
        generer_codes(noeud.droite, code_actuel + "1", codes)


# Etape 4 : compresser le texte
def compresser(texte, codes):
    chaine_bits = ""
    for caractere in texte:
        chaine_bits += str(codes[caractere])
    padding = 8 - len(chaine_bits) % 8
    chaine_bits += "0" * padding
    octets = bytearray()
    for i in range(0, len(chaine_bits), 8):
        octet = chaine_bits[i:i + 8]
        octets.append(int(octet, 2))
    return octets, padding


# Etape 5 : sauvegarder le fichier compressé
def sauvegarder(codes, padding, octets, nom_fichier):
    with open(nom_fichier, "wb") as f:
        pickle.dump(codes, f)
        pickle.dump(padding, f)
        pickle.dump(octets, f)


# Etape 5 : charger le fichier compressé
def charger(nom_fichier):
    with open(nom_fichier, "rb") as f:
        codes = pickle.load(f)
        padding = pickle.load(f)
        octets = pickle.load(f)
    return codes, padding, octets


# Etape 6 : décompresser
def decompresser(codes, padding, octets):
    chaine_bits = ""
    for octet in octets:
        chaine_bits += bin(octet)[2:].zfill(8)
    chaine_bits = chaine_bits[:-padding]
    codes_inverses = {v: k for k, v in codes.items()}
    texte = ""
    code_actuel = ""
    for bit in chaine_bits:
        code_actuel += bit
        if code_actuel in codes_inverses:
            texte += codes_inverses[code_actuel]
            code_actuel = ""
    return texte


# Etape 7 : vérifier et mesurer
def mesurer(nom_original, nom_compresse, texte_original, texte_retrouve):
    if texte_original == texte_retrouve:
        print("✓ Décompression réussie : le texte est identique à l'original")
    else:
        print("✗ Erreur : le texte décompressé est différent de l'original")
    taille_avant = os.path.getsize(nom_original)
    taille_apres = os.path.getsize(nom_compresse)
    pourcentage = round((1 - taille_apres / taille_avant) * 100, 2)
    print(f"Taille originale  : {taille_avant} octets")
    print(f"Taille compressée : {taille_apres} octets")
    print(f"Réduction         : {pourcentage}%")