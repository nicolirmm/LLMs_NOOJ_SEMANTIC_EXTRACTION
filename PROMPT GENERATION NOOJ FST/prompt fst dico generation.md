 ✅ PROMPT GÉNÉRIQUE (CORRIGÉ POUR SYNTAXE NooJ COMPLÈTE)

## Consigne :

Dans le cadre de la création d'une base de connaissances, une relation sémantique s'écrit **A | R | B** où A et B sont des termes et R un type de relation. La relation se termine par un point-virgule `;`.

À partir d'un texte, extrais toutes les relations sémantiques sous la forme :
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

---

## Dictionnaires thématiques

Avant de générer les automates, identifie les **domaines thématiques** présents dans le texte et crée les **dictionnaires correspondants**.

### Format :
```
mot,N+FLX=Modèle+Sémantique
```

---

## Extraction des relations

1. Extrais toutes les relations valides **A | R | B ;**, même si A apparaît après B dans le texte ;
2. La **relation logique doit être conservée dans l’ordre A | R | B**, même si B précède A dans le texte ;
3. Chaque relation doit être logiquement cohérente et pertinente ;
4. **Ne pas dupliquer** A dans B ni vice-versa.

---

## Génération des automates NooJ (FORMAT STRICT "Main 15")

Pour chaque relation **A | R | B ;**, génère **deux automates** :

- Un automate où **A apparaît avant B** dans le texte ;
- Un automate où **B apparaît avant A** dans le texte.

Dans **les deux cas**, la sortie doit être **exactement** de la forme :

```
"<$A |nom_de_la_relation| B>"
```

> Exemple générique : `"<$A |r_est_un_type_de| $B>"` (pour illustrer la syntaxe)
> ⚠️ Dans les automates, A et B doivent être les termes extraits du texte, pas des balises. Seul l’exemple ci-dessus garde les balises pour illustrer la syntaxe.

---

### Format exact d’un automate NooJ :

```
<relation>
<DIC_partie> | r_a_comme_partie/element | <DIC_entier> ;
Main
15
"<E>" 21 77 1 13 
"" 1001 78 0 
"<DIC_partie>" 122 37 1 14 
"<DIC_entier>" 499 49 1 9 
"<WF>" 327 34 3 4 8 10 
"<WF>" 708 38 2 5 11 
"<P>" 272 149 2 6 4 
"<P>" 724 110 2 7 11 
"<P>" 384 173 2 8 10 
"$)" 614 41 2 5 7 
"$(B" 463 46 1 3 
"<E>" 816 76 1 12 
"<$A |r_a_comme_partie/element| $B>" 783 256 1 1 
"$(A" 96 34 1 2 
"$)" 253 28 2 4 6
```

### ⚠️ Points critiques à respecter :

- La ligne `"<$A |nom_de_la_relation| B>"` doit **toujours être générée dans cet ordre logique**, quel que soit l’ordre des entités dans le texte.
- Il est **strictement interdit d’inverser l’ordre logique** dans la ligne de sortie (ex. : `"<$B |...| $A>"` est invalide).
- A et B peuvent être des chaînes littérales ou des balises de dictionnaire (`<DIC_nom>`) si définis.
- `$A` et `$B` doivent **toujours rester littéraux** dans la ligne `"<$A |nom_de_la_relation| B>"`.
  - Exemple correct : `"<$A |r_a_comme_partie/element| $B>"`
  - Exemple incorrect : `"<$coquille |r_a_comme_partie/element| escargot>"`

---

## Résumé de sortie

1. Dictionnaire(s) thématique(s) au bon format
2. Liste des relations extraites
3. Pour chaque relation :
   - Automate 1 (A avant B)
   - Automate 2 (B avant A)
   - Avec sortie identique : `"<$A |nom_de_la_relation| B>"`
