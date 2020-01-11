
#  ex 3.10 de :
#  Audray Carré Legros Petrov Rezzouk, Informatique, Dunod, 2017

# ORBITALES ATOMIQUES

#############QUESTION 0 ###################
def couche_suivante(n,l):
    if l != 0:
        return n+1, l-1
    else:
        return n+1-n//2 , n//2

# print(couche_suivante(4,2))
# print(couche_suivante(4,0))

#############QUESTION 1 ###################

def souscouches(Z):   # Z : numéro atomique = nombre d'électons de l'atome
    C = []
    n = 1
    l = 0
    electrons_restant = Z
    while electrons_restant > 0:
        electrons_sous_couche = 2*(2*l + 1) # nombre max d'electrons pour cette sous-couche
        if electrons_sous_couche <= electrons_restant:
            # C[n-1][l] <- electrons_sous_couche
            if l == 0:
                C.append([electrons_sous_couche])
            else:
                C[n-1].append(electrons_sous_couche)
            electrons_restant = electrons_restant - electrons_sous_couche
        else:
            # C[n-1][l] <- electrons_restant
            if l == 0:
                C.append([electrons_restant])
            else:
                C[n-1].append(electrons_restant)
            electrons_restant = 0
        n, l = couche_suivante(n, l)
    return C

def to_string(C):
    nsc = ["s","p","d","f","g","h"] # nom des sous-couches
    sc = [] # sous-couches 
    for i in range(len(C)):
        for j in range(len(C[i])):
            sc.append(str(i+1) + nsc[j] + str(C[i][j]))
    configuration = " ".join(sc)
    return configuration

C = souscouches(14)
print(to_string(C))
