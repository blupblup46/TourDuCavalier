from collections import deque




graph = {
    "1" : {"2", "3", "6"},
    "2" : {"1", "3", "4"},
    "3" : {"1", "2", "4"},
    "4" : {"2", "3", "5"},
    "5" : {"4"},
    "6" : {"1"}
}

##Initialisation du dictionnaire des distances



def init (depart):
    
    for boucle in range (len(graph)):
        D.append(None)
        
    index=int(depart)-1
    D.pop(index)
    D.insert(index, 0)
    
    return D


def dfs (depart): 
    
    if depart not in visite:
        
        visite.append(depart)
        
        for voisin in graph[depart]:
            if (voisin not in visite):
                D[int(voisin)-1]= D[int(depart)-1] + 1
            dfs(voisin)
            
            

def affichage():
    
    max = len(graph)
    compteur= 0
    nombreValeurs=D.count(compteur)
    
    while (max> compteur and nombreValeurs!=0):
        
        print("sommet(s) au niveau #"+ str(compteur+1))
        boucle=0
        debut=0
        
        while (boucle< nombreValeurs):
            
            index=D.index(compteur, debut, len(D))
            print(index+1)
            boucle+=1
            debut=index+1
            
        compteur+=1
        nombreValeurs=D.count(compteur)
        
        
DEPART = "1"        
D=[]
D=init(DEPART)
print(D)

visite=[]
dfs(DEPART)


print(visite)
print(D)

