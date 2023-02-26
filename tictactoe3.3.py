import random
import math

# Définition des symboles pour les joueurs
joueur = 'X'
IA = 'O'
VIDE = ' '

# Définition du tableau de jeu
damier = [VIDE] * 9

# Fonction pour afficher le tableau de jeu
def afficher_grille(damier):
    print(f"| {damier[0]} | {damier[1]} | {damier[2]} |")
    print(f"| {damier[3]} | {damier[4]} | {damier[5]} |")
    print(f"| {damier[6]} | {damier[7]} | {damier[8]} |")

# Fonction pour vérifier si un joueur a gagné
def combinaisons_gagnantes(damier, joueur):
    for i in range(0, 9, 3):
        if (damier[i] == damier[i+1] == damier[i+2] == joueur):
            return True
    for i in range(3):
        if (damier[i] == damier[i+3] == damier[i+6] == joueur):
            return True
    if (damier[0] == damier[4] == damier[8] == joueur):
        return True
    if (damier[2] == damier[4] == damier[6] == joueur):
        return True
    return False


# Fonction pour vérifier si le tableau est plein
def egalite(damier):
    for i in range(len(damier)):
        if damier[i]==VIDE:
            return False
    return True

#Initialisation des fonctions pour le niveau difficile
# Fonction pour minimax avec élagage alpha-beta
def minimax_difficile(damier, profondeur, alpha, beta, max_joueur):
    if combinaisons_gagnantes(damier, IA):
        return 1
    elif combinaisons_gagnantes(damier, joueur):
        return -1
    elif egalite(damier):
        return 0

    if max_joueur:
        max_eval = -math.inf
        for i in range(9):
            if damier[i] == VIDE:
                damier[i] = IA
                eval = minimax_difficile(damier, profondeur+1, alpha, beta, False)
                damier[i] = VIDE
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if damier[i] == VIDE:
                damier[i] = joueur
                eval = minimax_difficile(damier, profondeur+1, alpha, beta, True)
                damier[i] = VIDE
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Fonction pour le coup de l'IA
def coup_IA_difficile(damier):
    meilleure_eval = -math.inf
    meilleur_coup = None
    for i in range(9):
        if damier[i] == VIDE:
            damier[i] = IA
            eval = minimax_difficile(damier, 0, -math.inf, math.inf, False)
            damier[i] = VIDE
            if eval > meilleure_eval:
                meilleure_eval = eval
                meilleur_coup = i
    damier[meilleur_coup] = IA

def code_joueur_difficile():
        print("Le joueur humain est 'X'.")
        afficher_grille(damier)

        while True:
            # Tour du joueur humain
            coup_joueur = int(input("Choisissez une case de 1 à 9 : ")) - 1
            while damier[coup_joueur] != VIDE:
                coup_joueur = int(input("Case déjà prise, choisissez une case de 1 à 9 : ")) - 1
            damier[coup_joueur] = joueur
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, joueur):
                print("Le joueur humain a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break

            # Tour de l'IA
            print("Tour de l'IA...")
            coup_IA_difficile(damier)
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, IA):
                print("L'IA a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break

def code_IA_difficile():
        print("Le joueur humain est 'X'.")
        afficher_grille(damier)

        while True:
            # Tour de l'IA
            print("Tour de l'IA...")
            coup_IA_difficile(damier)
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, IA):
                print("L'IA a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break

            # Tour du joueur humain
            coup_joueur = int(input("Choisissez une case de 1 à 9 : ")) - 1
            while damier[coup_joueur] != VIDE:
                coup_joueur = int(input("Case déjà prise, choisissez une case de 1 à 9 : ")) - 1
            damier[coup_joueur] = joueur
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, joueur):
                print("Le joueur humain a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break



def morpion_difficile():
    choix_mode_de_jeu = int(input("Qui commence ? joueur (1), IA (2) ou aléatoire (3) ? : "))
    if choix_mode_de_jeu == 3 :
        choix_mode_de_jeu=random.choice([1,2])

    if choix_mode_de_jeu == 1 :
        print("Le joueur commence")
        code_joueur_difficile()

    if choix_mode_de_jeu == 2 :
        print("L'IA commence")
        code_IA_difficile()


#initialisation des fonctions pour le niveau moyen
def minimax_moyen(damier, profondeur, alpha, beta, max_joueur):
    if combinaisons_gagnantes(damier, IA):
        return 1
    elif combinaisons_gagnantes(damier, joueur):
        return -1
    elif egalite(damier):
        return 0

    if max_joueur:
        max_eval = -math.inf
        for i in range(9):
            if damier[i] == VIDE:
                damier[i] = IA
                eval = minimax_moyen(damier, profondeur+1, alpha, beta, False)
                damier[i] = VIDE
                max_eval = 0
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if damier[i] == VIDE:
                damier[i] = joueur
                eval = minimax_moyen(damier, profondeur+1, alpha, beta, True)
                damier[i] = VIDE
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Fonction pour le coup de l'IA

def coup_IA_moyen(damier):
    meilleure_eval = -math.inf
    meilleur_coup = None
    for i in range(9):
        if damier[i] == VIDE:
            damier[i] = IA
            eval = minimax_moyen(damier, 0, -math.inf, math.inf, False)
            damier[i] = VIDE
            if eval > meilleure_eval:
                meilleure_eval = eval
                meilleur_coup = i
    damier[meilleur_coup] = IA
    return meilleur_coup


def code_joueur_moyen():
        print("Le joueur humain est 'X'.")
        afficher_grille(damier)

        while True:
            # Tour du joueur humain
            coup_joueur = int(input("Choisissez une case de 1 à 9 : ")) - 1
            while damier[coup_joueur] != VIDE:
                coup_joueur = int(input("Case déjà prise, choisissez une case de 1 à 9 : ")) - 1
            damier[coup_joueur] = joueur
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, joueur):
                print("Le joueur humain a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break

            # Tour de l'IA
            print("Tour de l'IA...")
            coup_IA_moyen(damier)
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, IA):
                print("L'IA a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break

def code_IA_moyen():
    print("Le joueur humain est 'X'.")
    afficher_grille(damier)

    while True:
        # Tour de l'IA
        print("Tour de l'IA...")
        coup = coup_IA_moyen(damier)
        damier[coup] = IA
        afficher_grille(damier)

        if combinaisons_gagnantes(damier, IA):
            print("L'IA a gagné !")
            break
        if egalite(damier):
            print("Match nul !")
            break

        # Tour du joueur humain
        coup_joueur = int(input("Choisissez une case de 1 à 9 : ")) - 1
        while damier[coup_joueur] != VIDE:
            coup_joueur = int(input("Case déjà prise, choisissez une case de 1 à 9 : ")) - 1
        damier[coup_joueur] = joueur
        afficher_grille(damier)

        if combinaisons_gagnantes(damier, joueur):
            print("Le joueur humain a gagné !")
            break
        if egalite(damier):
            print("Match nul !")
            break




def morpion_moyen():
    choix_mode_de_jeu = int(input("Qui commence ? joueur (1), IA (2) ou aléatoire (3) ? : "))
    if choix_mode_de_jeu == 3 :
        choix_mode_de_jeu=random.choice([1,2])

    if choix_mode_de_jeu == 1 :
        code_joueur_moyen()

    if choix_mode_de_jeu == 2 :
        code_IA_moyen()



#initialisation des fonctions pour le niveau facile
def minimax_facile(damier, profondeur, alpha, beta, max_joueur):
    if combinaisons_gagnantes(damier, IA):
        return 1
    elif combinaisons_gagnantes(damier, joueur):
        return -1
    elif egalite(damier):
        return 0

    if max_joueur:
        max_eval = -math.inf
        for i in range(9):
            if damier[i] == VIDE:
                damier[i] = IA
                eval = minimax_facile(damier, profondeur+1, alpha, beta, False)
                damier[i] = VIDE
                max_eval=-1
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if damier[i] == VIDE:
                damier[i] = joueur
                eval = minimax_facile(damier, profondeur+1, alpha, beta, True)
                damier[i] = VIDE
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Fonction pour le coup de l'IA
def coup_IA_facile(damier):
    meilleure_eval = -math.inf
    meilleur_coup = None
    for i in range(9):
        if damier[i] == VIDE:
            damier[i] = IA
            eval = minimax_facile(damier, 0, -math.inf, math.inf, False)
            damier[i] = VIDE
            if eval > meilleure_eval:
                meilleure_eval = eval
                meilleur_coup = i
    damier[meilleur_coup] = IA

def code_joueur_facile():
        print("Le joueur humain est 'X'.")
        afficher_grille(damier)

        while True:
            # Tour du joueur humain
            coup_joueur = int(input("Choisissez une case de 1 à 9 : ")) - 1
            while damier[coup_joueur] != VIDE:
                coup_joueur = int(input("Case déjà prise, choisissez une case de 1 à 9 : ")) - 1
            damier[coup_joueur] = joueur
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, joueur):
                print("Le joueur humain a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break

            # Tour de l'IA
            print("Tour de l'IA...")
            coup_IA_facile(damier)
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, IA):
                print("L'IA a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break

def code_IA_facile():
        print("Le joueur humain est 'X'.")
        afficher_grille(damier)

        while True:
            # Tour de l'IA
            print("Tour de l'IA...")
            coup_IA_facile(damier)
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, IA):
                print("L'IA a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break

            # Tour du joueur humain
            coup_joueur = int(input("Choisissez une case de 1 à 9 : ")) - 1
            while damier[coup_joueur] != VIDE:
                coup_joueur = int(input("Case déjà prise, choisissez une case de 1 à 9 : ")) - 1
            damier[coup_joueur] = joueur
            afficher_grille(damier)

            # Vérification de la fin de la partie
            if combinaisons_gagnantes(damier, joueur):
                print("Le joueur humain a gagné !")
                break
            if egalite(damier):
                print("Match nul !")
                break



def morpion_facile():
    choix_mode_de_jeu = int(input("Qui commence ? joueur (1), IA (2) ou aléatoire (3) ? : "))
    if choix_mode_de_jeu == 3 :
        choix_mode_de_jeu=random.choice([1,2])

    if choix_mode_de_jeu == 1 :
        code_joueur_facile()

    if choix_mode_de_jeu == 2 :
        code_IA_facile()


#initialisation des fonctions pour le code joueur contre joueur
# Définition des symboles pour les joueurs
JOUEUR1 = 'O'
JOUEUR2 = 'X'
VIDE = ' '


def coup(damier,joueur):
    coup_joueur = int(input("Choisissez une case de 1 à 9 : ")) - 1
    while damier[coup_joueur] != VIDE:
        coup_joueur = int(input("Case déjà prise, choisissez une case de 1 à 9 : ")) - 1
    damier[coup_joueur] = joueur
    afficher_grille(damier)


# Fonction principale pour le jeu
def morpion_joueur():
    print("Le joueur 1 est 'O' et le joueur 2 est 'X'")
    a = int(input("Qui commence ? JOUEUR 1 (1), JOUEUR 2 (2) ou ALEATOIRE (3)? :"))
    if a==3:
        a = random.choice([1,2])

    if a==1 :
        print("Le joueur 1 commence. ")
        afficher_grille(damier)
        while True :
            coup(damier,JOUEUR1)
            if combinaisons_gagnantes(damier, JOUEUR1):
                print("Le joueur 1 a gagné")
                break
            if egalite(damier):
                print ("Egalité")
                break
            coup(damier,JOUEUR2)
            if combinaisons_gagnantes(damier, JOUEUR2):
                print("Le joueur 2 a gagné")
                break
        damier_final=afficher_grille(damier)
        return damier_final


    if a==2 :
        print("Le joueur 2 commence. ")
        afficher_grille(damier)
        while True :
            coup(damier,JOUEUR2)
            if combinaisons_gagnantes(damier, JOUEUR2):
                print("Le joueur 2 a gagné")
                break
            if egalite(damier)==True:
                print ("Egalité")
                break
            coup(damier,JOUEUR1)
            if combinaisons_gagnantes(damier, JOUEUR1):
                print("Le joueur 1 a gagné")
                break
        damier_final=afficher_grille(damier)
        return damier_final


def morpion_final():
    choix_mode_de_jeu = int(input("Choississez votre mode de jeu : joueur contre joueur (1), joueur contre IA (2) : "))
    if choix_mode_de_jeu == 1:
        morpion_joueur()
    if choix_mode_de_jeu == 2:
        choix_niveau = int(input("Choississez votre niveau de difficulté : FACILE (1), MOYEN (2), DIFFICILE (3) ou ALEATOIRE (4) : "))
        if choix_niveau == 4:
            choix_niveau = random.choice([1,2,3])
        if choix_niveau == 1:
            print("NIVEAU FACILE")
            morpion_facile()
        if choix_niveau == 2:
            print("NIVEAU MOYEN")
            morpion_moyen()
        if choix_niveau == 3:
            print("NIVEAU DIFFICILE")
            morpion_difficile()


morpion_final()
