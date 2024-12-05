import random

grille =  ["-","-","-",
           "-","-","-",
           "-","-","-"]
joueur_actuel="O"
gagnant=None
partie_en_cours= True



# Créer la grille
def print_grille(grille) :
   print(grille [0]+'|'+ grille[1]+'|'+grille[2])
   print("-----")
   print(grille [3]+'|'+ grille[4]+'|'+grille[5])
   print("-----")
   print(grille [6]+'|'+ grille[7]+'|'+grille[8])




# Saisir nombre utilisateur
def print_joueur(grille):
    inp=int(input("Choisir un nombre entre 1-9 : "))
    if inp >=1 and inp <=9 and grille[inp-1] == "-":
      grille[inp-1] =joueur_actuel
    else :
      print("Il y a déjà un joueur sur cette case ") 

#Vérifier conditions de victoire ou de match nul"
def verifier_ligne(grille) :
    global gagnant
    if grille[0]==grille[1]==grille[2] and grille [0] !="-":
        gagnant=grille[0] 
        return True
    elif grille[3]==grille[4]==grille[5] and grille [3] !="-":
        gagnant=grille[3]
        return True
    elif grille[6]==grille[7]==grille[8] and grille [6] !="-":
         gagnant=grille[6]
         return True 
         
def verifier_colonne (grille) :
    global gagnant
    if grille[0] == grille[3] == grille[6] and grille [0] !="-":
        gagnant=grille[0]
        return True
    elif grille [1] == grille[4] == grille[7] and grille [1] !="-":
        gagnant=grille[1]
        return True
    elif grille [2] == grille[5] == grille [8] and grille [2] != "-":
        gagnant = grille[2]
        return True

def verifier_diagonale (grille):   
      global gagnant
      if grille[0] == grille [4] == grille [8] and grille [0] != "-":
          gagnant=grille[0]
          return True
      elif grille [3] == grille[4] == grille [5] and grille [3] !="-":
          gagnant=grille [3]
          return True
      
          
# Verifier match nul
def verifier_match_nul (grille):
    global partie_en_cours
    if"-"not in grille  :
        print (" Match nul ! ")
        partie_en_cours=False 
    



# Fonction victoire pour éviter de répéter les autres conditons
def verifier_victoire (grille):
       if verifier_ligne(grille) or verifier_colonne(grille) or verifier_diagonale(grille) :
          print (f"Victoire de {gagnant}")
          
       


# Inverser Joueur
def inverser_joueur():
    global joueur_actuel
    if joueur_actuel=="X":
        joueur_actuel="O"
    else :
        joueur_actuel = "X"
inverser_joueur ()

# Partie contre ordinateur
def ordinateur (grille):
   while joueur_actuel=="O":
      position =random.randint(0, 8)
      if grille[position] == "-":
          grille[position] = "O"
    
          inverser_joueur()
    




 # Afficher tour précédent chaque fois qu'on joue un coup 
while partie_en_cours :
 print_grille(grille)
 print_joueur(grille)
 verifier_victoire(grille)
 verifier_match_nul(grille)
 inverser_joueur()
 ordinateur (grille)
 verifier_victoire(grille)
 verifier_match_nul (grille)

 
  