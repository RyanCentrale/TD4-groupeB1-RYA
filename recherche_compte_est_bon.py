#! /usr/bin/env python3

""" Implémentation des parcours de l’arbre de calculs à la volée :
- parcours en profondeur d’abord itératif
- parcours en profondeur d’abord récursif
- parcours en largeur d’abord itératif """

#from TAD.piles_listes_python import Pile
#from TAD.files_listes_python import File
#from TAD.piles_listes_simplement_chainees import Pile
#from TAD.files_listes_doublement_chainees import File
from notation_polonaise_inverse import *

def parcours_DFS(cartons, cible) : 
    # cartons : une liste
    # cible : entier 
    nb_noeuds = 0
    meilleure_expression = []
    pile = Pile()
    etat_initial = ([],cartons)
    pile.empiler(etat_initial)
    while not pile.est_vide() :
        (expression_partielle,cartons_restants)=p.depiler()
        nb_noeuds += 1

        valideOuNon, valeurOuNone = eval_NPI_liste(expression_partielle)
        
        if valideOuNon:
            if valeurOuNone is not None:
                ecart = abs(cible - valeurOuNone)
                if ecart < meilleur_ecart:
                    meilleur_ecart = ecart
                    meilleure_expression = expression_partielle                    
                    if ecart == 0:
                        break
        
        # Option A : Piocher un nouveau carton
        for i in range(len(cartons_restants)):
            nouvelle_expression = expression_partielle + [cartons_restants[i]]
            nouveaux_restants = cartons_restants[:i] + cartons_restants[i+1:]
            p.empiler((nouvelle_exppression, nouveaux_restants))
            
        # Option B : Appliquer un opérateur
        for operateur in ['+', '-', '*', '/']:
            nouvelle_expression = expression_partielle + [operateur]
            p.empiler((nouvelle_expression, cartons_restants))
    
    return meilleure_expression, nb_noeuds

def parcours_BFS(cartons, cible) : 
    # cartons : une liste
    # cible : entier 
    nb_noeuds = 0
    meilleure_expression = []

    return meilleure_expression, nb_noeuds 

def parcours_DFS_recursif(cartons, cible) :
    meilleure_expression = []
    nb_noeuds = 0

    def parcours_DFSR_aux(choisis, restants) :
        nonlocal meilleure_expression
        nonlocal nb_noeuds
        nonlocal cible
        pass
        
    # Appeler parcours_DFSR_aux ! 

    return meilleure_expression, nb_noeuds


if __name__ == "__main__":
    parcours_DFS([3,5, 7, 9, 25, 50], 859)
    parcours_BFS([3,5, 7, 9, 25, 50], 859)
    parcours_DFS_recursif([3,5, 7, 9, 25, 50], 859)
 
