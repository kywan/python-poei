###############################################################################
#        -' | \                                                               #
#       /7     \                                    GRASSIN Pierre            #
#      /        `-_                                 pierrr.312@gmail.com      #
#      \-'_        `-.____________                                            #
#       -- \                 /    `.                Creation : 05/06/2018     #
#          /                 \      \               Modification : 05/06/2018 #
#  _______/    /_       ______\      |__________-   Version : 5               #
# (,__________/  `-.___(,_____________----------_)                            #
###############################################################################



# on importe la librairie liée à la fonction random et emoji
import random, emoji


# difficulty va demander a l'utilisateur de choisir un niveau
# et va retrourner la valeur max du niveau
# tant que l'utilisateur ne rentre pas un niveau nous alons lui redemander de choisir
def diffiulty():
    print("Choisisez votre difficulté :")
    print("1 : entre 1 et 100")
    print("2 : entre 1 et 1000")
    print("3 : entre 1 et 10000")
    print("4 : entre 1 et 100000")
    level = input("===============")
    print(level)
    if level == '1':
        return 100
    elif level == '2':
        return 1000
    elif level == '3':
        return 10000
    elif level == '4':
        return 100000
    else:
        return diffiulty()


# generation va génerer alléatoirement un nombre entre 1 et le maximum
# param = maximum de la génération (int)
def generation(param):
    return random.randrange(1, param)


# turnmax demande à l'utilisateur de choisir un nombre de tour maximum
# si l'utilisateur rentre un nombre négatif on redemandera à l'utilisateur de choisir
def turnmax():
    val = int(input("En combien de tour maximum pense tu réussir ? (0 pour jouer à l'infinie)"))
    if val >= 0:
        return val
    else:
        turnmax()


# aideAsk demande à l'utilisateur si il veux de l'aide
# ici on ne redemande pas jusqu'a validation, si c'est 1 mode simple et le reste sera mode normal
def aideAsk():
    return int(input("veux tu jouer avec les aides ? (1 : easy mode | 2 : normal mode)"))


# programe principal
# nbr = nombre rentré par l'user
# turn = compte le nombre de tentative
# aide = affiche ou non l'aide
# min = valeur minimum apres tentative
# max = valeur maximum apres tentative, s'initialise à la valeur de difficulty
# rand = nombre à trouver
# maxTurn = nombre de tentative max autorisé
def mainprog():
    nbr = 0
    turn = 0
    aide = aideAsk()
    min = 0
    max = diffiulty()
    rand = generation(max)
    maxTurn = turnmax()

    while nbr != rand:
        print("tu en est à " + str(turn) + " tentative(s)" + emoji.emojize(":heart:"*(maxTurn-turn), use_aliases=True))
        if turn >= maxTurn and maxTurn != 0:
            return print("Perdu " + emoji.emojize(":skull:", use_aliases=True) +"! tu as eu " + str(turn) + " tentative et tu n'a toujours pas trouvé le nombre :" + str(rand))
        if aide == 1:
            print("Le nombre est entre " + str(min) + " et " + str(max))
        nbr = int(input("Choisis un nombre :"))
        if nbr < rand:
            print("c'est plus")
            if nbr > min:
                min = nbr
        elif nbr > rand:
            print("c'est moins")
            if nbr < max:
                max = nbr
        turn += 1


# lancement du jeux
mainprog()

# ici on demande à l'user si il veux rejouer
while int(input("veux tu rejouer (1:oui | 2:non)")) == 1:
    mainprog()
