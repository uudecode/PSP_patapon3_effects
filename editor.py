# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1395, 939)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(40, 20, 131, 23))
        self.openFileButton.setObjectName("openFileButton")
        self.saveFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveFileButton.setGeometry(QtCore.QRect(180, 20, 121, 23))
        self.saveFileButton.setObjectName("saveFileButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(970, 850, 311, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(960, 470, 271, 351))
        self.label_4.setObjectName("label_4")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(1240, 850, 75, 23))
        self.exitButton.setObjectName("exitButton")
        self.fileName = QtWidgets.QLabel(self.centralwidget)
        self.fileName.setGeometry(QtCore.QRect(320, 20, 261, 16))
        self.fileName.setText("")
        self.fileName.setObjectName("fileName")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1180, 20, 159, 22))
        self.comboBox.setMaxVisibleItems(50)
        self.comboBox.setObjectName("comboBox")
        self.loadedCount = QtWidgets.QLCDNumber(self.centralwidget)
        self.loadedCount.setEnabled(True)
        self.loadedCount.setGeometry(QtCore.QRect(1090, 20, 64, 23))
        self.loadedCount.setAutoFillBackground(False)
        self.loadedCount.setObjectName("loadedCount")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 110, 341, 80))
        self.groupBox.setObjectName("groupBox")
        self.EffectName = QtWidgets.QLineEdit(self.groupBox)
        self.EffectName.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.EffectName.setReadOnly(True)
        self.EffectName.setObjectName("EffectName")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.ID = QtWidgets.QLineEdit(self.groupBox)
        self.ID.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.ID.setReadOnly(True)
        self.ID.setObjectName("ID")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 230, 120, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(550, 210, 120, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(800, 220, 120, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(850, 130, 120, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(350, 400, 120, 80))
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(280, 570, 120, 80))
        self.groupBox_7.setObjectName("groupBox_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1395, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openFileButton.setText(_translate("MainWindow", "Открыть файл"))
        self.saveFileButton.setText(_translate("MainWindow", "Сохранить файл"))
        self.label_3.setText(_translate("MainWindow", "<a href=\"https://github.com/Goldmoyai\">https://github.com/Goldmoyai</a>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/peppapon/patapon_editor1.png\"/></p></body></html>"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.groupBox.setTitle(_translate("MainWindow", "Effect"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Base"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Effect flags 1"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Physics"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Hitbox"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Appearance"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Animation"))
import peppapon_rc