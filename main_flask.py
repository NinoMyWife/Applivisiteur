from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource, abort
from MYSQL import DBConnection, DBSelect, DBInsert

app = Flask(__name__)
api = Api(app)

@app.route('/Praticiens')
def Pratciens():
    MaDB = DBConnection()
    Praticiens = DBSelect(MaDB, "SELECT pra_prenom, pra_nom, pra_cp, pra_ville FROM praticien")
    if Praticiens :
        Feedback_Praticiens = [{"prenom" : Informations_Praticien[0], "nom" : Informations_Praticien[1], "cp" : Informations_Praticien[3], "ville" : Informations_Praticien[2]} for Informations_Praticien in Praticiens]
        return jsonify(Feedback_Praticiens)
    else :
        return jsonify({"msg": "Erreur SQL"}), 401

@app.route('/Authentification/<string:User>/<string:Password>')
def Authentification(User, Password):
    MaDB = DBConnection()
    User = User.split('_')
    Vis_matricule = DBSelect(MaDB, f"SELECT vis_matricule FROM visiteur WHERE vis_prenom = '{User[0]}' AND vis_nom = '{User[1]}' AND vis_mdp = '{Password}'")
    if Vis_matricule :
        return jsonify({"matricule" : Vis_matricule[0][0]})
    else :
        return jsonify({"matricule" : None})

@app.route('/Compterendus/<string:Vis_matricule>')
def Compte_Rendus(Vis_matricule):
    MaDB = DBConnection()
    Rapports = DBSelect(MaDB, f"SELECT rap_date_visite, rap_bilan, rap_motif, pra_num, med_nomcommercial, off_quantite FROM rapportvisite INNER JOIN offrir on rapportvisite.rap_num = offrir.rap_num INNER JOIN medicament ON offrir.med_depotlegal = medicament.med_depotlegal WHERE rapportvisite.vis_matricule = '{Vis_matricule}'")
    if Rapports : 
        Feedback_Rapports = []
        for Rapport in Rapports :
            Rapport_date, Rapport_bilan, Rapport_motif, Praticien_ID, Echantillon, Echantillon_qty  = Rapport
            Praticien_infos = DBSelect(MaDB, f"SELECT pra_prenom, pra_nom, pra_cp, pra_ville FROM praticien WHERE pra_num = '{Praticien_ID}'")
            pra_prenom, pra_nom, pra_cp, pra_ville = Praticien_infos[0]
            Rapport_infos = {"Date" : Rapport_date,
                        "pra_prenom" : pra_prenom,
                        "pra_nom" : pra_nom,
                        "pra_cp" : pra_cp,
                        "pra_ville" : pra_ville,
                        "Motif de la visite" : Rapport_motif, 
                        "Commentaire" : Rapport_bilan,
                        "Echantillon" : Echantillon,
                        "Echantillon_qty" : Echantillon_qty,
                        }                 
            Feedback_Rapports.append(Rapport_infos)
    else :
        return jsonify({"msg": "Erreur SQL"}), 401
    return jsonify(Feedback_Rapports)

@app.route('/AjoutCompterendus/<date>/<string:praticien>/<string:motif>/<string:echantillon>/<int:nbr_echantillon>/<string:resume>')
def AjoutCompterendus(date, praticien, motif, echantillon, nbr_echantillon, resume):
    MaDB = DBConnection()
    InfoPraticien = praticien.split(" ")
    IDpraticien = DBSelect(MaDB, f"SELECT pra_num FROM praticien WHERE pra_nom = {InfoPraticien[1]} AND pra_prenom = {InfoPraticien[0]}")
    NumCompterendu = DBSelect(MaDB, f"SELECT max(rap_num)+1 FROM rapportvisite")
    DBInsert(MaDB, f"INSERT INTO rapportvisite (vis_matricule, rap_num, rap_date_visite, rap_bilan, rap_motif VALUES ('{IDpraticien}', {NumCompterendu}, {date}, {resume}, {motif})")
    med_depotlegal = DBSelect(MaDB, f"SELECT med_depotlegal FROM medicament WHERE med_nomcommercial = {echantillon}")
    DBInsert(MaDB, f"INSERT INTO offir (vis_matricule, rap_num, med_depotlegal, off_quantite VALUES ('{IDpraticien}', {NumCompterendu}, '{med_depotlegal}', {nbr_echantillon})")


@app.route('/Medicaments')
def Medicaments():
    MaDB = DBConnection()
    Medicaments = DBSelect(MaDB, "SELECT med_nomcommercial FROM medicament")
    if Medicaments :
        Feedback_Medicaments = [Medicament[0] for Medicament in Medicaments]
        return jsonify(Feedback_Medicaments)
    else :
        return jsonify({"msg": "Erreur SQL"}), 401


if __name__== "__main__":
    app.run(debug=True)