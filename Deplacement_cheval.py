def plateauCarre(n):
    
    echequier = dict()

    for k in range(n*n): # n*n -> dimentions de l'échequier
        i = k//n         #ligne de la case k
        j = k%n          #colone de la case k
        echequier[k]=[]  #liste des voisins de la case k

        if  (0<=i-2<n) and (0<=j-1<n) : 
            echequier[k].append((i-2)*n+(j-1))

        if  (0<=i-2<n) and  (0<=j+1<n) : 
            echequier[k].append((i-2)*n+(j+1))

        if  (0<=i-1<n) and  (0<=j-2<n) : 
            echequier[k].append((i-1)*n+(j-2))

        if  (0<=i-1<n) and  (0 <=j+2<n) : 
            echequier[k].append((i-1)*n+(j+2))

        if  (0<=i+1<n) and  (0<=j-2<n) : 
            echequier[k].append((i+1)*n+(j-2))

        if  (0<=i+1<n) and  (0<=j+2<n) : 
            echequier[k].append((i+1)*n+(j+2))

        if  (0<=i+2<n) and  (0<=j-1<n) : 
            echequier[k].append((i+2)*n+(j-1))

        if  (0<=i+2<n) and  (0<=j+1<n) : 
            echequier[k].append((i+2)*n+(j+1))
    
    print(echequier)
    return echequier


from collections import deque

##Initialisation du dictionnaire des distances

def dfs_cavalierEdition (depart, depart_statique, passe): 
    
    if depart not in visite:
        
        if (passe != 0):
            visite.append(depart)
            Q.pop()
            
        print(visite)

                
        for voisin in graph[depart]:
            
            if (voisin not in visite):
                
                
                
                #print(graph[voisin])
                dfs_cavalierEdition(voisin, depart_statique, passe+1)
       
        if (len(Q)!=0 ):
            visite.pop()
            Q.append(1)
        
        
        elif (len(Q)==0 and visite[-1]!= depart_statique):
            visite.pop()
            Q.append(1)
        
        
   
            
        

graph = plateauCarre(6)
visite=[]
Q=[]
DEPART = 5

print("recherche...")
for sommet in graph.keys():
    Q.append(sommet)
    
    
dfs_cavalierEdition(DEPART, DEPART, 0)
visite.insert(0, DEPART)

print("chemin = ")
print(visite)
