# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grade.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_widget(QMainWindow):
    def __init__(self):
        super(Ui_widget, self).__init__()
        self.setupUi(self)

    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(500, 400)
        widget.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.tableView = QtWidgets.QTableView(widget)
        self.tableView.setGeometry(QtCore.QRect(5, 1, 491, 221))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(10, 260, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(widget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 260, 148, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(260, 260, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 260, 148, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(60, 327, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(widget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 327, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(widget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 327, 93, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(widget)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 327, 93, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(widget.close)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "年级设置"))
        self.label.setText(_translate("widget", "年级编号："))
        self.label_2.setText(_translate("widget", "年级名称："))
        self.pushButton.setText(_translate("widget", " 添  加"))
        self.pushButton_2.setText(_translate("widget", "修  改"))
        self.pushButton_3.setText(_translate("widget", "删  除"))
        self.pushButton_4.setText(_translate("widget", "退  出"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_widget()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())