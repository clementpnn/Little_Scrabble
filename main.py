from random import randint
from random import shuffle
from time import sleep
from ascii import *
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
p = 0
q = "quit"
bq = q.capitalize()

for i in range(1, 4):
    new_liste = []
    mot_v = []
    mot_f = []
    cq = 0
    fichier = open("word_list.txt", "rt")

    liste = [x.rstrip("\n") for x in fichier]
    mot1 = liste[randint(0, len(liste) - 1)]
    mot2 = liste[randint(0, len(liste) - 1)]
    mot3 = liste[randint(0, len(liste) - 1)]

    while mot1 == mot2 or mot1 == mot3 or mot2 == mot3 :
        mot1 = liste[randint(0, len(liste) - 1)]
        mot2 = liste[randint(0, len(liste) - 1)]
        mot3 = liste[randint(0, len(liste) - 1)]

    liste_mots = mot1 + mot2 + mot3
    l = liste_mots.replace(" ", "")



    for element in l:
        if element not in new_liste:
            new_liste.append(element)

    shuffle(new_liste)

    while cq < 3:
        clearConsole()
        ban()

        print("\nManche(s) :",i,"/ 3")
        print("Point(s) :",p)
        print("\nVous disposez de", len(new_liste), "lettres avec lesquelles vous devez faire 3 mots")
        print("\nVoici vos lettres : ","   ".join(new_liste))
        print("\n✅ "," ".join(mot_v))
        print("\n❌ "," ".join(mot_f))
        print(mot1,mot2,mot3)

        choix = str(input("\nEntrez un mot ou quit pour passer à la manche suivante : "))
        mc = choix.capitalize()
        mc1 = mot1.capitalize()
        mc2 = mot2.capitalize()
        mc3 = mot3.capitalize()
        if choix in mot_f or choix in mot_v:
            print("\nVous avez déjà écrit ce mot")  
        elif choix == mot1 or mc == mc1 or choix == mot2 or mc == mc2 or choix == mot3 or mc == mc3:
            mot_v.append(choix)
            cq += 1
            p += 1
        elif choix == q or mc == bq :
            sleep(1)
            print("\nVous avez décidé de passer cette manche")
            cq = 4
        else :
            mot_f.append(choix)

    sleep(2)
    if i < 3 :
        clearConsole()
        suiv()
        sleep(4)
clearConsole()
fin()
print("\n")
if p == 0 :
    p_0()
elif p == 1 :
    p_1()
elif p == 2 :
    p_2()
elif p == 3 :
    p_3()
elif p == 4 :
    p_4()
elif p == 5 :
    p_5()
elif p == 6 :
    p_6()
elif p == 7 :
    p_7()
elif p == 8 :
    p_8()
else :
    p_9()