"""Funny little calculator go bRrRrrr"""

"""Funny Calc is a funny calc"""

import sys

#import cool thing
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

#do cool thing again
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from functools import partial


__verion__ = "0.1"
__author__ = "Max"

#create cool subclass
class funnicalcUi(QMainWindow):
    """Funni Calc view (GUI)"""
    def __init__(self):
        """view initilaixidrjwerreiu"""
        super().__init__()
        #set some windows stuff
        self.setWindowTitle("Funni Calc")
        self.setFixedSize(500, 500)
        #set the central thing
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget((self._centralWidget))
        self._centralWidget.setLayout(self.generalLayout)
        #Create and display button
        self._createDisplay()
        self._createButtons()
    def _createDisplay(self):
        """Create displayyyy"""
        #create display
        self.display = QLineEdit()
        # Set some display's props
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        #valid
        #add ddddisplay
        self.generalLayout.addWidget(self.display)
    def _createButtons(self):
        """Buttons exist"""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        #Button text position
        buttons = {
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
            "/": (0, 3),
            "C": (0, 4),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "*": (1, 3),
            "(": (1, 4),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "-": (2, 3),
            ")": (2, 4),
            "0": (3, 0),
            "00": (3, 1),
            ".": (3, 2),
            "+": (3, 3),
            "=": (3, 4),
        }
        #Create buttons and add them to cool grid ;layoutn3tijweruigeru
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        #Add ButtonsLaout to the general Layout
        self.generalLayout.addLayout(buttonsLayout)
    def setDisplayText(self, text):
        """set display's text ting"""
        self.display.setText(text)
        self.display.setFocus()
    def displayText(self):
        """Get display's text."""
        return self.display.text()
    def clearDisplay(self):
        """Clearrrrrrrrrrrrrrrrrr"""
        self.setDisplayText("")

class FunniCalcCtrl:
    """CONTROL EVERYTHING"""
    def __init__(self, model, view):
        """Control initializer"""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()
    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build Expression"""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots"""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons["C"].clicked.connect(self._view.clearDisplay)

ERROR_MSG = "ERROR GET GOOD AT MATHS"

#create a Model to handle calc op
def evaluateExpression(expression):
    """Evaluate an expression"""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result

#Client Code
def main():
    """main func thing"""
    # Create cool instance
    funnicalc = QApplication(sys.argv)
    #Show calc gui ting
    view = funnicalcUi()
    view.show()
    #create instances of teh model and teh controler
    model = evaluateExpression
    FunniCalcCtrl(model=model, view=view)
    #Execute the calculators main loooooooooooooop
    sys.exit(funnicalc.exec_())



if __name__ == "__main__":
    main()
