import mysql.connector
from math import *
from haversine import haversine, Unit
import time

###DOCTEST###
"""ville1 = (45.74642690476188,5.60249178571429)
ville2 = (46.00144716049382,5.36654228395062)
print(haversine(ville1,ville2))"""


BDD = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "code postaux"
)

curseur_test = BDD.cursor



#################UI##################
print("1 - Cherchez le code postal grâce à la saisie du nom de la ville (orthographe exacte).")
print("2 - Cherchez le nom de la ville grâce à la saisie du code postal (orthographe exacte).")
print("3 - Passez en paramètre un nom de ville et un rayon (en km) pour trouver les villes qui se situent aux alentours.")

choice = input("Quel est vôtre choix ? ->")
#l'utilisateur choisis de chercher un code postal grâce à un nom de ville
if choice == '1' :
    param = input("Saisissez un nom de ville :")
    curseur1 = BDD.cursor()
    #curseur.execute("SELECT zip_code FROM cities WHERE name = '"+recherche_user+"'")
    curseur1.execute("SELECT zip_code FROM cities WHERE name ='"+param+"'")
    res =curseur1.fetchone()
    print(res[0])
#l'utilisateur choisis de chercher une ville grâce au code postal
elif choice == '2' :
    param = input("Saisissez un code postal : ")
    curseur2 = BDD.cursor()
    curseur2.execute("SELECT name FROM cities WHERE zip_code = '"+param+"'")
    res2 =curseur2.fetchone()
    print(res2[0])


elif choice == '3':
    """alentours = []
    curseur = BDD.cursor()
    print("Veuillez choisir une ville ")
    param_ville = str(input())
    curseur.execute("SELECT zip_code FROM cities WHERE name ='"+param_ville+"'")
    #ville centrale
    ville = curseur.fetchone()
    print(ville[0])
    print("Veuillez choisir un rayon (en km)")
    #choix du rayon
    rayon = input()
    curseurLatCentre = BDD.cursor()

    curseurLatCentre.execute("SELECT gps_lat FROM cities WHERE zip_code ='"+ville[0]+"'")
    latitudeCentre = curseurLatCentre.fetchone()
    curseur.execute("SELECT gps_lng FROM cities WHERE zip_code ='"+ville[0]+"'")
    longitudeCentre = curseur.fetchone()
    villeCentre = (latitudeCentre[0],longitudeCentre[0])#premier repère établit
    print(villeCentre)

    curseur.execute("SELECT MAX(id) FROM cities")
    max_index = curseur.fetchone()
    cpt = 1
    while cpt != 100:
        curseur.execute("SELECT gps_lat FROM cities WHERE id = '" + str(cpt)+"'")
        latVille2 = curseur.fetchone()

        print(latVille2)

        curseur.execute("SELECT gps_lat FROM cities WHERE id = '" + str(cpt)+"'")
        lngVille2 = curseur.fetchone()

        print(lngVille2)
        CoorVille2 = (latVille2[0],lngVille2[0])
        distance = haversine(villeCentre,CoorVille2)
        if distance <= float(rayon):
            curseur.execute("SELECT name FROM cities WHERE id = "+str(cpt))
            nom_ajout = curseur.fetchone()
            alentours.append[nom_ajout[0]]
        cpt+=1
    print(alentours)"""

    #essai 2
    cpt_villes_alentours = 0
    villeCentraleUser = input("Veuillez choisir une ville ->")
    rayonCentralUser = input("Choisissez le rayon autour de cette ville ->")
    ###définition du tuple de la ville qui est le point central###
    curseurCentralLat = BDD.cursor()
    curseurCentralLat.execute("SELECT gps_lat FROM cities WHERE name = '" + villeCentraleUser + "'")
    latCentrale = curseurCentralLat.fetchone()
    latCentrale = latCentrale[0] #Latitude de la ville centrale
    #print(latCentrale)

    curseurCentralLng = BDD.cursor()
    curseurCentralLng.execute("SELECT gps_lng FROM cities WHERE gps_lat = '" + str(latCentrale) +"'")
    lngCentrale = curseurCentralLng.fetchone()
    lngCentrale = lngCentrale[0] #Longitude de la ville centrale
    #print(lngCentrale)

    CoordVilleCentrale = (latCentrale,lngCentrale) #Latitude et longitude combinées sous forme de tuple

    ##################################

    nb_repet_actuelle = 1
    alentours = []

    curseurMax = BDD.cursor()
    curseurMax.execute("SELECT MAX(id) FROM cities")
    nb_repet_max = curseurMax.fetchone()
    nb_repet_max = nb_repet_max[0] #Nombre de villes au total
    #print(nb_repet_max)

    curseurNomAlentours = BDD.cursor()
    curseurLatPos2 = BDD.cursor()
    curseurLngPos2 = BDD.cursor()
    while nb_repet_actuelle != nb_repet_max:
        curseurLatPos2.execute("SELECT gps_lat FROM cities WHERE id = '" + str(nb_repet_actuelle) + "'") #récupère la latitude de la pos2 actuelle
        LatPos2_actuelle = curseurLatPos2.fetchone() #assignation de la latitude à la variable
        LatPos2_actuelle = LatPos2_actuelle[0]

        curseurLngPos2.execute("SELECT gps_lng FROM cities WHERE id = '" + str(nb_repet_actuelle) + "'")
        LngPos2_actuelle = curseurLngPos2.fetchone() #Assignation de la longitude à la variable
        LngPos2_actuelle = LngPos2_actuelle[0]

        CoordVilleActuelle = (LatPos2_actuelle,LngPos2_actuelle) #Tuple de la ville étudiée

        if haversine(CoordVilleCentrale,CoordVilleActuelle) <= float(rayonCentralUser):
                curseurNomAlentours.execute("SELECT name FROM cities WHERE id = '" + str(nb_repet_actuelle ) + "'")
                NomVilleDansRayon = curseurNomAlentours.fetchone()
                NomVilleDansRayon = NomVilleDansRayon[0]
                alentours.append(NomVilleDansRayon)
                cpt_villes_alentours += 1


        ##indicateurs de répétitions
        if nb_repet_actuelle == 2500:
            print("*---------")
        if nb_repet_actuelle == 5000:
            print("**-------")
        if nb_repet_actuelle == 10000:
            print("***-------")
        if nb_repet_actuelle == 15000:
            print("****------")
        if nb_repet_actuelle == 20000:
            print("*****-----")
        if nb_repet_actuelle == 25000:
            print("******----")
        if nb_repet_actuelle == 30000:
            print("********--")
        if nb_repet_actuelle == 34500:
            print("**********")
        nb_repet_actuelle += 1
    print("Complete !")
    time.sleep(1.5)

    #print(alentours)#retour des villes proches
    if len(alentours) == 1:
         print("Il n'y a aucunes autre villes aux alentours de " + villeCentraleUser + " dans un rayon de " + str(rayonCentralUser) +"km. Essayez d'agrandir votre rayon de recherche.")
    else:
        print("Il y a "+ str(cpt_villes_alentours-1) +" villes aux alentours de "+villeCentraleUser + " dans un rayon de " + rayonCentralUser + "km :")
        for elt in alentours:
                if elt != villeCentraleUser:
                    print("-" + elt)