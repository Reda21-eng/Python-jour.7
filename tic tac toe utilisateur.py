 #créer un grille tic_tac_toe
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
# Saisir nombre utilisateur
def print_joueur(grille):
    inp=int(input("Choisir un nombre entre 1-9 : "))
    if inp >=1 and inp <=9 and grille[inp-1] == "-":
      grille[inp-1] =joueur_actuel
    else :
      print("Il y a déjà un joueur sur cette case ") 
print_joueur(grille)   
