from calculator import Calculator
from PyQt5 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
UI_Calculator = QtWidgets.QMainWindow()
UI_Calculator.setWindowIcon(QtGui.QIcon("calculator-icon.png"))
ui = Calculator()
ui.setupUi(UI_Calculator)
UI_Calculator.show()
sys.exit(app.exec_())
