import os
import platform

# Nombre de grille
NUMBER_OF_GRIDS = 6

def create_grids ():
    """
        Fonction qui permet de crée la grille de jeu.
    """

    # Renvoie la grille de jeu sous format de list dans des lists
    return [ ["  "]*NUMBER_OF_GRIDS for _ in range(NUMBER_OF_GRIDS) ]

# Status du jeu
game_over = False
# Nombre de coup (ou tour) joué de la part du joueur rouge
red_turn = 0
# Nombre de coup (ou tour) joué de la part du joueur bleu
blue_turn = 0
# Grille de jeu
grids = create_grids()

# Choix des pseudonymes de la part des joueurs
player_one_username = input('\n\033[41m Joueur 1 \033[0m - Choisissez votre pseudonyme: \n')
player_two_username = input('\n\033[46m Joueur 2 \033[0m - Choisissez votre pseudonyme: \n')

def clear ():

    """ 
        Exécute la command de clear, permet en outre de supprimer tout le contenu précédent pour avoir une
        claireté de jeu, code source de la fonction: https://www.tutorialspoint.com/how-to-clear-screen-in-python
    """

    # Stocker en mémoire la command approprié à l'OS de la machine.
    clear_command = ""

    # Si la l'OS est Windows alors la command de clear serra 'cls'.
    if platform.system().lower() == "windows" :
        clear_command = 'cls'
    # Sinon la commande de clear sera 'clear' pour tout autre système d'exploitation.
    else:
        clear_command = 'clear'

    os.system(clear_command)

def show_grids (grids):
    """ 
        Fonction qui affiche graphiquement la grille en bouclan dans chaque élèments. 
    """

    # On parcour la grille par index de grille
    for row in range(len(grids)):
        
        # Affiche graphiquement la grille 
        print(f"{grids[row]} | R{row}")

    # Affiche graphiquement l'index de la grille de façon horizontal
    horizontal_column_indexs = [ f"C{i}" for i in range(NUMBER_OF_GRIDS) ]
    print(horizontal_column_indexs)

def check_vertical_strike(grids, pawn):
    """
        Fonction qui permet de vérifier les pions en vertical
    """
    
    for row in range(len(grids)): # Parcoure de façon inversé les grilles par 'row' pour obtenirs le bon ordre de calcule
        for column in range(len(grids[row])): # Parcoure les grilles de coordonnées 'column' pour obtenir la coordonée 'row'
            if row + 1 < len(grids) and row + 2 < len(grids) and row + 3 < len(grids): # On vérifie si on ne dépasse pas le nombre de rangée existante
                if grids[row][column] == pawn and grids[row + 1][column] == pawn and grids[row + 2][column] == pawn and grids[row + 3][column] == pawn:
                    return True

def check_horizontal_strike(grids, pawn):
    """
        Fonction qui permet de vérifier les pions en horizontal
    """

    for row in range(len(grids)): # Parcoure de façon inversé les grilles par 'row' pour obtenirs le bon ordre de calcule
        for column in range(len(grids[row])): # Parcoure les grilles de coordonnées 'column' pour obtenir la coordonée 'row'
            if column + 1 < len(grids[row]) and column + 2 < len(grids[row]): # On vérifie si on ne dépasse pas le nombre de collones existante
                if grids[row][column] == pawn and grids[row][column + 1] == pawn and grids[row][column + 2] == pawn and grids[row][column + 3] == pawn:
                    return True

def check_left_diagonal_strike(grids, pawn):
    """
        Fonction qui permet de vérifier les pions en diagonale (côté gauche)
    """
    
    # Parcoure de façon inversé les grilles par 'row' pour obtenirs le bon ordre de calcule
    for row in reversed(range(len(grids))):
        # Parcoure les grilles de coordonnées 'column' pour obtenir la coordonée 'row'
        for column in reversed(range(len(grids[row]))):
            if row - 1 < NUMBER_OF_GRIDS and grids[row][column] == pawn and grids[row - 1][column - 1] == pawn and grids[row - 2][column - 2] == pawn and grids[row - 3][column - 3] == pawn:
                # Alors on renvoie True, annonçant la victoire d'un des joueurs
                return True

def check_right_diagonal_strike(grids, pawn):
    """
        Fonction qui permet de vérifier les pions en diagonale (côté droit)
    """

    for row in reversed(range(len(grids))): # Parcoure de façon inversé les grilles par 'row' pour obtenirs le bon ordre de calcule
        for column in range(len(grids[row])): # Parcoure les grilles de coordonnées 'column' pour obtenir la coordonée 'row'
            if grids[row][column] == pawn and grids[row - 1][column - 1] == pawn and grids[row - 2][column - 2] == pawn and grids[row - 3][column - 3] == pawn:
                # Alors on renvoie True, annonçant la victoire d'un des joueurs
                return True

def drop_pawn (grids, grid, symbol):
    """
        Fonction qui ajoute un pion dans une grille selectioner, prend en compte la grille et le symbol du joueur 
        return True si on a pu placer le pion.
    """

    # Supprime le contenu précédent
    clear()

    # Parcoure les grilles par le nombre de grille données en 'i'
    for i in range(NUMBER_OF_GRIDS - 1, -1, -1):

        # Si la grille d'index i + 1 est d'un tel grid est vide, alors on ajoute un symbol
        if grids[i][grid] == "  ":
            # On stop la boucle en renvoyant True
            grids[i][grid] = symbol
            return True
    # On stop la boucle en renvoyant False
    return False

def check_instance_of_grid (grids, grid, player, color, player_color):
    """ 
        Fonction qui vérifie si un nombre est valide et prend en paramètre le joueur actuel 
    """

    # Vérifie si le nombre de grille est un entier compris entre 0 et 5
    if isinstance(grid, int) and grid >= 0 and grid <= 5:
    
        # Ajoute un pion si il est possible de le placer
        if drop_pawn(grids, grid, color) == False:
            # Affiche la grille
            show_grids(grids)
            # Averti le joueur du nombre de grille maximal atteint
            print(f"{player_color} {player} \033[0m - \033[31mVous ne pouvez pas allez plus loin, vous avez atteint le nombre de grille maximal, votre tour est passé !\033[0m")
        # Sinon on montre que la grille
        else:
            show_grids(grids)
    # Sinon on averti le joueur et son tour passe au suivant
    else:
        print(f"{player_color} {player} \033[0m - \033[31mVeuillez mettre un nombre valide, votre tour est passé !\033[0m")

# On nettoie le screen
clear()
# Affiche la grille
show_grids(grids)

# Boucle à l'infini le jeux
while not game_over:  

    # Essai du code
    try:
        if not game_over:
            # Tour du premier joueur
            grid = input(f"\n\033[41m {player_one_username} \033[0m - Choisissez votre colonne (C): \n")
            
            # On vérifie l'instance de la grille du joueur
            check_instance_of_grid(grids, int(grid), player_one_username, '🔴', '\033[41m')
            
            # On incrémente de 1 le nombre de coup joué
            red_turn += 1
            
            # On vérifie toute les possibilités de victoire du joueur 1 
            if check_left_diagonal_strike(grids, '🔴') or check_right_diagonal_strike(grids, '🔴') or check_horizontal_strike(grids, '🔴') or  check_vertical_strike(grids, '🔴'):
                print(f"\n\033[41m {player_one_username} \033[0m - PUISSANCE 4 ! Vous avez gagné la partie en {red_turn} coup !\n")
                game_over = True

    # Renvoie une erreur en cas de problème
    except ValueError:
        clear()
        show_grids(grids)
        print(f"\n\033[41m\033[37m {player_one_username} \033[0m - \033[31mUn erreur c'est produite durant l'execution, votre tour est passé !\033[0m")

    # Essai du code
    try:
        if not game_over:
            # Tour du deuxième joueur
            grid = input(f"\n\033[46m {player_two_username} \033[0m - Choisissez votre colonne (C): \n")

            # On vérifie l'instance de la grille du joueur
            check_instance_of_grid(grids, int(grid), player_two_username, '🔵', '\033[46m')

            # On incrémente de 1 le nombre de coup joué
            blue_turn += 1

            # On vérifie toute les possibilités de victoire pour le joueur 2
            if check_left_diagonal_strike(grids, '🔵') or check_right_diagonal_strike(grids, '🔵') or check_horizontal_strike(grids, '🔵') or check_vertical_strike(grids, '🔵'):
                print(f"\n\033[46m {player_two_username} \033[0m - PUISSANCE 4 ! Vous avez gagné la partie en {blue_turn} coup !\n")
                game_over = True

    # Renvoie une erreur en cas de problème
    except ValueError:
        clear()
        show_grids(grids)
        print(f"\n\033[46m\033[37m {player_two_username} \033[0m - \033[31mUn erreur c'est produite durant l'execution, votre tour est passé !\033[0m")
