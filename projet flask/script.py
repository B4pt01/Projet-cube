# Importer les bibliothèques nécessaires
from flask import Flask, render_template, request
import mysql.connector
from haversine import haversine
import time

# Initialiser l'application Flask
app = Flask(__name__)

# Établir la connexion à la base de données
BDD = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="codes_postaux"
)

# Définir une route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Définir une route pour traiter le formulaire
@app.route('/resultat', methods=['GET'])
def resultat():
    # Vérifier si 'choice' existe dans request.form
    if 'choice' not in request.args:
        return "Erreur : La chaîne de requête ne contient pas la clé 'choice'."
    
    choice = request.args['choice']
    param = request.args['param']
    rayon = request.args['rayon']
    alentours = []

    if choice == '1':
        
        try:
            curseur1 = BDD.cursor()
            curseur1.execute("SELECT zip_code FROM cities WHERE name = %s", (param,))
            res = curseur1.fetchone()
            result = res[0] if res else "Aucun résultat trouvé."
        finally:
            if 'curseur1' in locals():
                curseur1.close()
                
                
        ##curseur1 = BDD.cursor()
        ##curseur1.execute("SELECT zip_code FROM cities WHERE name = %s", (param,))
        ##res = curseur1.fetchone()
        ##result = res[0] if res else "Aucun résultat trouvé."
        # Fermer le curseur après avoir utilisé les résultats
        ##curseur1.close()

    elif choice == '2':   
    
        try:
            curseur2 = BDD.cursor()
            curseur2.execute("SELECT zip_code FROM cities WHERE name = %s", (param,))
            res = curseur2.fetchone()
            result = res[0] if res else "Aucun résultat trouvé."
        finally:
            if 'curseur2' in locals():
                curseur2.close()
         
        ##curseur2 = BDD.cursor()
        ##curseur2.execute("SELECT name FROM cities WHERE zip_code = %s", (param,))
        ##res2 = curseur2.fetchone()
        ##result = res2[0] if res2 else "Aucun résultat trouvé."
        # Fermer le curseur après avoir utilisé les résultats
        ##curseur2.close()
        

    #elif choice == '3':
    #    cpt_villes_alentours = 0
    #    villeCentraleUser = input("Veuillez choisir une ville ->")
    #    rayonCentralUser = input("Choisissez le rayon autour de cette ville ->")
    #    ###définition du tuple de la ville qui est le point central###
    #    curseurCentralLat = BDD.cursor()
    #    curseurCentralLat.execute("SELECT gps_lat FROM cities WHERE name = '" + villeCentraleUser + "'")
    #    latCentrale = curseurCentralLat.fetchone()
    #    latCentrale = latCentrale[0] #Latitude de la ville centrale
    #    #print(latCentrale)

    #    curseurCentralLng = BDD.cursor()
    #    curseurCentralLng.execute("SELECT gps_lng FROM cities WHERE gps_lat = '" + str(latCentrale) +"'")
    #    lngCentrale = curseurCentralLng.fetchone()
    #    lngCentrale = lngCentrale[0] #Longitude de la ville centrale
    #    #print(lngCentrale)

    #    CoordVilleCentrale = (latCentrale,lngCentrale) #Latitude et longitude combinées sous forme de tuple

        ##################################

    #    nb_repet_actuelle = 1
    #    alentours = []

    #    curseurMax = BDD.cursor()
    #    curseurMax.execute("SELECT MAX(id) FROM cities")
    #    nb_repet_max = curseurMax.fetchone()
    #    nb_repet_max = nb_repet_max[0] #Nombre de villes au total
        #print(nb_repet_max)

    #    curseurNomAlentours = BDD.cursor()
    #    curseurLatPos2 = BDD.cursor()
    #    curseurLngPos2 = BDD.cursor()
    #    while nb_repet_actuelle != nb_repet_max:
    #        curseurLatPos2.execute("SELECT gps_lat FROM cities WHERE id = '" + str(nb_repet_actuelle) + "'") #récupère la latitude de la pos2 actuelle
    #        LatPos2_actuelle = curseurLatPos2.fetchone() #assignation de la latitude à la variable
    #        LatPos2_actuelle = LatPos2_actuelle[0]

    #        curseurLngPos2.execute("SELECT gps_lng FROM cities WHERE id = '" + str(nb_repet_actuelle) + "'")
    #        LngPos2_actuelle = curseurLngPos2.fetchone() #Assignation de la longitude à la variable
    #        LngPos2_actuelle = LngPos2_actuelle[0]

    #        CoordVilleActuelle = (LatPos2_actuelle,LngPos2_actuelle) #Tuple de la ville étudiée

    #        if haversine(CoordVilleCentrale,CoordVilleActuelle) <= float(rayonCentralUser):
    #                curseurNomAlentours.execute("SELECT name FROM cities WHERE id = '" + str(nb_repet_actuelle ) + "'")
    #                NomVilleDansRayon = curseurNomAlentours.fetchone()
    #                NomVilleDansRayon = NomVilleDansRayon[0]
    #                alentours.append(NomVilleDansRayon)
    #                cpt_villes_alentours += 1


            ##indicateurs de répétitions
            ##if nb_repet_actuelle == 2500:
            ##    print("*---------")
           ##if nb_repet_actuelle == 5000:
             ##   print("**-------")
            ##if nb_repet_actuelle == 10000:
             ##   print("***-------")
            ##if nb_repet_actuelle == 15000:
             ##   print("****------")
            ##if nb_repet_actuelle == 20000:
             ##   print("*****-----")
            ##if nb_repet_actuelle == 25000:
             ##   print("******----")
            ##if nb_repet_actuelle == 30000:
              ##  print("********--")
            ##if nb_repet_actuelle == 34500:
             ##  print("**********")
            ##nb_repet_actuelle += 1
        ###print("Complete !")
        ###time.sleep(1.5)

        #print(alentours)#retour des villes proches
    #    if len(alentours) == 1:
    #        print("Il n'y a aucunes autre villes aux alentours de " + villeCentraleUser + " dans un rayon de " + str(rayonCentralUser) +"km. Essayez d'agrandir votre rayon de recherche.")
    #    else:
    #        print("Il y a "+ str(cpt_villes_alentours-1) +" villes aux alentours de "+villeCentraleUser + " dans un rayon de " + rayonCentralUser + "km :")
    #        for elt in alentours:
    #                if elt != villeCentraleUser:
    #                    print("-" + elt)
        

    return render_template('résultat.html', result=result, alentours=alentours)

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)

