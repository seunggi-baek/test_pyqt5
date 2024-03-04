import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

homeForm = resource_path('home.ui')
homeUi = uic.loadUiType(homeForm)[0]

mainForm = resource_path('main.ui')
mainUi = uic.loadUiType(mainForm)[0]

adminForm = resource_path('admin.ui')
adminUi = uic.loadUiType(adminForm)[0]

class HomeWindow(QWidget, homeUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btnMainClicked(self):
        main_widget.setCurrentIndex(1)

    def btnAdminClicked(self):
        main_widget.setCurrentIndex(2)  # Admin 윈도우로 이동

class MainWindow(QMainWindow, mainUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btnHomeClicked(self):
        main_widget.setCurrentIndex(0)
    def btnAdminClicked(self):
        main_widget.setCurrentIndex(2)

class AdminWindow(QMainWindow, adminUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btnHomeClicked(self):
        main_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_widget = QStackedWidget()

    home = HomeWindow()
    main = MainWindow()
    admin = AdminWindow()

    main_widget.addWidget(home)
    main_widget.addWidget(main)
    main_widget.addWidget(admin)

    main_widget.setCurrentIndex(0)  # 시작 시 Home 윈도우를 먼저 보여줌
    main_widget.show()

    sys.exit(app.exec_())
