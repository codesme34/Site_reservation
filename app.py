from flask import Flask
from flask import render_template
from flask import request
import json
from pymongo import MongoClient





app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")

db = client["Site_reservation"]

formu_contact = db["formulaire_contacts"]
db_hotel = db["Hotels"]


@app.route("/",methods= ['GET'])
def hello_world():
    return render_template('index.html')







#Route contact


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



#Route contact





#Route Hotels

@app.route("/hotels",methods= ['GET'])

def hotels():

    

    list_hotels = list(db_hotel.find())

    return render_template('hotels.html', hotels=list_hotels)

#Route Hotels






@app.route("/paiements_process1")
def pp1():
    return render_template('pp1.html')

@app.route("/paiements_process2")
def pp2():
    return render_template('pp2.html')