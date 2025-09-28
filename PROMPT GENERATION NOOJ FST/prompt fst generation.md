# ✅ PROMPT CORRIGÉ POUR EXTRACTION COMPLÈTE SANS DICTIONNAIRES IMBRIQUÉS

## Consigne :

Dans le cadre de la création d'une base de connaissances, une relation sémantique s'écrit **A | R | B** où A et B sont des termes et R un type de relation. La relation se termine par un point-virgule `;`.

À partir d'un texte, extrais **TOUTES** les relations sémantiques possibles sous la forme :
**A | R | B ;**

où :
- A et B sont des termes (entités nommées, groupes nominaux ou mots simples),
- R est une relation parmi :
    - **r_est_un_type_de**
    - **r_se_trouve_dans** 
    - **r_a_comme_caracteristique**
    - **r_peut**
    - **r_a_comme_partie/element**
    - **r_fait_partie_de**
    - **r_permet_de**
    - **r_necessite**
    - **r_produit**
    - **r_utilise**

---

## Extraction EXHAUSTIVE des relations

### Principe : 
1. **Analyser chaque phrase** pour identifier toutes les entités et leurs relations
2. **Extraire TOUS les cas possibles** : synonymes, variantes, expressions complexes
3. **Considérer les relations implicites** et explicites
4. **Inclure les relations bidirectionnelles** quand pertinentes
5. **Traiter les énumérations** et listes comme relations multiples

### Exemples d'extraction exhaustive :
- Si le texte mentionne "le hachisch à tamiser à sec est une forme de hachisch" → `hachisch à tamiser à sec | r_est_un_type_de | hachisch ;`
- Si "les trichomes font partie de la plante" → `trichomes | r_fait_partie_de | plante ;`
- Si "le tamisage permet de séparer" → `tamisage | r_permet_de | séparation ;`
- Si "écrans de 60 LPI, 88 LPI, 100 LPI" → relations multiples pour chaque valeur

---

## Génération des automates NooJ OPTIMISÉS

### Format strict d'un automate NooJ :

```
<nom_relation>
<entité_A> | relation | <entité_B> ;
Main
15
"<E>" 21 77 1 13 
"" 1001 78 0 
"terme1|terme2|terme3" 122 37 1 14 
"terme4|terme5" 499 49 1 9 
"<WF>" 327 34 3 4 8 10 
"<WF>" 708 38 2 5 11 
"<P>" 272 149 2 6 4 
"<P>" 724 110 2 7 11 
"<P>" 384 173 2 8 10 
"$)" 614 41 2 5 7 
"$(B" 463 46 1 3 
"<E>" 816 76 1 12 
"<$A |nom_de_la_relation| $B>" 783 256 1 1 
"$(A" 96 34 1 2 
"$)" 253 28 2 4 6
```

### ⚠️ RÈGLES CRITIQUES :

1. **Listes directes dans les nœuds** : Utiliser `"terme1|terme2|terme3"` au lieu de `<DIC_nom>`
2. **Pas de dictionnaires séparés** : Tout est intégré dans les nœuds de l'automate
3. **Expressions complètes** : Inclure variantes, synonymes, formes fléchies
4. **Sortie standardisée** : Toujours `"<$A |nom_de_la_relation| $B>"`
5. **Relations bidirectionnelles** : Créer 2 automates si nécessaire (A→B et B→A)

### Exemple concret d'optimisation :

Au lieu de :
```
<DIC_outils>
tamis,N+FLX=Sing+Sem=outil
écran,N+FLX=Sing+Sem=outil
```

Utiliser directement :
```
"tamis|écran|filtre|grille" 122 37 1 14
```

---

## Structure de sortie demandée

1. **Liste complète des relations extraites** (format A | R | B ;)
2. **Pour chaque relation unique** :
   - **Automate A→B** (quand A précède B dans le texte)
   - **Automate B→A** (quand B précède A dans le texte)
   - **Listes de termes intégrées** dans chaque nœud
   - **Sortie identique** : `"<$A |nom_de_la_relation| $B>"`

3. **Variantes linguistiques** à inclure dans les listes :
   - Formes au singulier/pluriel
   - Synonymes courants
   - Expressions techniques/familières
   - Abréviations et formes complètes

---

## Consignes spécifiques pour le texte fourni

En analysant le texte sur le tamisage à sec, extrais notamment :

- **Termes techniques** : tamisage, criblage, sift, hash, trichomes, etc.
- **Équipements** : écrans, filtres, rouleaux, cartes, etc.
- **Processus** : extraction, séparation, collecte, pressage, etc.
- **Matériaux** : cannabis, résine, contaminants, etc.
- **Mesures** : LPI, microns, températures, pressions, etc.
- **Relations causales** : permet de, nécessite, produit, etc.

Génère des automates robustes capables de reconnaître toutes les variantes et expressions du domaine.