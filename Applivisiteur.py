# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Applivisiteur.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json
import sys
from datetime import datetime

BASE = "http://127.0.0.1:5000"
# BASE = "http://api-gsb.gsb.lan"

def getPraticien():
    response = requests.get(f"{BASE}/Praticiens")
    outputjson = response.json()
    Praticiens = [f'{Informations_Praticien["prenom"]} {Informations_Praticien["nom"]} {Informations_Praticien["ville"]} {Informations_Praticien["cp"]}' for Informations_Praticien in outputjson]
    return sorted(Praticiens)

def getCompteRendu(Vis_matricule):
    response = requests.get(f"{BASE}/Compterendus/{Vis_matricule}")
    outputjson = response.json()
    compterendus = [f'Date : {(datetime.strptime(compterendu["Date"], "%a, %d %b %Y %H:%M:%S %Z")).strftime("%d/%m/%Y")}        Praticien : {compterendu["pra_prenom"]} {compterendu["pra_nom"]} {compterendu["pra_cp"]} {compterendu["pra_ville"]}\r\nMotif de la visite : {compterendu["Motif de la visite"]}\r\nEchantillons : {compterendu["Echantillon"]} x{compterendu["Echantillon_qty"]}\r\nCommentaire : {compterendu["Commentaire"]}\n' for compterendu in outputjson]
    return compterendus

def addCompteRendu(date, praticien, motif, echantillon, nbr_echantillon, resume):
    requests.get(f"{BASE}/AjoutCompterendus/{date}/{praticien}/{motif}/{echantillon}/{nbr_echantillon}/{resume}")

def getMedicaments():
    response = requests.get(f"{BASE}/Medicaments")
    outputjson = response.json()
    return sorted(outputjson)


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'foo' and
            self.textPass.text() == 'bar'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

class Ui_MainWindow(object):
    Vis_matricule = Login().textName
    UserLogin = Login().textPass
    UserFullName = UserLogin.replace("_", " ")

    def getFullCompteRendu(self):
        nbr_echantillon = self.echantillon_spinBox.text()
        echantillon = self.medicament_list_box.currentText()
        date = self.visitdate.text()
        motif = self.motif_textbox.text()
        praticien = self.praticien_list_box.currentText()
        resume_text = self.textEdit.toPlainText()
        Post_compte_rendu = f"Date : {date}        Praticien : {praticien}\r\nMotif de la visite : {motif}\r\nEchantillons : {echantillon} x{nbr_echantillon}\r\nCommentaire : {resume_text}\n"
        self.listWidget.addItem(Post_compte_rendu)

    def setupUi(self, MainWindow, Vis_matricule):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1080, 720))
        self.tabWidget.setMinimumSize(QtCore.QSize(1080, 720))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.Accueil = QtWidgets.QWidget()
        self.Accueil.setObjectName("Accueil")
        self.bonjour_label = QtWidgets.QLabel(self.Accueil)
        self.bonjour_label.setGeometry(QtCore.QRect(425, 290, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.bonjour_label.setFont(font)
        self.bonjour_label.setObjectName("bonjour_label")
        self.user_name_label = QtWidgets.QLabel(self.Accueil)
        self.user_name_label.setGeometry(QtCore.QRect(425, 325, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.user_name_label.setFont(font)
        self.user_name_label.setObjectName("user_name_label")
        self.tabWidget.addTab(self.Accueil, "")
        self.Compte_rendu_de_la_visite = QtWidgets.QWidget()
        self.Compte_rendu_de_la_visite.setObjectName("Compte_rendu_de_la_visite")
        self.compte_rendu_title = QtWidgets.QLabel(self.Compte_rendu_de_la_visite)
        self.compte_rendu_title.setGeometry(QtCore.QRect(20, 80, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        self.compte_rendu_title.setFont(font)
        self.compte_rendu_title.setStyleSheet("color:rgb(0, 0, 0)")
        self.compte_rendu_title.setObjectName("compte_rendu_title")
        self.praticien_label = QtWidgets.QLabel(self.Compte_rendu_de_la_visite)
        self.praticien_label.setGeometry(QtCore.QRect(20, 130, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.praticien_label.setFont(font)
        self.praticien_label.setObjectName("praticien_label")
        self.date_label = QtWidgets.QLabel(self.Compte_rendu_de_la_visite)
        self.date_label.setGeometry(QtCore.QRect(20, 180, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.motif_label = QtWidgets.QLabel(self.Compte_rendu_de_la_visite)
        self.motif_label.setGeometry(QtCore.QRect(20, 230, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.motif_label.setFont(font)
        self.motif_label.setObjectName("motif_label")
        self.echantillon_label = QtWidgets.QLabel(self.Compte_rendu_de_la_visite)
        self.echantillon_label.setGeometry(QtCore.QRect(20, 280, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.echantillon_label.setFont(font)
        self.echantillon_label.setObjectName("echantillon_label")
        self.resume_label = QtWidgets.QLabel(self.Compte_rendu_de_la_visite)
        self.resume_label.setGeometry(QtCore.QRect(20, 330, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.resume_label.setFont(font)
        self.resume_label.setObjectName("resume_label")
        self.textEdit = QtWidgets.QTextEdit(self.Compte_rendu_de_la_visite)
        self.textEdit.setGeometry(QtCore.QRect(240, 330, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.echantillon_spinBox = QtWidgets.QSpinBox(self.Compte_rendu_de_la_visite)
        self.echantillon_spinBox.setGeometry(QtCore.QRect(350, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.echantillon_spinBox.setFont(font)
        self.echantillon_spinBox.setObjectName("echantillon_spinBox")
        self.visitdate = QtWidgets.QDateEdit(self.Compte_rendu_de_la_visite)
        self.visitdate.setGeometry(QtCore.QRect(210, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.visitdate.setFont(font)
        self.visitdate.setObjectName("visitdate")
        self.motif_textbox = QtWidgets.QLineEdit(self.Compte_rendu_de_la_visite)
        self.motif_textbox.setGeometry(QtCore.QRect(220, 230, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.motif_textbox.setFont(font)
        self.motif_textbox.setObjectName("motif_textbox")
        self.praticien_list_box = QtWidgets.QComboBox(self.Compte_rendu_de_la_visite)
        self.praticien_list_box.setGeometry(QtCore.QRect(230, 130, 450, 31))
        self.praticien_list_box.setObjectName("praticien_list_box")
        self.praticien_list_box.addItems(getPraticien())
        self.medicament_list_box = QtWidgets.QComboBox(self.Compte_rendu_de_la_visite)
        self.medicament_list_box.setGeometry(QtCore.QRect(440, 280, 250, 31))
        self.medicament_list_box.setObjectName("medicament_list_box")
        self.medicament_list_box.addItems(getMedicaments())
        self.tabWidget.addTab(self.Compte_rendu_de_la_visite, "")
        self.Historique_des_visites = QtWidgets.QWidget()
        self.Historique_des_visites.setObjectName("Historique_des_visites")
        self.historique_label = QtWidgets.QLabel(self.Historique_des_visites)
        self.historique_label.setGeometry(QtCore.QRect(20, 80, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        self.historique_label.setFont(font)
        self.historique_label.setStyleSheet("color:rgb(0, 0, 0)")
        self.historique_label.setObjectName("historique_label")
        self.listWidget = QtWidgets.QListWidget(self.Historique_des_visites)
        self.listWidget.setGeometry(QtCore.QRect(20, 130, 1000, 500))
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItems(getCompteRendu(Vis_matricule))
        self.tabWidget.addTab(self.Historique_des_visites, "")
        self.Presentation_des_produits = QtWidgets.QWidget()
        self.Presentation_des_produits.setObjectName("Presentation_des_produits")
        self.tabWidget.addTab(self.Presentation_des_produits, "")
        self.Deconnexion = QtWidgets.QWidget()
        self.Deconnexion.setObjectName("Deconnexion")
        self.tabWidget.addTab(self.Deconnexion, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton = QtWidgets.QPushButton(self.Compte_rendu_de_la_visite)
        self.pushButton.setGeometry(QtCore.QRect(20, 450, 211, 24))
        self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(self.getFullCompteRendu)
        self.pushButton.clicked.connect(addCompteRendu(self.visitdate.text(), self.praticien_list_box.currentText(), self.motif_textbox.text(), self.medicament_list_box.currentText(), self.echantillon_spinBox.text(), self.textEdit.toPlainText()))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, UserFullName):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Applivisiteur", "Applivisiteur"))
        self.bonjour_label.setText(_translate("MainWindow", "Bonjour"))
        self.user_name_label.setText(_translate("MainWindow", f"{UserFullName}"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Accueil), _translate("MainWindow", "Accueil"))
        self.compte_rendu_title.setText(_translate("MainWindow", "Compte rendu :"))
        self.praticien_label.setText(_translate("MainWindow", "Nom du praticien :"))
        self.date_label.setText(_translate("MainWindow", "Date de la visite :"))
        self.motif_label.setText(_translate("MainWindow", "Motif de la visite :"))
        self.echantillon_label.setText(_translate("MainWindow", "Nombres d\'échantillons laissés :"))
        self.resume_label.setText(_translate("MainWindow", "Résumé de la visite :"))
        self.pushButton.setText(_translate("MainWindow", "Enregistrer le compte rendu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Compte_rendu_de_la_visite), _translate("MainWindow", "Compte rendu de la visite"))
        self.historique_label.setText(_translate("MainWindow", f"Historique des comptes rendus de {UserFullName}:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Historique_des_visites), _translate("MainWindow", "Historique des visites"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Presentation_des_produits), _translate("MainWindow", "Présentation des produits"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Deconnexion), _translate("MainWindow", "Deconnexion"))
        self.bonjour_label.adjustSize()
        self.user_name_label.adjustSize()
        self.compte_rendu_title.adjustSize()
        self.praticien_label.adjustSize()
        self.date_label.adjustSize()
        self.motif_label.adjustSize()
        self.echantillon_label.adjustSize()
        self.resume_label.adjustSize()
        self.historique_label.adjustSize()
        self.pushButton.adjustSize()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        import sys
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())