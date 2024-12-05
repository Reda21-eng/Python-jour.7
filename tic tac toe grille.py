
# créer un grille tic_tac_toe
grille =  ["-","-","-",
           "-","-","-",
           "-","-","-"]
joueur_actuel="X"
gagnant=None
partie_en_cours= True


## Créer la grille
def print_grille(grille) :
   print(grille [0]+'|'+ grille[1]+'|'+grille[2])
   print("-----")
   print(grille [3]+'|'+ grille[4]+'|'+grille[5])
   print("-----")
   print(grille [6]+'|'+ grille[7]+'|'+grille[8])

print_grille(grille)   
