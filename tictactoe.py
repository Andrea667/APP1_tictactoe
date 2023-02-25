import random
import math

# Définition des symboles pour les joueurs
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Définition du tableau de jeu
board = [EMPTY] * 9

# Fonction pour afficher le tableau de jeu
def print_board(board):
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")

# Fonction pour vérifier si un joueur a gagné
def check_win(board, player):
    for i in range(0, 9, 3):
        if (board[i] == board[i+1] == board[i+2] == player):
            return True
    for i in range(3):
        if (board[i] == board[i+3] == board[i+6] == player):
            return True
    if (board[0] == board[4] == board[8] == player):
        return True
    if (board[2] == board[4] == board[6] == player):
        return True
    return False

# Fonction pour vérifier si le tableau est plein
def check_tie(board):
    return all(square != EMPTY for square in board)

#Initialisation des fonctions pour le niveau difficile
# Fonction pour minimax avec élagage alpha-beta
def minimax_difficile(board, depth, alpha, beta, maximizing_player):
    if check_win(board, AI):
        return 1
    elif check_win(board, HUMAN):
        return -1
    elif check_tie(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval = minimax_difficile(board, depth+1, alpha, beta, False)
                board[i] = EMPTY
                max_eval = 1
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval = minimax_difficile(board, depth+1, alpha, beta, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
    
# Fonction pour le coup de l'IA
def ai_move_difficile(board):
    best_eval = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            eval = minimax_difficile(board, 0, -math.inf, math.inf, False)
            board[i] = EMPTY
            if eval > best_eval:
                best_eval = eval
                best_move = i
    board[best_move] = AI
    
def code_joueur_difficile():
        print("Le joueur humain est 'X'.")
        print_board(board)

        while True:
            # Tour du joueur humain
            human_move = int(input("Choisissez une case de 1 à 9 : ")) - 1
            if board[human_move] == EMPTY:
                board[human_move] = HUMAN
            else:
                print("Case déjà prise. Veuillez réessayer.")
                continue
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, HUMAN):
                print("Le joueur humain a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break

            # Tour de l'IA
            print("Tour de l'IA...")
            ai_move_difficile(board)
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, AI):
                print("L'IA a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break
            
def code_IA_difficile():
        print("Le joueur humain est 'X'.")
        print_board(board)

        while True:
            # Tour de l'IA
            print("Tour de l'IA...")
            ai_move_difficile(board)
            print_board(board)
            
            # Tour du joueur humain
            human_move = int(input("Choisissez une case de 1 à 9 : ")) - 1
            if board[human_move] == EMPTY:
                board[human_move] = HUMAN
            else:
                print("Case déjà prise. Veuillez réessayer.")
                continue
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, HUMAN):
                print("Le joueur humain a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break

            # Tour de l'IA
            print("Tour de l'IA...")
            ai_move_difficile(board)
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, AI):
                print("L'IA a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break
    
def morpion_difficile():
    choix_mode_de_jeu = int(input("Qui commence ? Joueur (1), IA (2) ou aléatoire (3) ? : "))
    if choix_mode_de_jeu == 1 : 
        code_joueur_difficile()
            
    if choix_mode_de_jeu == 2 :
        code_IA_difficile()
            
    if choix_mode_de_jeu == 3 :
        aleatoire=random.choice([1,2])
        if aleatoire == 1: 
            code_joueur_difficile()
        elif aleatoire == 2: 
            code_IA_difficile()

#initialisation des fonctions pour le niveau moyen
def minimax_moyen(board, depth, alpha, beta, maximizing_player):
    if check_win(board, AI):
        return 1
    elif check_win(board, HUMAN):
        return -1
    elif check_tie(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval = minimax_moyen(board, depth+1, alpha, beta, False)
                board[i] = EMPTY
                max_eval = 0
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval = minimax_moyen(board, depth+1, alpha, beta, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
    
# Fonction pour le coup de l'IA

def ai_move_moyen(board):
    best_eval = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            eval = minimax_moyen(board, 0, -math.inf, math.inf, False)
            board[i] = EMPTY
            if eval > best_eval:
                best_eval = eval
                best_move = i
    board[best_move] = AI
    return best_move

    
def code_joueur_moyen():
        print("Le joueur humain est 'X'.")
        print_board(board)

        while True:
            # Tour du joueur humain
            human_move = int(input("Choisissez une case de 1 à 9 : ")) - 1
            if board[human_move] == EMPTY:
                board[human_move] = HUMAN
            else:
                print("Case déjà prise. Veuillez réessayer.")
                continue
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, HUMAN):
                print("Le joueur humain a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break

            # Tour de l'IA
            print("Tour de l'IA...")
            ai_move_moyen(board)
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, AI):
                print("L'IA a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break
            
def code_IA_moyen():
    print("Le joueur humain est 'X'.")
    print_board(board)

    while True:
        # Tour de l'IA
        print("Tour de l'IA...")
        move = ai_move_moyen(board)
        board[move] = AI
        print_board(board)

        if check_win(board, AI):
            print("L'IA a gagné !")
            break
        if check_tie(board):
            print("Match nul !")
            break

        # Tour du joueur humain
        human_move = int(input("Choisissez une case de 1 à 9 : ")) - 1
        if board[human_move] == EMPTY:
            board[human_move] = HUMAN
        else:
            print("Case déjà prise. Veuillez réessayer.")
            continue
        print_board(board)

        if check_win(board, HUMAN):
            print("Le joueur humain a gagné !")
            break
        if check_tie(board):
            print("Match nul !")
            break


            
    
def morpion_moyen():
    choix_mode_de_jeu = int(input("Qui commence ? Joueur (1), IA (2) ou aléatoire (3) ? : "))
    if choix_mode_de_jeu == 1 : 
        code_joueur_moyen()
            
    if choix_mode_de_jeu == 2 :
        code_IA_moyen()
            
    if choix_mode_de_jeu == 3 :
        aleatoire=random.choice([1,2])
        if aleatoire == 1: 
            code_joueur_moyen()
        elif aleatoire == 2: 
            code_IA_moyen()

#initialisation des fonctions pour le niveau facile
def minimax_facile(board, depth, alpha, beta, maximizing_player):
    if check_win(board, AI):
        return 1
    elif check_win(board, HUMAN):
        return -1
    elif check_tie(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval = minimax_facile(board, depth+1, alpha, beta, False)
                board[i] = EMPTY
                max_eval = 0
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval = minimax_facile(board, depth+1, alpha, beta, True)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
    
# Fonction pour le coup de l'IA
def ai_move_facile(board):
    best_eval = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            eval = minimax_facile(board, 0, -math.inf, math.inf, False)
            board[i] = EMPTY
            if eval > best_eval:
                best_eval = eval
                best_move = i
    board[best_move] = AI
    
def code_joueur_facile():
        print("Le joueur humain est 'X'.")
        print_board(board)

        while True:
            # Tour du joueur humain
            human_move = int(input("Choisissez une case de 1 à 9 : ")) - 1
            if board[human_move] == EMPTY:
                board[human_move] = HUMAN
            else:
                print("Case déjà prise. Veuillez réessayer.")
                continue
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, HUMAN):
                print("Le joueur humain a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break

            # Tour de l'IA
            print("Tour de l'IA...")
            ai_move_facile(board)
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, AI):
                print("L'IA a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break
            
def code_IA_facile():
        print("Le joueur humain est 'X'.")
        print_board(board)

        while True:
            # Tour de l'IA
            print("Tour de l'IA...")
            ai_move_facile(board)
            print_board(board)
            
            # Tour du joueur humain
            human_move = int(input("Choisissez une case de 1 à 9 : ")) - 1
            if board[human_move] == EMPTY:
                board[human_move] = HUMAN
            else:
                print("Case déjà prise. Veuillez réessayer.")
                continue
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, HUMAN):
                print("Le joueur humain a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break

            # Tour de l'IA
            print("Tour de l'IA...")
            ai_move_facile(board)
            print_board(board)

            # Vérification de la fin de la partie
            if check_win(board, AI):
                print("L'IA a gagné !")
                break
            if check_tie(board):
                print("Match nul !")
                break
    
def morpion_facile():
    choix_mode_de_jeu = int(input("Qui commence ? Joueur (1), IA (2) ou aléatoire (3) ? : "))
    if choix_mode_de_jeu == 1 : 
        code_joueur_facile()
            
    if choix_mode_de_jeu == 2 :
        code_IA_facile()
            
    if choix_mode_de_jeu == 3 :
        aleatoire=random.choice([1,2])
        if aleatoire == 1: 
            code_joueur_facile()
        elif aleatoire == 2: 
            code_IA_facile()
            
#initialisation des fonctions pour le code joueur contre joueur        
# Définition des symboles pour les joueurs
JOUEUR1 = 'O'
JOUEUR2 = 'X'
VIDE = ' '


def move(board,player):
    player_move = int(input("Choisissez une case de 1 à 9 : ")) - 1
    while board[player_move] != VIDE:
        player_move = int(input("Case déjà prise, choisissez une case de 1 à 9 : ")) - 1
    board[player_move] = player
    print_board(board)
    

# Fonction principale pour le jeu
def morpion_joueur():
    print("Le joueur 1 est 'O' et le joueur 2 est 'X'")
    a = int(input("Qui commence ? JOUEUR 1 (1), JOUEUR 2 (2) ou ALEATOIRE (3)? :"))
    if a==3:
        a = random.choice([1,2])
        
    if a==1 :
        print("Le joueur 1 commence. ")
        print_board(board)
        while True :
            move(board,JOUEUR1)
            if check_win(board, JOUEUR1)==True:
                print("Le joueur 1 a gagné")
                break
            if check_tie(board)==True:
                print ("Egalité")
                break
            move(board,JOUEUR2)
            if check_win(board, JOUEUR2)==True:
                print("Le joueur 2 a gagné")
                break
        damier_final=print_board(board)
        return damier_final
    
    
    if a==2 :
        print("Le joueur 2 commence. ")
        print_board(board)
        while True :
            move(board,JOUEUR2)
            if check_win(board, JOUEUR2)==True:
                print("Le joueur 2 a gagné")
                break
            if check_tie(board)==True:
                print ("Egalité")
                break
            move(board,JOUEUR1)
            if check_win(board, JOUEUR1)==True:
                print("Le joueur 1 a gagné")
                break
        damier_final=print_board(board)
        return damier_final        


def morpion_final(): 
    choix_mode_de_jeu = int(input("Choississez votre mode de jeu : Joueur contre joueur (1), Joueur contre IA (2) ou IA contre IA (3) : "))
    if choix_mode_de_jeu == 1: 
        morpion_joueur()
    if choix_mode_de_jeu == 2: 
        choix_niveau = int(input("Choississez votre niveau de difficulté : FACILE (1), MOYEN (2), DIFFICILE (3) ou ALEATOIRE (4) : "))
        if choix_niveau == 4: 
            aleatoire = random.choice([1,2,3])
            if aleatoire == 1:
                print("Niveau facile : ")
                morpion_facile()
            if aleatoire == 2: 
                print("Niveau moyen : ")
                morpion_moyen()
            if aleatoire == 3:
                print("Niveau difficile : ")
                morpion_difficile()
        if choix_niveau == 1: 
            morpion_facile()
        if choix_niveau == 2: 
            morpion_moyen()
        if choix_niveau == 3: 
            morpion_difficile()
    if choix_mode_de_jeu == 3: 
        print("Pas encore fait")

morpion_final()
    