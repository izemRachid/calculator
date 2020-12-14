import sys
from PyQt5 import QtCore,QtWidgets,QtGui
from main import Ui_MainWindow
import math


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
trigger=True #to check if you start a new calculation ad to avoid writing in the same space

#_______________________________buttons_______________________________
def zero():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"0")
    if not trigger:
        ui.lineEdit.setText("0")
    trigger=True

def one():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"1")
    if not trigger:
        ui.lineEdit.setText("1")
    trigger=True
def two():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"2")
    if not trigger:
        ui.lineEdit.setText("2")
    trigger=True
def three():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"3")
    if not trigger:
        ui.lineEdit.setText("3")
    trigger=True
def four():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"4")
    if not trigger:
        ui.lineEdit.setText("4")
    trigger=True
def five():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"5")
    if not trigger:
        ui.lineEdit.setText("5")
    trigger=True
def six():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"6")
    if not trigger:
        ui.lineEdit.setText("6")
    trigger=True
def seven():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"7")
    if not trigger:
        ui.lineEdit.setText("7")
    trigger=True
def eight():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"8")
    if not trigger:
        ui.lineEdit.setText("8")
    trigger=True
def nine():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"9")
    if not trigger:
        ui.lineEdit.setText("9")
    trigger=True
def point():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+".")
    if not trigger:
        ui.lineEdit.setText(".")
    trigger=True
def left_bracket():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"(")
    if not trigger:
        ui.lineEdit.setText("(")
    trigger=True
def right_bracket():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+")")
    if not trigger:
        ui.lineEdit.setText(")")
    trigger=True
def addition():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"+")
    if not trigger:
        ui.lineEdit.setText("+")
    trigger=True
def multiplication():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"*")
    if not trigger:
        ui.lineEdit.setText("*")
    trigger=True
def division():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"/")
    if not trigger:
        ui.lineEdit.setText("/")
    trigger=True
def minus():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"-")
    if not trigger:
        ui.lineEdit.setText("-")
    trigger=True
def percent():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"%")
    if not trigger:
        ui.lineEdit.setText("%")
    trigger=True
def log():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"math.log10(")
    if not trigger:
        ui.lineEdit.setText("math.log10(")
    trigger=True
def ln():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text() + "math.ln(")
    if not trigger:
        ui.lineEdit.setText("math.ln(")
    trigger = True
def cos():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"math.cos(")
    if not trigger:
        ui.lineEdit.setText("math.cos(")
    trigger=True
def sin():
    global trigger
    if trigger:
       ui.lineEdit.setText(ui.lineEdit.text()+"math.sin(")
    if not trigger:
        ui.lineEdit.setText("math.sin(")
    trigger=True
def puissance():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"**")
    if not trigger:
        ui.lineEdit.setText("**")
    trigger=True
def tan():
    math.tan()
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"math.tan(")
    if not trigger:
        ui.lineEdit.setText("math.tan(")
    trigger=True
def exp():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"math.exp(")
    if not trigger:
        ui.lineEdit.setText("math.exp(")
    trigger=True
def root():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"math.sqrt(")
    if not trigger:
        ui.lineEdit.setText("math.sqrt(")
    trigger=True

def factoriel():
    global trigger
    if trigger:
        ui.lineEdit.setText(ui.lineEdit.text()+"math.factorial(")
    if not trigger:
        ui.lineEdit.setText("math.factorial(")
    trigger=True
def delete():
    ui.lineEdit.setText(ui.lineEdit.text()[0:-1])
#################################--evaluation--######################################
def equal():
    global trigger
    ui.lineEdit.setText(str(eval(ui.lineEdit.text())))
    trigger =False
######################################################################################
def clear():
    ui.lineEdit.setText("")


#connections
ui.clear_butt.clicked.connect(clear)
ui.butt_0.clicked.connect(zero)
ui.butt_1.clicked.connect(one)
ui.butt_2.clicked.connect(two)
ui.butt_3.clicked.connect(three)
ui.butt_4.clicked.connect(four)
ui.butt_5.clicked.connect(five)
ui.butt_6.clicked.connect(six)
ui.butt_7.clicked.connect(seven)
ui.butt_8.clicked.connect(eight)
ui.butt_9.clicked.connect(nine)
ui.point_butt.clicked.connect(point)
ui.paren_1.clicked.connect(left_bracket)
ui.paren_2.clicked.connect(right_bracket)
ui.ln_butt.clicked.connect(ln)
ui.log_butt.clicked.connect(log)
ui.racine.clicked.connect(root)
ui.tan_butt.clicked.connect(tan)
ui.sin_butt.clicked.connect(sin)
ui.cos_butt.clicked.connect(cos)
ui.tan_butt.clicked.connect(eight)
ui.exp_butt.clicked.connect(exp)
ui.factoriel_butt.clicked.connect(factoriel)
ui.plus_butt.clicked.connect(addition)
ui.minu_butt.clicked.connect(minus)
ui.percentage_butt.clicked.connect(percent)
ui.multipl_butt.clicked.connect(multiplication)
ui.divise_butt.clicked.connect(division)
ui.pushButton_38.clicked.connect(delete)
ui.equal_butt.clicked.connect(equal)
ui.exp_butt_2.clicked.connect(puissance)




























sys.exit(app.exec_())
