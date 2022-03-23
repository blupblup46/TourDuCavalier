import grapheDeplacements
import networkx as nx
import matplotlib.pyplot as plt 

##Initialisation du dictionnaire des distances

def dfs_cavalierEdition (depart): 
    
    if depart not in visite:
        
        visite.append(depart)
        Q.pop()
            
        #print(visite)
        
        voisinTrie = list()
        
        for boucle in range (len(graph[depart])):
            minPosibilite= 999
            minSommet = 1
            for voisin in graph[depart]:
                
                
                if (voisin not in voisinTrie):
                    if (minPosibilite > len(graph[voisin])):
                        minPosibilite = len(graph[voisin])
                        minSommet = voisin
            
            voisinTrie.append(minSommet)
                
        for voisin in voisinTrie:
            if (voisin not in visite):
                    #print(graph[voisin])
                    dfs_cavalierEdition(voisin)
       
        if (len(Q)!=0 ):
            visite.pop()
            Q.append(1)
        
def afficherResultat():
    if visite!=[]:
        resultat = nx.Graph()
        resultat.add_nodes_from(graph.keys())
        listeArrete = []
        for i in range(len(visite)-1):
            listeArrete.append([visite[i],visite[i+1]])
        resultat.add_edges_from(listeArrete)
        nx.draw(resultat,with_labels=True,font_weight="bold")
        plt.show()
    else:
        print("Aucun chemin trouvé")
    print(visite)

visite=[]
Q=[]

nbLigne=int(input("Saisir le nombre de ligne : "))
nbColone=int(input("Saisir le nombre de colone : "))

graph = grapheDeplacements.grapheDeplacementsCavalier(nbColone,nbLigne)
DEPART=int(input("Saisir le sommet de départ : "))

print("recherche...")
for sommet in graph.keys():
    Q.append(sommet)

dfs_cavalierEdition(DEPART)

afficherResultat()