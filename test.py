from collections import deque
import grapheDeplacement
import networkx as nx 
import matplotlib.pyplot as plt

##Initialisation du dictionnaire des distances
def dfs_cavalierEdition (depart): 
    
    if depart not in visite:
        
        visite.append(depart)
        Q.pop()
        
        for voisin in graph[depart]:
            if (voisin not in visite):
                #print(graph[voisin])
                dfs_cavalierEdition(voisin)
                
        if (len(Q) != 0):
            visite.pop()
            Q.append(1)


# affichage du résultat sous forme d'un graphe
def afficherResultat():
    if visite!=[]:
        res=nx.Graph()
        res.add_nodes_from(graph.keys())
        listeArrete=[]
        for i in range(len(visite)-1):
            listeArrete.append([visite[i],visite[i+1]])
        res.add_edges_from(listeArrete)
        nx.draw(res,with_labels=True,font_weight="bold")
        plt.show()
    else:
        print("Aucun chemin possible")



visite=[]
Q=[]

nbLigne=int(input("Nombre de ligne(s) : "))
nbColone=int(input("Nombre de colone(s) : "))
graph = grapheDeplacement.grapheDeplacementsCavalier(nbColone,nbLigne)

for sommet in graph.keys():
    Q.append(sommet)

sommetDepart=int(input("Par quel sommet commencer ?\nsaisis ton sommet : "))
print("recherche...")
dfs_cavalierEdition(sommetDepart)

afficherResultat()