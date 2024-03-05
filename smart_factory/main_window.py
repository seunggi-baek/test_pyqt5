from PyQt5.QtWidgets import QDialog
from numpad_window import NumpadWindow
from PyQt5 import uic
from utils import resource_path

class MainWindow(QDialog):
    def __init__(self, main_widget):
        super().__init__()
        uic.loadUi(resource_path('main.ui'), self)
        self.main_widget = main_widget

    def btnHomeClicked(self):
        self.main_widget.setCurrentIndex(0)

    def btnAdminClicked(self):
        self.main_widget.setCurrentIndex(2)
        
    def btnNumpadClicked(self):
        targetButton = self.sender()
        NumpadWindow.showNumpadDialog(self, targetButton)
