from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from utils import resource_path

class HomeWindow(QDialog):
    def __init__(self, main_widget):
        super().__init__()
        uic.loadUi(resource_path('home.ui'), self)
        self.main_widget = main_widget

    def btnMainClicked(self):
        self.main_widget.setCurrentIndex(1)

    def btnAdminClicked(self):
        self.main_widget.setCurrentIndex(2)
