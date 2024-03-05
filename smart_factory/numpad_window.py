from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from utils import resource_path

class NumpadWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path('numpad.ui'), self)
        self.result = ""
        
    def btnNumberClicked(self):
        if len(self.result) < 5:
            self.result += self.sender().text()
            self.lcdNumber.display(self.result)

    def btnDeleteClicked(self):
        self.result = ""
        self.lcdNumber.display("0")

    def btnEnterClicked(self):
        self.accept()

    def getResult(self):
        return self.result

    @staticmethod
    def showNumpadDialog(parent, targetButton):
        result = "0"
        numpadDialog = NumpadWindow()
        if numpadDialog.exec_() == QDialog.Accepted:
            result = numpadDialog.getResult()
            targetButton.setText(result)
            print(result)
