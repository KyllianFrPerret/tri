def fusion(T1,T2):
    """
        Fusionne les tableaux triés T1 et T2 en conservant l'ordre. Le tri est croissant.

        Entrées :
            * T1 : list -> tableau d'entiers trié dans l'ordre croissant
            * T2  :list -> tableau d'entiers trié dans l'ordre croissant

        Sortie : list -> tableau d'entiers trié dans l'ordre croissant qui contient une fois tous les éléments de T1 et tous les éléments de T2 (doublons possible)
    """
    # tableau fusionné
    rep = []

    # compteurs pour parcourir T1 et T2
    compteurT1 = 0
    compteurT2 = 0

    # boucle de fusion
    for _ in range(len(T1)+len(T2)):
        # si le compteurT1 est trop grand
        # il ne reste des éléments que dans T2
        if compteurT1 >= len(T1):
            rep.append(T2[compteurT2])
            compteurT2 = compteurT2 + 1
        # si le compteurT2 est trop grand
        # il ne reste des éléments que dans T1
        elif compteurT2 >= len(T2):
            rep.append(T1[compteurT1])
            compteurT1 = compteurT1 + 1
        # sinon il reste des éléments dans
        # les deux tableaux,
        # on prend alors le plus petit des deux
        elif T1[compteurT1] < T2[compteurT2]:
            rep.append(T1[compteurT1])
            compteurT1 = compteurT1 + 1
        else:
            rep.append(T2[compteurT2])
            compteurT2 = compteurT2 + 1

    return rep


def triFusion(T):
    """
        Tri le tableau T à l'aide d'un algorithme de tri fusion.
        Entrée :
            T : list -> un tableau d'éléments comparables.
        Sortie : list -> un tableau contenant les éléments de T triés dans l'ordre croissant.
    """
    # Cas d'arrêt
    if len(T) == 1 :
        return T
    else:
        # Diviser
        # je coupe mon tableau en 2 sous-tableaux de tailles proches
        # T1 = []
        # for i in range(len(T)//2):
        #     T1.append(T[i])
        T1 = [T[i] for i in range(len(T)//2)]
        # T2 = []
        # for i in range(len(T)//2,len(T)):
        #     T2.append(T[i])
        T2 = [T[i] for i in range(len(T)//2,len(T))]

        # Régner
        # je trie T1 et T2
        T1 = triFusion(T1)
        T2 = triFusion(T2)

        # Recombiner
        # je fusionne T1 et T2
        return fusion(T1,T2)

def triSelection(T):
    """
        Tri par sélection du tableau T
        Entrée :
            * T : list -> un tableau d'éléments comparables
        Sortie : aucune (tableau trié)
    """
    for i in range(len(T)-1):
        indMin = i
        for j in range(i,len(T)):
            if T[j] < T[indMin]:
                indMin = j
        swap = T[i]
        T[i] = T[indMin]
        T[indMin] = swap


def triInsertion(T):
    """
        Tri croissant par insertion du tableau T
        Entrée :
            * T : list -> un tableau d'éléments comparables
        Sortie : aucune (tableau trié)
    """

    # pour tous les éléments du tableau (à partir du deuxième)
    for indice in range(1,len(T)):
        swap = T[indice]
        compteur = indice

        # tant que je ne suis pas au début et que l'élément d'avant est plus grand je remonte vers la gauche
        while (compteur > 0) and (T[compteur-1] > swap):
            T[compteur] = T[compteur-1]
            compteur = compteur - 1

        T[compteur] = swap

def inser(T):
    for i in range(1,len(t)):
        cont=i
        while cont>0 and T[cont-1]>T[cont]:
            T[cont-1],T[cont]=T[cont],T[cont-1]
            cont=cont-1

    return T



## Tests
from random import randint
import timeit

T1 = [randint(1,1_000_000) for _ in range(20000)]
T2 = [elt for elt in T1]
T3 = [elt for elt in T1]

print('Sélection ->',timeit.timeit('triSelection(T1)',number=1,globals=globals()))
print('Insertion ->',timeit.timeit('triInsertion(T2)',number=1,globals=globals()))
print('Fusion ->',timeit.timeit('triFusion(T3)',number=1,globals=globals()))










