from flask import Flask
from flask import render_template
from flask import request
import json
from pymongo import MongoClient
from flask import session




app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")

db = client["Site_reservation"]

formu_contact = db["formulaire_contacts"]
db_hotel = db["Hotels"]
reservations = db["reservation_client"]


@app.route("/",methods= ['GET'])
def hello_world():
    return render_template('index.html')





#------------------Route contact----------------


@app.route("/contact",methods= ['GET','POST'])
def contact():
    if request.method == "POST":
        
        nom = request.form["nom"]
        prenom = request.form['prenom']
        tel = request.form['tel']
        mail = request.form['mail']
        message = request.form['message']

        new_contact={"Nom" : nom, "Prenom" : prenom, "Tel": tel, "Mail": mail,"Message" : message,}
        

        formu_contact.insert_one(new_contact)

        return render_template('thankyou.html')

    else:    
        return render_template('contact.html')



#------------------Route contact----------------




#---------------Route Hotels----------

@app.route("/hotels",methods= ['GET'])

def hotels():

    
    list_hotels = list(db_hotel.find())

    return render_template('hotels.html', hotels=list_hotels)

#---------------Route Hotels-----------




#---------------Reservation-----------

@app.route("/reservation/<slug>",methods= ['GET'])
def hotel_cibling(slug):

    list_hotels = (db_hotel.find_one({"slug":slug}))


    return render_template('reservation.html',hotel=list_hotels)


@app.route("/customers", methods=["POST"])
def customers():
    

    depart_start = request.form['depart']
    depart_end = request.form['sortie']
    nombre_de_majeur = request.form['adultes']
    nombre_de_mineur = request.form['enfants']

    nom = request.form['nom']
    prenom = request.form['prenom']
    adresse = request.form['adresse']
    ville = request.form['ville']
    code_postal = request.form['cp']
    tel = request.form['tel']
    mail = request.form['mail']

    name_hotel = request.form['hotel_name']
    adresse_hotel = request.form['hotel_adresse']
    ville_hotel = request.form['hotel_ville']
    cp_hotel = request.form['hotel_cp']
    tel_hotel = request.form['hotel_tel']
    pays_hotel = request.form['hotel_pays']

    reservation = {'Date arrivé':depart_start,'Date de depart' :depart_end,"Nombre adulte": int(nombre_de_majeur),"Nombre enfants":int(nombre_de_mineur),
                   'Nom': nom,"Prenom":prenom,'Adresse':adresse,"Ville":ville,"Cp":code_postal,"Tel": tel, "Mail": mail,'Hotel reserve' : name_hotel,"Adresse_H":adresse_hotel,"Ville_H":ville_hotel,"Cp_H":cp_hotel,"Telephone_H": tel_hotel,"Pays_H":pays_hotel}
    
    reservations.insert_one(reservation)

    return render_template('paiement.html')


#---------------Reservation-----------

@app.route("/paiements_process")
def paiement():
    return render_template('paiement.html')