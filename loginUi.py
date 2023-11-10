from PyQt5 import QtCore, QtGui, QtWidgets
import sys , res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(947, 581)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(110, 60, 691, 500))
        self.widget.setStyleSheet("QPushButton#login_btn, #reg_btn, #switch_btn{\n"
"    background-color: #008689; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; transition: background-color 0.3s ease-in-out;\n"
"}\n"
"\n"
"QPushButton#login_btn:hover, #reg_btn:hover, #switch_btn:hover{\n"
"    background-color: #00656b;\n"
"}\n"
"\n"
"QPushButton#login_btn:pressed, #reg_btn:pressed, #switch_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("background-image: url(:/images/login-bg.png);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 30);\n"
"border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 350, 430))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 230, 130))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(50, 80, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_7.setObjectName("label_7")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(300, 70, 320, 315))
        self.widget_3.setObjectName("widget_3")
        self.register_2 = QtWidgets.QLabel(self.widget_3)
        self.register_2.setGeometry(QtCore.QRect(40, 10, 145, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.register_2.setObjectName("register_2")
        self.userName_reg = QtWidgets.QLineEdit(self.widget_3)
        self.userName_reg.setGeometry(QtCore.QRect(40, 110, 225, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userName_reg.setFont(font)
        self.userName_reg.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.userName_reg.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.userName_reg.setObjectName("userName_reg")
        self.firstName = QtWidgets.QLineEdit(self.widget_3)
        self.firstName.setGeometry(QtCore.QRect(40, 60, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstName.setFont(font)
        self.firstName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.firstName.setObjectName("firstName")
        self.reg_btn = QtWidgets.QPushButton(self.widget_3)
        self.reg_btn.setGeometry(QtCore.QRect(40, 270, 225, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.reg_btn.setFont(font)
        self.reg_btn.setObjectName("reg_btn")
        self.lastName = QtWidgets.QLineEdit(self.widget_3)
        self.lastName.setGeometry(QtCore.QRect(165, 60, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lastName.setFont(font)
        self.lastName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lastName.setObjectName("lastName")
        self.password_reg = QtWidgets.QLineEdit(self.widget_3)
        self.password_reg.setGeometry(QtCore.QRect(40, 160, 225, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_reg.setFont(font)
        self.password_reg.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.password_reg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_reg.setObjectName("password_reg")
        self.cf_password = QtWidgets.QLineEdit(self.widget_3)
        self.cf_password.setGeometry(QtCore.QRect(40, 210, 225, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cf_password.setFont(font)
        self.cf_password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.cf_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cf_password.setObjectName("cf_password")
        self.switch_btn = QtWidgets.QPushButton(self.widget)
        self.switch_btn.setGeometry(QtCore.QRect(270, 80, 30, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.switch_btn.setFont(font)
        self.switch_btn.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.switch_btn.setCheckable(True)
        self.switch_btn.setObjectName("switch_btn")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(50, 107, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_8.setObjectName("label_8")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(300, 70, 320, 315))
        self.widget_2.setObjectName("widget_2")
        self.login = QtWidgets.QLabel(self.widget_2)
        self.login.setGeometry(QtCore.QRect(40, 10, 145, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.widget_2)
        self.password.setGeometry(QtCore.QRect(40, 127, 225, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.userName = QtWidgets.QLineEdit(self.widget_2)
        self.userName.setGeometry(QtCore.QRect(40, 80, 225, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userName.setFont(font)
        self.userName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.userName.setObjectName("userName")
        self.login_btn = QtWidgets.QPushButton(self.widget_2)
        self.login_btn.setGeometry(QtCore.QRect(40, 225, 225, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("")
        self.login_btn.setObjectName("login_btn")
        self.exit_btn = QtWidgets.QPushButton(self.widget)
        self.exit_btn.setGeometry(QtCore.QRect(590, 30, 30, 30))
        self.exit_btn.setStyleSheet("border  : none;\n"
"font-size: 16px;\n"
"color: black;\n"
"cursor: pointer;\n"
"transition: transform 0.2s;\n"
"font-weight: bold;\n"
"\n"
"")
        self.exit_btn.setObjectName("exit_btn")
        self.minimized_btn = QtWidgets.QPushButton(self.widget)
        self.minimized_btn.setGeometry(QtCore.QRect(560, 30, 30, 30))
        self.minimized_btn.setStyleSheet("border  : none;\n"
"font-size: 16px;\n"
"color: black;\n"
"cursor: pointer;\n"
"transition: transform 0.2s;\n"
"font-weight: bold;")
        self.minimized_btn.setObjectName("minimized_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "Student"))
        self.register_2.setText(_translate("Form", "Register"))
        self.userName_reg.setPlaceholderText(_translate("Form", " User Name"))
        self.firstName.setPlaceholderText(_translate("Form", " First Name"))
        self.reg_btn.setText(_translate("Form", "R e g i s t e r"))
        self.lastName.setPlaceholderText(_translate("Form", " Last Name"))
        self.password_reg.setPlaceholderText(_translate("Form", " Password"))
        self.cf_password.setPlaceholderText(_translate("Form", " Confirm Password"))
        self.switch_btn.setText(_translate("Form", "》"))
        self.label_8.setText(_translate("Form", "Management System"))
        self.login.setText(_translate("Form", "Log In"))
        self.password.setPlaceholderText(_translate("Form", "  Password"))
        self.userName.setPlaceholderText(_translate("Form", "  User Name"))
        self.login_btn.setText(_translate("Form", "L o g  I n"))
        self.exit_btn.setText(_translate("Form", "⨉"))
        self.minimized_btn.setText(_translate("Form", "─"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
