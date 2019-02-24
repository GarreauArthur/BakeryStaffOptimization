Issue : How to optimize staff scheduling for 18 bakeries taking into account constraints such as labor laws, staff leave and sick days, preferences, etc...

This is a constrained combinatorial optimization problem.
I will attempt to solve it by implementing a genetic algorithm.

The chromosomes are implemented as schedule objects which main attribute is a list of assignment objects. A schedule covers a week.

Since I could not come up with a good way of representing the chromosomes as binary sequences, mutations are implemented as follows. They affect the assignment objects in six possible different ways :
    - Extend : adds 15 minutes to the assignment, if two assignments conflict, the mutated one has priority
    - Reduce : -15 minutes
    - Split : splits an assignment in two down the middle
    - Merge : merges two touching assignments
    - Swap : swaps the workers on two assignments
    - Change : changes the worker on an assignment


Fitness is determined as follows :
There are mutiple factors taken into account in order to determine fitness, such as :
    - Remaining available working hours for the week
    - Max consecutive worked hours
    - Job descrition
    - Prefered bakery
    - Prefered schedule 
    - ...
A config file determines bonus and penalties for respecting or not each of the constraints. The fitness is the sum of these scores

For crossovers, the days are randomly swapped between the two chromosomes.

Json files are used as inputs and outputs to easily interface with the web app developped in parallel.

--------------

## Analyse du code

* **config.txt** : un fichier texte contenant des paramètres
* **Constants.py** : une classe qui parse config.txt, ça aurait été plus simple d'avoir un seul fichier constants.py avec les contantes directement
* **ScheduleAssignment** : une tâche à faire dans le schedule
* **ScheduleOptimizer.py** : implements a genetic algorithm to solve this optimization problem
* **StoreSchedule** : A Store's schedule, what we are trying to optimize (1 week = 1 individual of the pop = 1 chromosome)
* **Visualizer** : A quickly done visualizer for generated schedules
* **Worker** : Object defining the workers
* **WorkerSchedule** : Defines the schedule of the worker
* **Workforce** :


The chromosomes are implemented as schedule objects (StoreSchedule) which main attribute is a list of assignment objects (ScheduleAssignment). A schedule covers a week.

### Input

The input is a JSON file, composed of 2 main elemnts:

* "schedule": is an object containing an object for every day of the week, each containing a list of tasks
* "worker": is a list containing object representing the staff members (workers)


    {
        "schedule": {
            "mon": [
                [job, start, end, store, importance]
            ],
        }

        "worker": [
            {first name, last name, normal hours, hours left, jobs, store, rest}
        ]
    }


Let's find where the input is processed

ScheduleOptimizer.py "has a main". It first load the data from the json file, and
passed it to the constructor of Scheduler. The data is then given to a StoreSchedule.
StoreSchedule create the workforce. Then Scheduler.generate_initial_population()
is called and generates an arbitrary schedule that fits the desired schedule, but
not the workers constraints.

---------------
Pour générer les diagrammes j'ai utilisé pyreverse (inclus dans pylint)
`pyreverse -o png ./*.py`

-------------
Intel conversation with Pierre Leroy

Quand l'utilisateur clique sur le bouton IA sur le site web, le script python
est exécuté. L'IA doit pouvoir générer pour une boulangerie à la fois
uniquement, et pour une semaine complète (lundi au dimanche).

En entrée :

* liste d'exigence par jour
* liste de worker
  * un id
  * nombre d'heures semaime normale
  * nombre d'heures qui reste (possibilité d'ajouter des heures manuellement,
puis d'utiliser l'IA (donc en gros, ce n'est pas l'IA qui doit gérer les heures
en plus))
  * compétences
  * liste de jours et d'heures indisponibles

Compétence priorité numéro 1  

pour l'instant l'algo peut donner des horaires de merde :  6.14 à 6.29 puis
7.2 à 8.35 puis 12.65 à 19h
et il va mettre 60h à un collaborateur et 0 aux autres
il donne des compétences à des workers qui ne les ont pas et ça c'est vraiment
la priorité

20/02/2019

pour l'exemple simple de pierre, l'algo fonctionne à peu près mais renvoie des
warnings bizarres, donc, je vais regarder ça et drop le taux de mutation



VENDREDI

[x] envoyer message à théo

[ ] modifier `Workforce.get_best_worker_for_job`
[ ] modifier mutation

[ ] modifier fitness
[ ] modifier population intiale







J'ai discuté avec Pierre et ça m'a permis de voir un peu plus clair sur la situation actuelle,
le site web envoie le planning de la semaine pour une seule boulangerie avec
la liste des employés ; et le but de l'IA est d'associer des personnes aux heures
planifiées. L'utilisateur du site a la possibilité d'ajouter des heures supplémentaires aux employés
manuellement puis d'utiliser l'IA. Du coup ça rend le problème plus simple, mais
ça veut aussi dire que le besoin client n'est peut être pas respecté. En cas
d'urgence, d'arrêt maladie... le client devra sélectionner lui-même les collabolateurs
et les heures en plus dont il a besoin.

Alexis a pourtant mis en place un moyen de gérer les employés de différentes
boulangeries.

Cependant, ce qu'a fait Alexis ne fonctionne pas, même sur un exemple simple.
L'algo va donner des heures comme de 6.14 à 6.29 puis 7.2 à 8.35 puis 12.65 à 19h.
Il va mettre 60h à une personne et 0 aux autres. Il donne des compétences à des
workers qui ne les ont pas. Pierre est obligé de faire des fusions et des
réarrangements.

J'ai quelques pistes pour faire fonctionner l'algo, mais si ça ne fonctionne pas,
je pense que le plus simple sera de tout refaire.
