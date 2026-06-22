# compresseur-huffman

Implémentation de l'algorithme de compression de Huffman en Python pur





\# Compresseur Huffman



Implémentation de l'algorithme de compression de Huffman en Python pur.



\## Description



Ce projet compresse et décompresse des fichiers texte en utilisant l'algorithme

de Huffman. Les caractères fréquents reçoivent des codes courts, les caractères

rares des codes plus longs, ce qui réduit la taille du fichier sans perte de données.



\## Fonctionnalités



\- Analyse des fréquences des caractères

\- Construction de l'arbre de Huffman

\- Génération des codes binaires

\- Compression en vrais octets binaires

\- Sauvegarde et chargement du fichier compressé

\- Décompression et vérification de l'intégrité

\- Mesure du taux de compression



\## Utilisation



```bash

python main.py

```



\## Résultats



| Fichier | Taille originale | Taille compressée | Réduction |

|---------|-----------------|-------------------|-----------|

| texte\_exemple.txt | XX octets | XX octets | XX% |



\## Technologies



\- Python 3

\- Modules standard : pickle, os

