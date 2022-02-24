##print('On commence')

##print('C est mon premier cours de programmation')

##monNom = "Marie-Christine Desmarais-Bilodeau" #variable contenant mon nom
##print(monNom)

##nomDeFamille = "Bélanger" #variable contenant mon nom de famille
##print(nomDeFamille)

##Programme pour demande le nom de l'utilisateur
##nom = input("Quel est votre nom?")
##print("Allo", nom)

##Programme pour demander la couleur préférée de l'utilisateur
##couleur = input("Quelle est votre couleur préférée?")
##print("Votre couleur préférée est le", couleur)

##monNombre = 200
##tonNombre = input("Entre un nombre entier: \n")
##tonNombre = int(tonNombre)
##print("Si on additionne les deux nombres, ça fait:", monNombre + tonNombre)

##nouvelAge = 20
##age = input("Entre ton âge: \n")
##age = int(age)
##print("Dans 20 ans, tu auras", age + nouvelAge, "ans")

##initialiser une liste de nombres
##listeDeNombres = [9, 12, 5, 43, 1]
##print(listeDeNombres)

##répéter plusieurs fois le même processus à l'aide dune boucle
##for x in range(20):
##    print("La boucle est rendue au numéro", x)

##for nom in ["Léa", "Mireille", "Marianne", "Sophie"]:
##    print("Bonjour", nom)

##laListe = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
##print(laListe)
##laListe.append("dimanche")
##print(laListe)

#Addition des chaînes de caractères pour former un message.
##debutPrenom = input("Quelles sont les deux premières lettres de votre prénom? \n")
##finPrenom = input("Quelles sont les autres lettres? \n")
##debutNomFamille = input("Quelle est la première syllabe de votre nom de famille? \n")
##finNomFamille = input("Quelles sont les autres syllabes? \n")
##message = "Bonjour " + debutPrenom + finPrenom + " " + debutNomFamille + finNomFamille + "!"
##print(message)

##phrase = "Les logiciels que j'utilise sont: "
##for logiciel in ["Word", "PowerPoint", "Excel", "Photoshop"]:
##    phrase = phrase + " " + logiciel
##print(phrase + ".")

##nom = "Madeline"
##age = 25
##message = "Je m'apelle " + nom + " et j'ai " + str(age) + " ans."
##print(message)

##monNom = "Léo"
##reponse = input("Est-ce que tu veux savoir comment je m'appelle? (oui ou non) \n")
##if reponse == "oui" :
##    print("Je m'appelle", monNom)

##for x in range(20):
##    print(x, x%5)


##for x in range(20):
##    if x%2 == 0:
##        print (x, "pair")
##    else: 
##        print (x, "impair")

##nombre = input("Jusqu'à quel nombre désirez-vous aller? \n")
##nombre = int(nombre)
##for x in range(nombre):
##    if x%3 == 0:
##        print(x)

##nombre = input("Veuillez entrer un nombre \n")
##nombre = int(nombre)
##if nombre > 100:
##    print ("Le nombre ", nombre, " est supérieur à 100")
##else:
##    print ("Le nombre ", nombre, " est inférieur à 100")

###Tracer une ligne avec du code
##from turtle import *
##forward(500)
##
##from turtle import *
##for x in range(5):
##    forward(10)
##    dot(40)
##hideturtles()

##from turtle import*
##for x in range(20):
##    home()
##    setheading(x * 18)
##    forward (100)
##    dot(10)
##hideturtle()
##
##from turtle import *
##for x in range(10):
##    home()
##    setheading(x * 36)
##    forward(50)
##    dot(20, "red")
##hideturtle()

##from turtle import *
##for x in range(20):
##    home()
##    setheading(x * 18)
##    if x%2 == 0:
##        forward(40)
##        dot(20, "lavender blush")
##    else:
##        forward(30)
##        dot(10, "light pink")
##hideturtle()
##
##def pairOuImpair():
##    nbr = input("Entrez un nombre entier. \n")
##    nbr = int(nbr)
##    if nbr%2 == 0:
##        print(nbr, "est pair")
##    else:
##        print(nbr, "est impair")
##pairOuImpair()

##def salutations():
##    prenom = input("Entrez votre prénom. \n")
##    nomFamille = input("Entrez votre nom de famille. \n")
##    print("Bonjour, " + prenom + " " + nomFamille + "!")
##
##salutations()

###Génerer une fenêtre
##from tkinter import *
##maFenetre = Tk()
##maFenetre.geometry("800x350")
##maFenetre.title("Module 6")
##
##logo=PhotoImage(file = "logo.png")
##logoCompagnie = Label(maFenetre, image = logo)
##logoCompagnie.grid(row = 1, column = 1)
##
##texteRequete = Label(maFenetre, text = "Entrez le nom de la compagnie")
##texteRequete.grid(row = 1, column = 2)
##texteSousLogo = Label(maFenetre, text = "Nom temporaire", font=("Arial",16))
##texteSousLogo.grid(row = 2, column = 1)
##
##nomCompagnie = Entry(maFenetre)
##nomCompagnie.grid(row = 1, column = 3)
##
##leTypeChoisi =StringVar(maFenetre)
##leTypeChoisi.set("Choisir un type d'entreprise")
##menuTypes = OptionMenu(maFenetre,leTypeChoisi, "Finances", "Électroménagers", "Publicité", "Immobilier")
##menuTypes.grid(row = 2, column = 2)
##
##def actionSiClic():
##    texteSousLogo.configure(text = nomCompagnie.get() + "\n" + leTypeChoisi.get())
##    nomCompagnie.delete(0, END)
##
##monBouton = Button(maFenetre, text = "Enregistrer", command = actionSiClic)
##monBouton.grid(row = 3, column = 2)



#Développer une petite application

from tkinter import *
maFenetre = Tk()
maFenetre.geometry("1200x600")
maFenetre.title("Projet d'intégration")

logo=PhotoImage(file = "logo.png")
logoCompagnie = Label(maFenetre, image = logo)
logoCompagnie.grid(row = 1, column = 1)

texteFiche = Label(maFenetre, text = "Fiche d'inscription", font=("Arial", 12))
texteFiche.grid(row = 1, column = 2)
texteRapport = Label(maFenetre, text = " ")
texteRapport.grid (row = 1, column = 5)

#Rangée 2 de l'interface

texteCompagnie = Label(maFenetre, text = "TOPKAPI inc.", font=("Arial", 15))
texteCompagnie.grid (row = 2, column = 1)

#Rangées 3 ,4 , 5 et 6 de l'interface

textePrenom = Label(maFenetre, text = "Prénom")
textePrenom.grid(row = 3, column = 2)
Prenom = Entry(maFenetre)
Prenom.grid(row = 3, column = 3)

texteNomFamille = Label(maFenetre, text = "Nom de famille")
texteNomFamille.grid(row = 4, column = 2)
NomFamille = Entry(maFenetre)
NomFamille.grid(row = 4, column = 3)

texteSexe = Label(maFenetre, text = "Sexe (F ou M)")
texteSexe.grid(row = 5, column = 2)
Sexe = Entry(maFenetre)
Sexe.grid(row = 5, column = 3)

texteNaissance = Label(maFenetre, text = "Année de naissance")
texteNaissance.grid(row = 6, column = 2)
Naissance = Entry(maFenetre)
Naissance.grid(row = 6, column = 3)

#Rangée 7 de l'interface

texteEmploi = Label (maFenetre, text = "Titre de l'emploi")
texteEmploi.grid (row = 7, column = 2)
Emploi =StringVar(maFenetre)
Emploi.set("Sélectionner")
menuEmploi = OptionMenu(maFenetre,Emploi, "designer graphique", "programmeur python", "programmeur C++", "developpeur web", "rédacteur","artiste 3D")
menuEmploi.grid(row = 7, column = 3)

#Rangée 8 de l'interface


texteLogiciel = Label (maFenetre, text = "Logiciels")
texteLogiciel.grid(row = 8, column = 2)
Logiciel = Entry(maFenetre)
Logiciel.grid(row = 8, column = 3)
listeLogiciels = []

def actionAjoutLogiciel():
    nouveauLogiciel = Logiciel.get()
    listeLogiciels.append(nouveauLogiciel)
    Logiciel.delete(0, END)

monBouton = Button(maFenetre, text = "Ajouter le logiciel", command = actionAjoutLogiciel)
monBouton.grid(row = 8, column = 4)

#Rangée 9 de l'interface

def actionSoummettre():

#1
    prenomEmploye= Prenom.get()
    nomFamilleEmploye = NomFamille.get()
    sexeEmploye = Sexe.get()

#2

    anneeEmploye = Naissance.get()
    anneeEmploye = int(anneeEmploye)
    ageEmploye = 2022 - anneeEmploye

#3

    emploiEmploye = Emploi.get()

#4
    #ligne 1

    if sexeEmploye == "F":
        ligne1 = "La nouvelle employée"
    else:
        ligne1 = "Le nouvel employé"
    ligne1 = ligne1 + " s'appelle " + prenomEmploye + " " + nomFamilleEmploye + ". \n"

    #ligne 2

    ageEmploye = str(ageEmploye)
    ligne2= "À la fin de l'année 2022, cette personne aura " + ageEmploye + " ans. \n"

    #ligne 3

    ligne3 = "Son titre au sein de l'entreprise est: " + emploiEmploye + ". \n"

    #ligne 4

    ligne4 = "Elle utilise les logiciels suivants :"
    
    for Logiciel in listeLogiciels:
        ligne4 = ligne4 + " " + Logiciel
    ligne4 = ligne4 + "."
    texteRapport.configure(text = ligne1 + ligne2 + ligne3 + ligne4)

BoutonSoumettre = Button(maFenetre, text = "Soumettre un rapport", command = actionSoummettre)
BoutonSoumettre.grid(row = 9, column = 3)




