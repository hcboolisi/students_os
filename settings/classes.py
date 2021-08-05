# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QAbstractItemView
from service import service


class Ui_Form(QMainWindow):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        Form.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(5, 1, 490, 215))
        self.tableWidget.setObjectName("tableView")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.itemClicked.connect(self.getItem)
        self.query()

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(100, 230, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.bindGrade()


        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 280, 141, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 280, 141, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 340, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add)

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 340, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.edit)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 340, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.delete)

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 340, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "班级设置"))
        self.label.setText(_translate("Form", "选择年级："))
        self.label_2.setText(_translate("Form", "班级编号："))
        self.label_3.setText(_translate("Form", "班级名称："))
        self.pushButton.setText(_translate("Form", "添  加"))
        self.pushButton_2.setText(_translate("Form", "修  改"))
        self.pushButton_3.setText(_translate("Form", "删  除"))
        self.pushButton_4.setText(_translate("Form", "退  出"))

    def query(self):
        self.tableWidget.setRowCount(0)
        result = service.query("select classID,gradeName,className from v_classinfo")
        row = len(result)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["班级编号", "所属年级", "班级名称"])
        for i in range(row):
            for j in range(self.tableWidget.columnCount()):
                data = QTableWidgetItem(str(result[i][j]))
                data.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.tableWidget.setItem(i, j, data)

    def bindGrade(self):
        result = service.query('select gradeName from tb_grade')
        for i in result:
            self.comboBox.addItem(i[0])

    def getName(self, cid, name):
        result = service.query("select * from tb_class where gradeID = %s and className = %s", cid, name)
        return len(result)

    def getItem(self, item):
        if item.column() == 0:
            self.select = item.text()
            self.lineEdit.setText(self.select)

    def add(self):
        classID = self.lineEdit.text()
        className = self.lineEdit_2.text()
        if self.comboBox.currentText() != "":
            result = service.query("select gradeID from tb_grade where gradeName = %s",
                                   self.comboBox.currentText())
            if len(result) > 0:
                gradeID = result[0]
                if classID != "" and className != "":
                    if self.getName(gradeID, className) > 0:
                        self.lineEdit.setText("")
                        self.lineEdit_2.setText("")
                        QMessageBox.information(None, "提示", "您要添加的班级已存在，请重新输入！",
                                                QMessageBox.Ok)
                    else:
                        result = service.exec("insert into tb_class(classID,gradeID,className) values (%s,%s,%s)",
                                              (classID, gradeID, className))
                        if result > 0:
                            self.query()
                            self.lineEdit.setText("")
                            self.lineEdit_2.setText("")
                            QMessageBox.information(None, "提示", "信息添加成功", QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, "警告", "请输入数据后再执行相关操作！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None, "警告", "请先添加年级！", QMessageBox.Ok)

    def edit(self):
        try:
            if self.select != "":
                className = self.lineEdit_2.text()
                if self.comboBox.currentText() != "":
                    result = service.query('select gradeID from tb_grade where gradeName = %s',
                                           self.comboBox.currentText())
                    if len(result) > 0:
                        gradeID = result[0]
                        if className != "":
                            if self.getName(gradeID, className) > 0:
                                self.lineEdit_2.setText("")
                                QMessageBox.information(None, '提示', '您要修改的班级已存在！请重新输入',
                                                        QMessageBox.Ok)
                            else:
                               result = service.exec('update tb_class set gradeID=%s , className=%s where classID = %s',
                                                     (gradeID, className, self.select))# 这三个数值的逗号是一定要打，
                                                                                       # 不然会错误
                               if result > 0:
                                   self.query()
                                   self.lineEdit_2.setText("")
                                   QMessageBox.information(None, '提示', '信息修改成功', QMessageBox.Ok)
                               else:
                                   QMessageBox.information(None, '提示', '修改不成功', QMessageBox.Ok)
                        else:
                            QMessageBox.warning(None, '警告', '请输入要修改的内容', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要修改的数据', QMessageBox.Ok)
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')

    def delete(self):
        try:
            if self.select != '':
                result = service.exec('delete from tb_class where classID = %s', self.select)
                if result > 0:
                    QMessageBox.information(None, '提示', '信息删除成功', QMessageBox.Ok)
                    self.lineEdit.setText('')
                    self.query()
        except:
            QMessageBox.warning(None, '警告', '请选择要删除的数据', QMessageBox.Ok)
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
