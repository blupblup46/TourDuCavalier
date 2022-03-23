import networkx as nx 
import matplotlib.pyplot as plt
import mygraph

def grapheDeplacementsCavalier(nbColone,nbLigne):
    echiquier = dict()
    for k in range(nbColone*nbLigne):
        ligne=k//nbColone
        colone=k%nbColone
        echiquier[k]=[]
    
        if (0<=ligne-2<nbLigne)and(0<=colone-1<nbColone):
            echiquier[k].append((ligne-2)*nbColone+(colone-1))

        if (0<=ligne-1<nbLigne)and(0<=colone-2<nbColone):
            echiquier[k].append((ligne-1)*nbColone+(colone-2))

        if (0<=ligne-2<nbLigne)and(0<=colone+1<nbColone):
            echiquier[k].append((ligne-2)*nbColone+(colone+1))

        if (0<=ligne-1<nbLigne)and(0<=colone+2<nbColone):
            echiquier[k].append((ligne-1)*nbColone+(colone+2))

        if (0<=ligne+1<nbLigne)and(0<=colone-2<nbColone):
            echiquier[k].append((ligne+1)*nbColone+(colone-2))

        if (0<=ligne+2<nbLigne)and(0<=colone-1<nbColone):
            echiquier[k].append((ligne+2)*nbColone+(colone-1))

        if (0<=ligne+1<nbLigne)and(0<=colone+2<nbColone):
            echiquier[k].append((ligne+1)*nbColone+(colone+2))
        
        if (0<=ligne+2<nbLigne)and(0<=colone+1<nbColone):
            echiquier[k].append((ligne+2)*nbColone+(colone+1))
    
    return echiquier

def affichage(nbColone,nbLigne):
    graphe = grapheDeplacementsCavalier(nbColone,nbLigne)
    affichage = nx.Graph()
    affichage.add_nodes_from(mygraph.Graphe(graphe).all_sommets())
    affichage.add_edges_from(mygraph.Graphe(graphe).all_aretes())
    nx.draw(affichage,with_labels=True,font_weight="bold")
    plt.show()