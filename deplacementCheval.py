import grapheDeplacements
import networkx as nx
import matplotlib.pyplot as plt 

def dfs_cavalierEdition (depart): 
    #Pour chaque sommets, on lance la recherche d'un chemin 
    
    if depart not in visite:
        
        visite.append(depart)
        Q.pop()
        
        voisinTrie = list() 
        #On fera le dfs a partir de cette liste de voisin triee sur le nombre de voisin a partir d'un des voisins de depart
        
        for boucle in range (len(graph[depart])):
            #Trie des voisins du sommet depart sur leurs nombre de voisins
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
            #S'il n'y a plus de voisins pour le sommet de depart mais qu'il reste encore des sommets dans la reserve Q, alors on rebrousse-chemin 
            visite.pop()
            Q.append(1)
        
def afficherResultat():
    #Recuperation des sommets et des arretes pour creer un affichage
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

#Programme principal
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
