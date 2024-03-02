import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic

class MyForm(QDialog):
    def __init__(self, parent=None):
        #QDialog.__init__(self, parent)
        super().__init__(parent)
        # loadUi 함수에 slot_save와 같은 시그널 함수를 사용하기 위해서
        # self 매개변수를 필수로 적어주지 않으면 오류발생
        self.ui = uic.loadUi('input.ui', self)
        self.ui.label.setText('input data! and click "Save"')
        self.ui.show()
        
    def slot_save(self): 
        msg = self.ui.lineEdit.text()
        # wt : 새로만들기, at : 기존파일에 추가
        with open('data.txt', 'at') as f:
            f.write(msg + '\n')
        self.ui.label.setText('Saved input data')
        self.ui.lineEdit.setText("")
    def slot_clear(self): 
        self.ui.label.setText("Clear input data")
        self.ui.lineEdit.setText("")
    def slot_exit(self): 
        print("Bye~")
        sys.exit()
    
        
app = QApplication(sys.argv)
w = MyForm()
sys.exit(app.exec())
