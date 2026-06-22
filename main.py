from huffman import (compter_frequence, construire_arbre,
                     generer_codes, compresser,
                     sauvegarder, charger, decompresser, mesurer)

texte = open("exemples/texte_exemple.txt", "r", encoding="utf-8").read()
frequences = compter_frequence(texte)
racine = construire_arbre(frequences)
codes = {}
generer_codes(racine, "", codes)
octets, padding = compresser(texte, codes)
sauvegarder(codes, padding, octets, "exemples/compresse.huff")
codes, padding, octets = charger("exemples/compresse.huff")
texte_retrouve = decompresser(codes, padding, octets)
mesurer("exemples/texte_exemple.txt", "exemples/compresse.huff", texte, texte_retrouve)