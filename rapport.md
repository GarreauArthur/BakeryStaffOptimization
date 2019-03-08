## Description du problème

décrire le problème

problème d'optimisation combinatoire

Le terme Intelligence Artificielle (IA ou AI) est généralement utilisé dans les
problèmes dont l'écriture d'un programme capable de trouver la solution est très difficile voire impossible.

## Analyse de l'existant

###

### Algorithme génétique

#### principe

L'algorithme utilisé est un algorithme génétique. Le principe est le suivant :
Une population d'invidus initiale est créée.  Chaque individu de la population 
est évalué grâce à une fonction de "fitness". Les individus ayant obtenu les
meilleurs scores (les mieux adaptés) sont conservés pour créer la population
suivante. Cette nouvelle population est créé en partie grâce à cette
sélection, mais également par des croisements (crossover), les chromosomes des
individus sont divisés et mélangés pour former de nouveaux individus. Pour 
apporter de la diversité génétiques des mutations aléatoires sont effectuées.
Ces opérations sont répétés sur plusieurs générations, jusqu'à ce qu'une des conditions suivantes est respectée :

* le score converge vers une limite
* le nombre de générations maximum est dépassé
* l'objectif est rempli


#### motivation

Un algorithme génétique ne semble pas être une mauvaise idée pour résoudre

Cependant, il ne prend pas en compte certaines heuristiques que l'on pourrait faire pour simplifier le programme

#### Implémentation

Ici un individu représente un planning.

`Scheduler.generate_initial_schedule` génère un planning arbitraire qui remplit
le planning désiré sans respecter les contraintes des travailleurs. La
population initiale est créée dans `Scheduler.generate_initial_population`.




### diagramme des classes

### Problème

