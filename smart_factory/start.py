import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QDialog
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

numpadForm = resource_path('numpad.ui')
numpadUi = uic.loadUiType(numpadForm)[0]

class HomeWindow(QMainWindow, homeUi):
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
        
    def btnNumpadClicked(self):
        targetButton = self.sender()
        showNumpadDialog(self, targetButton)

class AdminWindow(QMainWindow, adminUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btnHomeClicked(self):
        main_widget.setCurrentIndex(0)

class NumpadWindow(QDialog, numpadUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

# 메인 윈도우 또는 다른 위젯에서 NumpadWindow를 띄우는 메서드
def showNumpadDialog(self, targetButton):
    result = "0"
    numpadDialog = NumpadWindow()
    if numpadDialog.exec_() == QDialog.Accepted:
        result = numpadDialog.getResult()
        targetButton.setText(result)
        print(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_widget = QStackedWidget()

    home = HomeWindow()
    main = MainWindow()
    admin = AdminWindow()
    # numpad = NumpadWindow()

    main_widget.addWidget(home)
    main_widget.addWidget(main)
    main_widget.addWidget(admin)
    # main_widget.addWidget(numpad)

    main_widget.setCurrentIndex(0)  # 시작 시 Home 윈도우를 먼저 보여줌
    main_widget.show()

    sys.exit(app.exec_())
