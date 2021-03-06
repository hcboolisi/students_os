# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
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

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 20, 87, 31))
        self.comboBox.setObjectName("comboBox")
        self.bindGrade()
        self.comboBox.currentIndexChanged.connect(self.bindClass)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(340, 20, 87, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.bindClass()
        # self.comboBox_2.currentIndexChanged.connect(self.query)  # 开启此功能可以取代刷新按钮

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 20, 60, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.query)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 20, 60, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 20, 60, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.edit)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 20, 60, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.delete)

        self.tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tablewidget.setGeometry(QtCore.QRect(5, 60, 790, 310))
        self.tablewidget.setObjectName("tableView")
        self.tablewidget.setShowGrid(True)
        self.tablewidget.setAlternatingRowColors(True)
        self.tablewidget.resizeColumnsToContents()
        self.tablewidget.resizeRowsToContents()
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablewidget.itemClicked.connect(self.getItem)
        self.query()

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 395, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 444, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 390, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 440, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 395, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(450, 390, 101, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 444, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 440, 291, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 395, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(610, 390, 61, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 395, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(726, 390, 61, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.bindSex()

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(730, 20, 60, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(MainWindow.close)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 390, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 440, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生信息管理"))
        self.label.setText(_translate("MainWindow", "所属年级："))
        self.label_2.setText(_translate("MainWindow", "所属班级:"))
        self.pushButton.setText(_translate("MainWindow", "刷 新"))
        self.pushButton_2.setText(_translate("MainWindow", "添 加"))
        self.pushButton_3.setText(_translate("MainWindow", "修 改"))
        self.pushButton_4.setText(_translate("MainWindow", "删 除"))
        self.label_4.setText(_translate("MainWindow", "学生编号："))
        self.label_5.setText(_translate("MainWindow", "联系电话："))
        self.label_6.setText(_translate("MainWindow", "学生姓名："))
        self.label_7.setText(_translate("MainWindow", "家庭地址："))
        self.label_8.setText(_translate("MainWindow", "年龄："))
        self.label_9.setText(_translate("MainWindow", "性别："))
        self.pushButton_5.setText(_translate("MainWindow", "退 出"))
        self.label_3.setText(_translate("MainWindow", "信 息"))
        self.label_10.setText(_translate("MainWindow", "设 置"))

    def bindGrade(self):
        self.comboBox.addItem("所有")
        result = service.query("select gradeName from tb_grade")
        for i in result:
            self.comboBox.addItem(i[0])

    def bindClass(self):
        self.comboBox_2.clear()
        self.comboBox_2.addItem("所有")
        result = service.query("select className from v_classinfo where gradeName = %s",
                               self.comboBox.currentText())
        for i in result:
            self.comboBox_2.addItem(i[0])

    def bindSex(self):
        self.comboBox_3.addItem("男")
        self.comboBox_3.addItem("女")

    def getID(self, ID):
        result = service.query("select * from tb_student where stuID = %s", ID)
        return len(result)

    def getItem(self, item):
        if item.column() == 0:
            self.select = item.text()
            self.lineEdit.setText(self.select)
            result = service.query(f"select * from v_studentinfo where stuID = {self.select}")
            self.lineEdit_3.setText(result[0][1])
            self.lineEdit_5.setText(str(result[0][2]))
            self.comboBox_3.setCurrentText(result[0][3])
            self.lineEdit_2.setText(result[0][4])
            self.lineEdit_4.setText(result[0][5])

    def query(self):
        self.tablewidget.setRowCount(0)  # 设置表格的行数为0行
        g_name = self.comboBox.currentText()
        c_name = self.comboBox_2.currentText()
        if g_name == "所有":
            result = service.query("select stuID,stuName,CONCAT(gradeName,className),\
                                   sex,age,address,phone from v_studentinfo")
        elif g_name != "所有" and c_name == "所有":
            result = service.query("select stuID,stuName,CONCAT(gradeName,className),\
                                   sex,age,address,phone from v_studentinfo \
                                   where gradeName = %s", g_name)
        elif g_name != "所有" and c_name != "所有":
            result = service.query("select stuID,stuName,CONCAT(gradeName,className),\
                                   sex,age,address,phone from v_studentinfo \
                                   where gradeName = %s and className = %s", g_name, c_name)
        self.tablewidget.setColumnCount(7)  # 设置表格的列数为7列
        # 设置表格的水平每列的数据内容名称
        self.tablewidget.setHorizontalHeaderLabels(["学生编号", "学生姓名", "班级",
                                                    "性别", "年龄", "家庭地址", "联系电话"])
        row = len(result)  # 查询到的数据库条数（每一行为一条），作为表格的总行数
        self.tablewidget.setRowCount(row)  # 设置表格的行数为查询到的表格当中的数据总条数
        for i in range(row):  # 先遍历行数，选定每一行，再遍历该行的每一列，然后添加数据
            for j in range(self.tablewidget.columnCount()):  # 再遍历列数
                date = QTableWidgetItem(str(result[i][j]))  # 创建一个数据（单元格）对象
                date.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 设置该数据的对齐方式
                self.tablewidget.setItem(i, j, date)  # 将每个数据添加到指定的每一个单元格内

    def add(self):
        stu_ID = self.lineEdit.text()
        stu_name = self.lineEdit_3.text()
        age = self.lineEdit_5.text()
        sex = self.comboBox_3.currentText()
        phone = self.lineEdit_2.text()
        address = self.lineEdit_4.text()
        if self.comboBox.currentText() != "" and self.comboBox.currentText() != "所有":
            result = service.query("select gradeID from tb_grade where gradeName = %s",
                                   self.comboBox.currentText())
            if len(result) > 0:
                grade_ID = result[0]
                if self.comboBox_2.currentText() != "" and self.comboBox_2.currentText() != "所有":
                    result = service.query("select classID from tb_class where gradeID = %s and\
                                           className = %s", grade_ID, self.comboBox_2.currentText())
                    if len(result) > 0:
                        class_ID = result[0]
                        if stu_ID != "" and stu_name != "":
                            if self.getID(stu_ID) > 0:
                                self.lineEdit.setText("")
                                self.lineEdit_3.setText("")
                                self.lineEdit_5.setText("")
                                self.lineEdit_2.setText("")
                                self.lineEdit_4.setText("")
                                QMessageBox.information(None, "提示", "您要添加的学生编号已存在，请重新输入！",
                                                        QMessageBox.Ok)
                            else:
                                result = service.exec("insert into tb_student(stuID,stuName,classID,gradeID,age,sex,\
                                                       phone,address) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                                                      (stu_ID, stu_name, class_ID, grade_ID, age, sex, phone, address))
                                if result > 0:
                                    self.query()
                                    self.lineEdit.setText("")
                                    self.lineEdit_3.setText("")
                                    self.lineEdit_5.setText("")
                                    self.lineEdit_2.setText("")
                                    self.lineEdit_4.setText("")
                                    QMessageBox.information(None, "提示", "信息添加成功！", QMessageBox.Ok)
                        else:
                            QMessageBox.warning(None, "警告", "请输入数据后，再执行操作！", QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, "警告", "请先添加班级！", QMessageBox.Ok)
        else:
            QMessageBox.warning(None, "警告", "请先添加年级！", QMessageBox.Ok)

    def edit(self):
        try:
            if self.select != "":
                stu_ID = self.select
                stu_name = self.lineEdit_3.text()
                age = self.lineEdit_5.text()
                sex = self.comboBox_3.currentText()
                phone = self.lineEdit_2.text()
                address = self.lineEdit_4.text()
                result = service.exec("update tb_student set age=%s,sex=%s,phone=%s,address=%s,\
                                      stuName=%s where stuID=%s", (age, sex, phone, address, stu_name, stu_ID))
                if result > 0:
                    self.query()
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit_4.setText("")
                    QMessageBox.information(None, "提示", "信息修改成功！", QMessageBox.Ok)
        except:
            QMessageBox.warning(None, "警告", "请先选择要修改的数据！", QMessageBox.Ok)

    def delete(self):
        try:
            if self.select != "":
                result = service.exec("delete from tb_student where stuID =%s", self.select)
                if result > 0:
                    self.query()
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_2.setText("")
                    self.lineEdit_4.setText("")
                    QMessageBox.information(None, "提示", "信息删除成功！", QMessageBox.Ok)
        except:
            QMessageBox.warning(None, "警告", "请先选择你要删除的数据！", QMessageBox.Ok)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
