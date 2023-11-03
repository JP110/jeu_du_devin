
from random import randint

def jeu_devin_Q1():
    #Initialiser les limites 
    nombre_min = 1
    nombre_max = 999

    #Choisir un nombre à trouver
    reponse = randint (nombre_min,nombre_max)
    print ("J'ai choisi un nombre compris entre {} et {}".format(nombre_min, nombre_max))

    #Deviner le nombre
    nb_coups = 0
    a_trouve = False
    while (not a_trouve):
        #Demander une proposition à l'utlisateur
        proposition = int(input("Proposition {} : ".format(nb_coups + 1)))
        
        #Evaluer la proposition de l'utilisateur
        if (proposition == reponse):
            print("Trouvé ! ")
            a_trouve = True 
        elif (proposition > reponse):
            print("Trop Grand ! ")
        else:
            print("Trop petit ! ")
        nb_coups += 1

    #Afficher le bilan
    print ("Bravo ! Vous avez trouvé en {} essais".format(nb_coups))
    print()

def jeu_devin_Q2():
    #Initialiser les limites 
    nombre_min = 1
    nombre_max = 999
    
    #Demander à l'utilistauer s'il a choisi un nombre
    reponse = 'n'
    while (reponse != 'o'):
        reponse = input ("Avez-vous choisi un nombre compris entre {} et {} (o/n) ? ".format(nombre_min, nombre_max))
        if (reponse != ('o')):
            print("J'attends...")

    #Deviner le nombre
    nb_coups = 0
    a_trouve = False
    while (not a_trouve):
        #Réaliser une proposition
        proposition = (nombre_min + nombre_max) // 2
        print ("Proposition {} : {} ".format(nb_coups + 1,proposition))

        #Evaluer la proposition de  la machine
            #Demander l'évaluation' à l'utlisateur
        evaluation = input ("Trop (g)rand, trop (p)etit ou (t)rouvé ? ")
        evaluation = evaluation.lower()

            #Prendre en compte la reponse de l'utilisateur 
        if (evaluation == 't'): #trouvé
            nb_coups += 1
            a_trouve = True 
        elif (evaluation =='g'): #trop grand
            nombre_max = proposition - 1 
            nb_coups += 1
        elif (evaluation =='p'): #trop petit
            nombre_min = proposition + 1
            nb_coups += 1
        else: #réponse non valide
            print("Je n'ai pas compris la réponse. Merci de répondre :")
            print("g si ma proposition est trop grande")
            print("p si ma proposition est trop petite")
            print("t si j'ai trouvé le nombre")

    #Afficher le résultat
    print ("J'ai trouvé en en {} essais".format(nb_coups))
    print()

def main():

    jouer = True
    while (jouer):
    #Affciher le menu
        print("1- L'ordinateur choisit un nombre et vous le devinez")
        print("2- Vous choisissez un nombre et l'ordinateur le devine")
        print("0- Quitter le programme")

    #Demander le choix du mode à l’utilisateur
        choix_mode = input ("Votre choix : ")
        print()
    #Lancer le mode de jeu  
        if (choix_mode == "1"):
            jeu_devin_Q1()
        elif (choix_mode == "2"):
            jeu_devin_Q2()
        elif (choix_mode == "0"):
            print("Au revoir...")
            jouer = False


if __name__ == '__main__':
    main()
