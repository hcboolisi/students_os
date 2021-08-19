# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resulttinfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView
from service import service


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 10, 71, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 49, 790, 341))
        self.tableWidget.setObjectName("tableView")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(720, 10, 71, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 10, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 10, 87, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 10, 72, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(530, 10, 87, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.bindCbox()
        self.query()
        self.pushButton_4.clicked.connect(self.query)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生成绩查询"))
        self.pushButton_4.setText(_translate("MainWindow", "查 询"))
        self.pushButton_5.setText(_translate("MainWindow", "退 出"))
        self.label.setText(_translate("MainWindow", "输入学生姓名："))
        self.label_2.setText(_translate("MainWindow", "考试种类："))
        self.label_3.setText(_translate("MainWindow", "考试科目："))

    def bindCbox(self):
        self.comboBox.addItem("所有")
        result = service.query("select kindName from tb_examkinds")
        for i in result:
            self.comboBox.addItem(i[0])

        self.comboBox_2.addItem("所有")
        result = service.query("select subName from tb_subject")
        for i in result:
            self.comboBox_2.addItem(i[0])

    def query(self):
        stu_name = self.lineEdit.text()
        kind_name = self.comboBox.currentText()
        sub_name = self.comboBox_2.currentText()
        if stu_name == "":
            if kind_name == "所有":
                if sub_name == "所有":
                    result = service.query("select stuID, stuName, CONCAT(gradeName,className),\
                                            subName, kindName, result from v_resultinfo")
                else:
                    result = service.query("select stuID, stuName, CONCAT(gradeName,className),\
                                            subName, kindName, result from v_resultinfo where subName = %s",
                                           sub_name)
            else:
                if sub_name == "所有":
                    result = service.query("select stuID, stuName, CONCAT(gradeName,className),\
                                            subName, kindName, result from v_resultinfo where kindName = %s",
                                           kind_name)
                else:
                    result = service.query("select stuID, stuName, CONCAT(gradeName,className),\
                                            subName, kindName, result from v_resultinfo where subName = %s\
                                           and kindname = %s", sub_name, kind_name)
        else:
            if kind_name == "所有":
                if sub_name == "所有":
                    sql = "select stuID, stuName, CONCAT(gradeName,className),\
                        subName, kindName, result from v_resultinfo where stuName like '%" + stu_name + "%'"
                else:
                    sql = "select stuID, stuName, CONCAT(gradeName,className),\
                        subName, kindName, result from v_resultinfo where stuName like '%" + stu_name + "%'\
                        and subName like '%" + sub_name + "%'"
            else:
                if sub_name == "所有":
                    sql = "select stuID, stuName, CONCAT(gradeName,className),\
                        subName, kindName, result from v_resultinfo where stuName like '%" + stu_name + "%'\
                        and kindName like '%" + kind_name + "%'"
                else:
                    sql = "select stuID, stuName, CONCAT(gradeName,className),\
                        subName, kindName, result from v_resultinfo where stuName like '%" + stu_name + "%'\
                        and kindName like '%" + kind_name + "%' and subName like '%" + sub_name + "%'"
            result = service.query2(sql)
        row = len(result)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["学生编号", "学生姓名", "班级",
                                                    "科目", "种类", "成绩"])
        for i in range(row):
            for j in range(self.tableWidget.columnCount()):
                date = QTableWidgetItem(str(result[i][j]))
                date.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.tableWidget.setItem(i, j, date)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())