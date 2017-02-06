# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dave\Desktop\Programming\plates\resources\plates.ui'
#
# Created: Tue Oct 22 11:28:19 2013
#      by: PyQt5 UI code generator 5.0.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(450, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setMinimumSize(QtCore.QSize(450, 480))
        Main.setMaximumSize(QtCore.QSize(450, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        Main.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(140, 350, 171, 41))
        self.btn_download.setObjectName("btn_download")
        self.lbl_version = QtWidgets.QLabel(self.centralwidget)
        self.lbl_version.setGeometry(QtCore.QRect(60, 400, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_version.setFont(font)
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.tree_display = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree_display.setGeometry(QtCore.QRect(10, 10, 331, 241))
        self.tree_display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tree_display.setObjectName("tree_display")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(350, 10, 91, 31))
        self.btn_save.setObjectName("btn_save")
        self.lbl_hilow = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hilow.setGeometry(QtCore.QRect(70, 280, 51, 16))
        self.lbl_hilow.setObjectName("lbl_hilow")
        self.cb_type = QtWidgets.QComboBox(self.centralwidget)
        self.cb_type.setGeometry(QtCore.QRect(120, 300, 101, 31))
        self.cb_type.setEditable(False)
        self.cb_type.setMaxVisibleItems(15)
        self.cb_type.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_type.setObjectName("cb_type")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_high = QtWidgets.QComboBox(self.centralwidget)
        self.cb_high.setGeometry(QtCore.QRect(60, 300, 51, 31))
        self.cb_high.setEditable(False)
        self.cb_high.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_high.setObjectName("cb_high")
        self.cb_high.addItem("")
        self.cb_high.setItemText(0, "")
        self.cb_high.addItem("")
        self.lbl_type = QtWidgets.QLabel(self.centralwidget)
        self.lbl_type.setGeometry(QtCore.QRect(140, 280, 81, 16))
        self.lbl_type.setObjectName("lbl_type")
        self.lbl_suffix = QtWidgets.QLabel(self.centralwidget)
        self.lbl_suffix.setGeometry(QtCore.QRect(230, 280, 41, 16))
        self.lbl_suffix.setObjectName("lbl_suffix")
        self.cb_suffix = QtWidgets.QComboBox(self.centralwidget)
        self.cb_suffix.setGeometry(QtCore.QRect(230, 300, 31, 31))
        self.cb_suffix.setEditable(False)
        self.cb_suffix.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_suffix.setObjectName("cb_suffix")
        self.cb_suffix.addItem("")
        self.cb_suffix.setItemText(0, "")
        self.cb_suffix.addItem("")
        self.cb_suffix.addItem("")
        self.cb_suffix.addItem("")
        self.lbl_runway = QtWidgets.QLabel(self.centralwidget)
        self.lbl_runway.setGeometry(QtCore.QRect(270, 280, 41, 16))
        self.lbl_runway.setObjectName("lbl_runway")
        self.cb_lr = QtWidgets.QComboBox(self.centralwidget)
        self.cb_lr.setGeometry(QtCore.QRect(310, 300, 41, 31))
        self.cb_lr.setEditable(False)
        self.cb_lr.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_lr.setObjectName("cb_lr")
        self.cb_lr.addItem("")
        self.cb_lr.setItemText(0, "")
        self.cb_lr.addItem("")
        self.cb_lr.addItem("")
        self.cb_lr.addItem("")
        self.cb_lr.addItem("")
        self.lbl_ident = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ident.setGeometry(QtCore.QRect(10, 280, 61, 16))
        self.lbl_ident.setObjectName("lbl_ident")
        self.lbl_ident_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ident_2.setGeometry(QtCore.QRect(10, 260, 51, 16))
        self.lbl_ident_2.setObjectName("lbl_ident_2")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(350, 220, 91, 31))
        self.btn_add.setObjectName("btn_add")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 280, 31, 16))
        self.label_5.setObjectName("label_5")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(350, 50, 91, 31))
        self.btn_delete.setObjectName("btn_delete")
        self.lbl_cat = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cat.setGeometry(QtCore.QRect(380, 280, 71, 16))
        self.lbl_cat.setObjectName("lbl_cat")
        self.cb_cat = QtWidgets.QComboBox(self.centralwidget)
        self.cb_cat.setGeometry(QtCore.QRect(360, 300, 81, 31))
        self.cb_cat.setEditable(False)
        self.cb_cat.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cb_cat.setObjectName("cb_cat")
        self.cb_cat.addItem("")
        self.cb_cat.setItemText(0, "")
        self.cb_cat.addItem("")
        self.cb_cat.addItem("")
        self.cb_cat.addItem("")
        self.cb_cat.addItem("")
        self.cb_cat.addItem("")
        self.cb_cat.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 330, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.le_ident = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ident.setGeometry(QtCore.QRect(10, 300, 41, 31))
        self.le_ident.setMaxLength(4)
        self.le_ident.setFrame(True)
        self.le_ident.setObjectName("le_ident")
        self.le_rwy = QtWidgets.QLineEdit(self.centralwidget)
        self.le_rwy.setGeometry(QtCore.QRect(270, 300, 31, 31))
        self.le_rwy.setMaxLength(2)
        self.le_rwy.setObjectName("le_rwy")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(320, 360, 121, 21))
        self.progressBar.setMaximum(1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(Main)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCombine = QtWidgets.QAction(Main)
        self.actionCombine.setCheckable(True)
        self.actionCombine.setChecked(True)
        self.actionCombine.setObjectName("actionCombine")
        self.menuOptions.addAction(self.actionCombine)
        self.menuOptions.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Plates v0.3"))
        self.btn_download.setText(_translate("Main", "Download plates"))
        self.lbl_version.setText(_translate("Main", "<html><head/><body><p><span style=\" font-size:12pt;\">Plate version: January 2013</span></p></body></html>"))
        self.tree_display.headerItem().setText(0, _translate("Main", "Identifier"))
        self.tree_display.headerItem().setText(1, _translate("Main", "Procedure"))
        self.tree_display.headerItem().setText(2, _translate("Main", "Runway"))
        self.btn_save.setToolTip(_translate("Main", "Shortcut: Ctrl + s"))
        self.btn_save.setText(_translate("Main", "Save"))
        self.lbl_hilow.setText(_translate("Main", "High"))
        self.cb_type.setItemText(0, _translate("Main", "Airport diagram"))
        self.cb_type.setItemText(1, _translate("Main", "ILS"))
        self.cb_type.setItemText(2, _translate("Main", "ILS or LOC"))
        self.cb_type.setItemText(3, _translate("Main", "ILS or LOC-DME"))
        self.cb_type.setItemText(4, _translate("Main", "Light visual"))
        self.cb_type.setItemText(5, _translate("Main", "Localizer"))
        self.cb_type.setItemText(6, _translate("Main", "NDB"))
        self.cb_type.setItemText(7, _translate("Main", "RNAV (GPS)"))
        self.cb_type.setItemText(8, _translate("Main", "RNAV (RNP)"))
        self.cb_type.setItemText(9, _translate("Main", "Tacan"))
        self.cb_type.setItemText(10, _translate("Main", "VOR"))
        self.cb_type.setItemText(11, _translate("Main", "VOR-DME"))
        self.cb_high.setItemText(1, _translate("Main", "High"))
        self.lbl_type.setText(_translate("Main", "Procedure"))
        self.lbl_suffix.setText(_translate("Main", "Suffix"))
        self.cb_suffix.setItemText(1, _translate("Main", "Y"))
        self.cb_suffix.setItemText(2, _translate("Main", "Z"))
        self.cb_suffix.setItemText(3, _translate("Main", "A"))
        self.lbl_runway.setText(_translate("Main", "Rwy"))
        self.cb_lr.setItemText(1, _translate("Main", "L"))
        self.cb_lr.setItemText(2, _translate("Main", "C"))
        self.cb_lr.setItemText(3, _translate("Main", "R"))
        self.cb_lr.setItemText(4, _translate("Main", "LR"))
        self.lbl_ident.setText(_translate("Main", "identifier"))
        self.lbl_ident_2.setText(_translate("Main", "Airport"))
        self.btn_add.setToolTip(_translate("Main", "Shortcut: Enter"))
        self.btn_add.setText(_translate("Main", "Add"))
        self.label_5.setText(_translate("Main", "L/R"))
        self.btn_delete.setToolTip(_translate("Main", "Deletes selected item. Shortcut: Delete"))
        self.btn_delete.setText(_translate("Main", "Delete"))
        self.lbl_cat.setText(_translate("Main", "Category"))
        self.cb_cat.setItemText(1, _translate("Main", "CAT I"))
        self.cb_cat.setItemText(2, _translate("Main", "CAT II"))
        self.cb_cat.setItemText(3, _translate("Main", "CAT I & II"))
        self.cb_cat.setItemText(4, _translate("Main", "CAT II & III"))
        self.cb_cat.setItemText(5, _translate("Main", "SA CAT I"))
        self.cb_cat.setItemText(6, _translate("Main", "SA CAT I & II"))
        self.menuOptions.setTitle(_translate("Main", "Menu"))
        self.actionAbout.setText(_translate("Main", "About"))
        self.actionCombine.setText(_translate("Main", "Combine files"))

import plates_rc
