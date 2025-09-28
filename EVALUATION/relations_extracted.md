# Relations extraites — synthèse

Date : 2025-09-28
Source : sortie de l'évaluation (fichiers `logs/relations_*` et `logs/*chunked.json`)

## Checklist
- [x] Toutes les relations extraites pour chaque modèle incluses.
- [x] Indication de la présence (ou non) de passages source pour chaque modèle.
- [x] Fichier généré : `logs/relations_extracted.md`.

---

## phi:latest (n_relations = 1)
Relations :
- Entit1 | r_est_un_type_de | Entit2

Passage source :
- `logs/relations_phi_latest.B.txt` contient la même ligne (pas d'extrait textuel distinct enregistré).

---

## mistral:latest (n_relations = 13)
Relations :
- matière végétale | r_a_comme_partie | dry sift hash
- dry sift hash | r_est_un_type_de | tamisage à sec
- tamis | r_a_comme_partie | boîte équipée d'un tamis, Hash Shaker, machine pour extraction avec tambour, grinder
- matière végétale | r_se_trouve_dans | têtes, feuilles naissant des têtes, reste des plantes, etc.
- gants | r_a_comme_partie | manœuvres pour extraire du dry sift hash
- bout de bois ou d'une carte bleue | r_a_comme_caracteristique | presser la matière végétale et défaire davantage de trichomes
- haschich filtré | r_est_un_type_de | meilleure qualité de dry sift hash
- oileur ou bubbler | r_peut | consommer le haschich filtré à l'aide d'une méthode spécifique
- pollinator | r_est_un_type_de | machine pour extractions conçue pour obtenir du haschich de haute qualité sans utiliser de solvant
- hash shaker | r_a_comme_partie | méthodes d'extractions simples et efficaces pour extraire le haschich
- presse en T pour pollen | r_peut | presser l'haschich avec une pression extrêmement élevée de terpènes et puissants effets thérapeutiques ou psychoactifs
- bong oiler indus | r_peut | consommer le haschich en utilisant un système moins toxique
- Erik Collado Vidal | r_est_un_type_de | personne ayant plus de 10 années d'expérience dans l'industrie du cannabis.

Passage source :
- `logs/relations_mistral_latest.B.txt` contient les mêmes lignes (pas d'extrait distinct enregistré).

---

## llama2:latest (n_relations = 9)
Relations :
- ENTIT1 | r_est_un_type_de | ENTIT2
- ENTIT1 | r_est_un_type_de | VOITURE (r_est_un_type_de)
- ENTIT1 | r_a_comme_partie | VOITURE (r_fait_partie_de)
- ENTIT2 | r_se_trouve_dans | PARIS (r_se_trouve_dans)
- ENTIT1 | r_peut | ROUTE (r_peut)
- ENTIT1 | F_a_composition | VEHICLE (r_a_composition)
- ENTIT1 | r_se_trouve_dans | FRANCE (r_se_trouve_dans)
- ENTIT2 | r_est_un_type_de | MOTORE (r_est_un_type_de)
- ENTIT1 | r_peut | ROULE (r_peut)

Passage source :
- `logs/relations_llama2_latest.B.txt` présent mais contient plutôt des exemples/placeholder — pas d'extrait texte original distinct.

---

## gemma3:4b-it-qat (n_relations = 18)
Relations :
- Dry Sift Hash | r_est_un_type_de | extraction
- Dry Sift Hash | r_est_un_type_de | procédé
- procédé | r_a_comme_caracteristique | tamisage à sec
- tamisage à sec | r_est_un_type_de | technique
- technique | r_a_comme_caracteristique | extraction des trichomes
- trichomes | r_a_comme_caracteristique | résine des fleurs
- fleurs | r_a_comme_caracteristique | contenant des trichomes
- presse en T pour pollen | r_est_un_type_de | machine
- machine | r_peut | extraire le haschich
- Bong Oiler Indus | r_est_un_type_de | pipe
- Bong Oiler Indus | r_peut | fumer du haschich
- Bong Oiler Indus | r_peut | fumer des concentrés
- opérateur | r_peut | manipuler la matière végétale
- têtes | r_a_comme_partie | matière végétale
- feuilles | r_a_comme_partie | matière végétale
- plante | r_a_comme_partie | têtes
- plante | r_a_comme_partie | feuilles
- plante | r_a_comme_partie | reste des plantes

Passage source :
- `logs/relations_gemma3_4b-it-qat.B.txt` non trouvé séparément durant l'analyse (pas d'extrait textuel distinct enregistré).

---

## gemma3:1b (n_relations = 92)
Relations (liste complète extraite du fichier chunked) :
- r_est_un_type_de | r_a_comme_partie | Dry Sift Hash
- r_peut | Extrait_on | Dry Sift Hash
- r_peut | r_a_comme_partie | maximiser les effets
- r_a_comme_partie | r_a_comme_partie | fleurs
- r_a_comme_caracteristique | vise à | augmenter les effets
- r_a_comme_partie | r_a_comme_partie | méthodes d'extraction
- r_a_comme_caractéristique | vise à | augmenter les effets
- r_est_un_type_de | r_a_comme_partie | culture de cannabis
- r_est_un_type_de | r_a_comme_partie | sécheresse à l'aide de l'analyse de la composante (à déterminer)
- r_est_un_type_de | r_a_comme_partie | service personnalisé
- r_peut | r_a_comme_partie | livraison
- r_est_un_type_de | r_a_comme_partie | pénginobe
- r_est_un_type_de | r_a_comme_partie | vente
- r_est_un_type_de | r_a_comme_partie | livraison
- r_est_un_type_de | r_a_comme_partie | hash
- r_peut | défaire | trichomes
- r_a_comme_partie | le | dry sift
- r_est_un_type_de | le | BHO
- r_est_un_type_de | la | presse rosin
- r_est_un_type_de | le | dry sift
- r_peut | extraire | résine
- r_est_un_type_de | le | haschich
- r_peut | r_peut | matière végétale
- r_peut | r_peut | tamis
- r_peut | r_peut | Hash Shaker
- r_peut | r_peut | Machine pour extraction
- r_peut | r_peut | grinder
- r_peut | r_a_comme_partie | presser la matière végétale
- r_a_comme_partie | r_a_comme_partie | trichomes
- r_est_un_type_de | r_a_comme_partie | haschich
- r_a_comme_partielle | r_a_comme_partie | dry sift hash
- r_est_un_type_de | r_a_comme_partie | matière végétale
- r_peut | r_peut | résultat
- r_peut | r_peut | haschich
- r_a_comme_partie | matériel | haschich
- r_a_comme_partie | tamisage à sec | haschich
- r_a_comme_partie | tamisage | haschich
- r_a_comme_partie | matière végétale | tamisage
- r_a_comme_partie | appareil | haschich
- r_peut | r_peut | tamisage à sec
- r_peut | r_peut | tamisage
- r_peut | introduire | matière végétale
- r_est_un_type_de | r_a_comme_partie | machine
- r_peut | r_peut | remuer
- r_a_comme_partie | r_est_un_type_de | boîte à tamis
- r_a_comme_partie | r_est_un_type_de | hash shaker
- r_peut | r_peut | déplacer
- r_peut | r_peut | racler
- r_peut (capacité/action) | r_a_comme_partie | haschich
- r_peut (capacité/action) | r_a_comme_partie | concentration
- r_est_un_type_de | r_est_un_type_de | haschich
- r_fait_partie_de | r_a_comme_partie | presse en T
- r_fait_partie_de | r_a_comme_partie | pollen
- r_fait_partie_de | r_a_comme_partie | oiler
- r_fait_partie_de | r_a_comme_partie | bubbler
- r_fait_partie_de | r_a_comme_partie | pipes
- r_est_un_type_de | r_est_un_type_de | concentration
- r_peut (capacité/action) | utilisé_pour | haschich
- r_peut (capacité/action) | utilisé_pour | emballer
- r_peut (capacité/action) | utilisé_pour | transporter
- r_peut (capacité/action) | utilisé_pour | consommer
- r_peut (capacité/action) | utilisé_pour | extraire
- r_peut (capacité/action) | utilisé_pour | filtrer
- r_peut (capacité/action) | utilisé_pour | savourer
- r_peut (capacité/action) | utilisé_pour | profiter
- r_peut (capacité/action) | utilisé_pour |  | haschich
- r_peut (capacité/action) | utilisé_pour |  |  |
- r_est_un_type_de | r_a_comme_partie | machine pour extractions
- r_peut | action | extraire
- r_est_un_type_de | r_a_comme_partie | plante
- r_peut | action | séparer
- r_est_un_type_de | r_a_comme_partie | résine
- r_est_un_type_de | r_a_comme_partie | plantes
- r_peut | action | traiter
- r_peut | action | élaborer
- r_est_un_type_de | r_a_comme_partie | extraction
- r_peut | action | introduire
- r_est_un_type_de | r_a_comme_partie | têtes
- r_est_un_type_de | r_a_comme_partie | appareil
- r_peut | action | action giratoire
- r_peut (capacité/action) | offrira une concentration extrêmement élevée de terpènes | concentration extrêmement élevée de terpènes
- r_fait_partie_de (composition) | Presse à pollen en T | Presse à pollen en T
- r_peut (capacité/action) | r_peut | presser
- r_fait_partie_de (composition) | Roulette | Roulette
- r_est_un_type_de | terpènes | terpènes
- r_est_un_type_de | r_peut | puissants effets thérapeutiques ou psychoactifs
- r_est_un_type_de | r_peut | effets thérapeutiques ou psychoactifs
- r_fait_partie_de (composition) | r_peut | Pipe Oiler pour fumer
- r_est_un_type_de | r_se_trouve_dans | type_de
- r_est_un_type_de | r_peut | capacité
- r_est_un_type_de | r_a_comme_partie | composition
- r_peut | r_est_un_type_de | action

Passage source :
- `logs/relations_gemma3_1b.B.txt` contient majoritairement les mêmes triplets (pas d'extraits de texte originaux distincts enregistrés).

---

## deepseek-r1:7b (n_relations = 12)
Relations :
- Dry Sift Hash | r_est_un_type_de | Trichomes
- Dry Sift Hash | r_a_comme_partie | Tamisage à sec
- Dry Sift Hash | r_peut | Utiliser un hash shaker ou un grinder
- Dry Sift Hash | r_peut | Presser avec une pincée de bois ou d'une carte blanche
- Dry Sift Hash | r_a_comme_caracteristique | Terpènes, Effets psychoactifs
- Tamisage à sec | r_est_un_type_de | Trichomes
- Tamisage à sec | r_a_comme_partie | Dry Sift Hash
- Shaker | r_a_comme_partie | Dry Sift Hash
- Grinder | r_a_comme_partie | Dry Sift Hash
- Boîte à tamis | r_a_comme_partie | Dry Sift Hash
- Presser avec une pincée de bois ou d'une carte blanche | r_peut | Dry Sift Hash
- Terpènes, Effets psychoactifs | r_a_comme_caracteristique | Dry Sift Hash

Passage source :
- `logs/relations_deepseek-r1_7b.B.txt` contient les mêmes lignes (pas d'extrait distinct enregistré).

---

## Remarques et prochaines étapes proposées
- Les fichiers `A.txt`/`chunked.json` contiennent les relations. Les fichiers `B.txt` disponibles correspondent majoritairement aux mêmes annotations — aucun fichier ne contient des passages textuels originaux distincts liés clairement aux triplets (souvent les sorties du modèle sont directement les triplets).
- Si vous souhaitez que je :
  - compile un CSV/JSON avec tous les triplets, je peux le générer et le placer dans `logs/` ; ou
  - recherche dans le fichier source (`data/*` ou le texte d'origine) les passages pertinents pour chaque triplet (nécessitera une recherche par similarité), dites-le.

Fichier créé : `logs/relations_extracted.md`
