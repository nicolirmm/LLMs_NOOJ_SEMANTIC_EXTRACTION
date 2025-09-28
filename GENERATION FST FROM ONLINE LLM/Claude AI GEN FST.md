# Extraction de relations sémantiques - Tamisage à sec

## Dictionnaires thématiques

### Dictionnaire Cannabis
```
tamisage,N+FLX=Modèle+Sémantique
hachisch,N+FLX=Modèle+Sémantique  
trichomes,N+FLX=Modèle+Sémantique
cannabis,N+FLX=Modèle+Sémantique
rosin,N+FLX=Modèle+Sémantique
bubble_hash,N+FLX=Modèle+Sémantique
kief,N+FLX=Modèle+Sémantique
fleurs,N+FLX=Modèle+Sémantique
```

### Dictionnaire Équipement
```
écrans,N+FLX=Modèle+Sémantique
filtres,N+FLX=Modèle+Sémantique
sacs,N+FLX=Modèle+Sémantique
cadres,N+FLX=Modèle+Sémantique
papier_parchemin,N+FLX=Modèle+Sémantique
rouleau_peinture,N+FLX=Modèle+Sémantique
```

### Dictionnaire Mesures
```
LPI,N+FLX=Modèle+Sémantique
microns,N+FLX=Modèle+Sémantique
température,N+FLX=Modèle+Sémantique
```

## Relations extraites

1. **hachisch_à_tamiser_à_sec | r_est_un_type_de | concentré_cannabis ;**
2. **tamisage_à_sec | r_est_un_type_de | processus_mécanique ;**
3. **trichomes | r_a_comme_partie/element | têtes ;**
4. **têtes_trichomes | r_se_trouve_dans | tiges ;**
5. **écrans_tamisage | r_a_comme_caracteristique | pores ;**
6. **bubble_hash | r_peut | atteindre_fusion_complète ;**
7. **dry_sift | r_peut | produire_rosin_qualité ;**
8. **paint_roller_tech | r_est_un_type_de | technique_nettoyage ;**

## Automates NooJ (Format Main 15)

### Relation 1 : hachisch_à_tamiser_à_sec | r_est_un_type_de | concentré_cannabis

#### Automate 1.1 : hachisch_à_tamiser_à_sec avant concentré_cannabis
```
<relation>
hachisch_à_tamiser_à_sec | r_est_un_type_de | concentré_cannabis ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"hachisch_à_tamiser_à_sec" 122 37 1 14
"concentré_cannabis" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$hachisch_à_tamiser_à_sec |r_est_un_type_de| concentré_cannabis>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

#### Automate 1.2 : concentré_cannabis avant hachisch_à_tamiser_à_sec
```
<relation>
concentré_cannabis | r_est_un_type_de | hachisch_à_tamiser_à_sec ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"concentré_cannabis" 122 37 1 14
"hachisch_à_tamiser_à_sec" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$hachisch_à_tamiser_à_sec |r_est_un_type_de| concentré_cannabis>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

### Relation 2 : tamisage_à_sec | r_est_un_type_de | processus_mécanique

#### Automate 2.1 : tamisage_à_sec avant processus_mécanique
```
<relation>
tamisage_à_sec | r_est_un_type_de | processus_mécanique ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"tamisage_à_sec" 122 37 1 14
"processus_mécanique" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$tamisage_à_sec |r_est_un_type_de| processus_mécanique>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

#### Automate 2.2 : processus_mécanique avant tamisage_à_sec
```
<relation>
processus_mécanique | r_est_un_type_de | tamisage_à_sec ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"processus_mécanique" 122 37 1 14
"tamisage_à_sec" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$tamisage_à_sec |r_est_un_type_de| processus_mécanique>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

### Relation 3 : trichomes | r_a_comme_partie/element | têtes

#### Automate 3.1 : trichomes avant têtes
```
<relation>
trichomes | r_a_comme_partie/element | têtes ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"trichomes" 122 37 1 14
"têtes" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$trichomes |r_a_comme_partie/element| têtes>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

#### Automate 3.2 : têtes avant trichomes
```
<relation>
têtes | r_a_comme_partie/element | trichomes ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"têtes" 122 37 1 14
"trichomes" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$trichomes |r_a_comme_partie/element| têtes>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

### Relation 4 : têtes_trichomes | r_se_trouve_dans | tiges

#### Automate 4.1 : têtes_trichomes avant tiges
```
<relation>
têtes_trichomes | r_se_trouve_dans | tiges ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"têtes_trichomes" 122 37 1 14
"tiges" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$têtes_trichomes |r_se_trouve_dans| tiges>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

#### Automate 4.2 : tiges avant têtes_trichomes
```
<relation>
tiges | r_se_trouve_dans | têtes_trichomes ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"tiges" 122 37 1 14
"têtes_trichomes" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$têtes_trichomes |r_se_trouve_dans| tiges>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

### Relation 5 : écrans_tamisage | r_a_comme_caracteristique | pores

#### Automate 5.1 : écrans_tamisage avant pores
```
<relation>
écrans_tamisage | r_a_comme_caracteristique | pores ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"écrans_tamisage" 122 37 1 14
"pores" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$écrans_tamisage |r_a_comme_caracteristique| pores>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

#### Automate 5.2 : pores avant écrans_tamisage
```
<relation>
pores | r_a_comme_caracteristique | écrans_tamisage ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"pores" 122 37 1 14
"écrans_tamisage" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$écrans_tamisage |r_a_comme_caracteristique| pores>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

### Relation 6 : bubble_hash | r_peut | atteindre_fusion_complète

#### Automate 6.1 : bubble_hash avant atteindre_fusion_complète
```
<relation>
bubble_hash | r_peut | atteindre_fusion_complète ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"bubble_hash" 122 37 1 14
"atteindre_fusion_complète" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$bubble_hash |r_peut| atteindre_fusion_complète>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

#### Automate 6.2 : atteindre_fusion_complète avant bubble_hash
```
<relation>
atteindre_fusion_complète | r_peut | bubble_hash ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"atteindre_fusion_complète" 122 37 1 14
"bubble_hash" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$bubble_hash |r_peut| atteindre_fusion_complète>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

### Relation 7 : dry_sift | r_peut | produire_rosin_qualité

#### Automate 7.1 : dry_sift avant produire_rosin_qualité
```
<relation>
dry_sift | r_peut | produire_rosin_qualité ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"dry_sift" 122 37 1 14
"produire_rosin_qualité" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$dry_sift |r_peut| produire_rosin_qualité>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

#### Automate 7.2 : produire_rosin_qualité avant dry_sift
```
<relation>
produire_rosin_qualité | r_peut | dry_sift ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"produire_rosin_qualité" 122 37 1 14
"dry_sift" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$dry_sift |r_peut| produire_rosin_qualité>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

### Relation 8 : paint_roller_tech | r_est_un_type_de | technique_nettoyage

#### Automate 8.1 : paint_roller_tech avant technique_nettoyage
```
<relation>
paint_roller_tech | r_est_un_type_de | technique_nettoyage ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"paint_roller_tech" 122 37 1 14
"technique_nettoyage" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$paint_roller_tech |r_est_un_type_de| technique_nettoyage>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

#### Automate 8.2 : technique_nettoyage avant paint_roller_tech
```
<relation>
technique_nettoyage | r_est_un_type_de | paint_roller_tech ;
Main 15
"<E>" 21 77 1 13 ""
1001 78 0
"technique_nettoyage" 122 37 1 14
"paint_roller_tech" 499 49 1 9
"<WF>" 327 34 3 4 8 10
"<WF>" 708 38 2 5 11
"<P>" 272 149 2 6 4
"<P>" 724 110 2 7 11
"<P>" 384 173 2 8 10
"$)" 614 41 2 5 7
"$(B" 463 46 1 3
"<E>" 816 76 1 12
"<$paint_roller_tech |r_est_un_type_de| technique_nettoyage>" 783 256 1 1
"$(A" 96 34 1 2
"$)" 253 28 2 4 6
```

## Notes techniques

### Format NooJ
- Tous les automates respectent le format **Main 15** de NooJ
- Les sorties maintiennent l'ordre logique des relations : `<$A |relation| B>`
- Chaque relation génère deux automates pour capturer les deux ordres d'apparition possibles dans le texte

### Types de relations utilisées
- **r_est_un_type_de** : Relations taxonomiques
- **r_a_comme_partie/element** : Relations méronymiques 
- **r_se_trouve_dans** : Relations spatiales
- **r_a_comme_caracteristique** : Relations attributives
- **r_peut** : Relations de capacité/possibilité

### Application
Ces automates peuvent être utilisés dans NooJ pour :
1. Identifier automatiquement les relations sémantiques dans des textes sur le cannabis
2. Construire des graphes de connaissances
3. Enrichir des bases de données terminologiques
4. Développer des ontologies du domaine