# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import requests
from hashlib import sha512

BASE = "http://127.0.0.1:5000/"
# BASE = "http://api-gsb.gsb.lan/"

def Authentification(user, PasswordHash):
    response = requests.get(f"{BASE}Authentification/{user}/{PasswordHash}")
    outputjson = response.json()
    return outputjson

def HashPassword(password):
    mdp = password.encode()
    mdp_sign = sha512(mdp).hexdigest()
    return mdp_sign

class Ui_MainWindow(object):
    
    def getLogin(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        PasswordHash = HashPassword(password)
        Verification = Authentification(user, PasswordHash)
        if Verification["matricule"] is None:
            exit
        else :
            os.system(f'python Applivisiteur.py {Verification["matricule"]} {user}')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 550)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color : rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 170, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("color:rgb(0, 0, 0);")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 280, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("color:rgb(0, 0, 0);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.GSB_Logo = QtWidgets.QLabel(self.centralwidget)
        self.GSB_Logo.setGeometry(QtCore.QRect(158, 50, 150, 93))
        self.GSB_Logo.setObjectName("GSB_Logo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(145, 360, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color : rgb(0, 0, 0)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getLogin)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Connexion", "Connexion"))
        self.GSB_Logo.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"C:\\Users\\tofre\\Desktop\\logo-gsb.png\"/></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "   Nom d'utilisateur"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "   Mot de passe"))
        self.label.setText(_translate("MainWindow", "Connexion"))
        self.pushButton.setText(_translate("MainWindow", "Se connecter"))
        self.label.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
