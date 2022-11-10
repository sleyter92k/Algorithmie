print("Bienvenue dans le jeu du morpion!")
print("Les règles sont simple: le but est d'aligner trois chasubles pour faire un Morpion. ")

# Afficher la grille
def afficher_grille(grille): 
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3): #range(3) nous renvoit à: [0,1,2]
        print(" | " + str(grille[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | " + str(grille[i + 3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | " + str(grille[i + 6]), end='')
    print(" |")
    print("   -------------")

# Intro
joueur = 1
print("Le joueur 1 possède les ❌. Le joueur 2 possède les O")
grille = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
afficher_grille(grille)
gagne = 0

# Fonctionnement des tours
def tour(grille, joueur):
    print("C'est le tour du joueur " + str(joueur))
    colonne = input("Entrez le numero de la colonne : ")
    ligne = input("Entrez le numero de la ligne : ")
    print("Vous avez joué la case (" + colonne + ";" + ligne + ")")
    
# Empêchement anomalie du jeu 
    n = ['0', '1', '2'] #si la case sélectionné n'est pas vide alors on renvoie le message du choix des cases.
    while colonne not in n or ligne not in n :
        print("Tu dois choisir un chiffre compris entre 0 et 2")
        colonne = input("Entrez le numero de la colonne : ")
        ligne = input("Entrez le numero de la ligne : ")

    while grille[int(colonne) + int(ligne) * 3] != " ":
        afficher_grille(grille)
        print("Cette case est deja jouée ! Saisissez une autre case svp !")
        colonne = input("Entrez le numero de la colonne : ")
        ligne = input("Entrez le numero de la ligne : ")
        print("Vous avez joué la case (" + colonne + ";" + ligne + ")")

    if joueur == 1:
        grille[int(colonne) + int(ligne) * 3] = "❌"
    if joueur == 2:
        grille[int(colonne) + int(ligne) * 3] = "0"


# Détection des victoires
def est_gagnant(grille):
    if (grille[0] == grille[1]) and (grille[0]== grille[2]) and (grille[0] != " "):
        return 1
    if (grille[3] == grille[4]) and (grille[3]== grille[5]) and (grille[3] != " "):
        return 1
    if (grille[6] == grille[7]) and (grille[6]== grille[8]) and (grille[6] != " "):
        return 1
    if (grille[0] == grille[3]) and (grille[0]== grille[6]) and (grille[0] != " "):
        return 1
    if (grille[1] == grille[4]) and (grille[1]== grille[7]) and (grille[1] != " "):
        return 1
    if (grille[2] == grille[5]) and (grille[2]== grille[8]) and (grille[2] != " "):
        return 1
    if (grille[0] == grille[4]) and (grille[0]== grille[8]) and (grille[0] != " "):
        return 1
    if (grille[2] == grille[4]) and (grille[2]== grille[6]) and (grille[2] != " "):
        return 1

# Détection des matchs nuls
def est_match_nul(grille):
    for i in range(9):
        if grille[i] == " ": #si l'une des cases est vide alors return 0 = ok
            return 0 #return faux d'une fonction
    return 1 #return vrai d'une fonction

# Détection du gagnant
while gagne == 0:
    tour(grille, joueur)
    if est_gagnant(grille):
        print("Le joueur " + str(joueur) + " remporte la partie")
        gagne = 1
    else:
        if est_match_nul(grille):
            print("Plus de place ! Match nul !")
            gagne = 1
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1
