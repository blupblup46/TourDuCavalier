import networkx as nx 
import matplotlib.pyplot as plt
import mygraph
import random

def grapheplateauCarre(n):

    echiquier = dict()

    for k in range(n*n): # n*n -> dimentions de l'échequier
        i = k//n         #ligne de la case k
        j = k%n          #colone de la case k
        echiquier[k]=[]  #liste des voisins de la case k

        if  (0<=i-2<n) and (0<=j-1<n) : 
            echiquier[k].append((i-2)*n+(j-1))

        if  (0<=i-2<n) and (0<=j+1<n) : 
            echiquier[k].append((i-2)*n+(j+1))

        if  (0<=i-1<n) and (0<=j-2<n) : 
            echiquier[k].append((i-1)*n+(j-2))

        if  (0<=i-1<n) and (0 <=j+2<n) : 
            echiquier[k].append((i-1)*n+(j+2))

        if  (0<=i+1<n) and (0<=j-2<n) : 
            echiquier[k].append((i+1)*n+(j-2))

        if  (0<=i+1<n) and (0<=j+2<n) : 
            echiquier[k].append((i+1)*n+(j+2))

        if  (0<=i+2<n) and (0<=j-1<n) : 
            echiquier[k].append((i+2)*n+(j-1))

        if  (0<=i+2<n) and (0<=j+1<n) : 
            echiquier[k].append((i+2)*n+(j+1))
    
    return echiquier

    

def affichageCarre(n):
    graphe = grapheplateauCarre(n)
    affichage = nx.Graph()
    affichage.add_nodes_from(mygraph.Graphe(graphe).all_sommets())
    affichage.add_edges_from(mygraph.Graphe(graphe).all_aretes())
    nx.draw(affichage,with_labels=True,font_weight="bold")
    plt.show()

affichageCarre(4)