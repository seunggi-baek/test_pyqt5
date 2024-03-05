from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from utils import resource_path

class AdminWindow(QDialog):
    def __init__(self, main_widget):
        super().__init__()
        uic.loadUi(resource_path('admin.ui'), self)
        self.main_widget = main_widget

    def btnHomeClicked(self):
        self.main_widget.setCurrentIndex(0)
