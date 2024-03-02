import sys, glob, os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5 import uic

class MyForm(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = uic.loadUi("convert.ui", self)
        self.lineEdit_1.setEnabled(False)
        self.lineEdit_1.setPlaceholderText('pattern for files')
        self.sourcefolder = None
        self.sourcefile = None
        self.ui.show()
        
    def select_sourcefolder(self): 
        self.sourcefolder = QFileDialog.getExistingDirectory() + '/'
        self.label_1.setText(self.sourcefolder)
        self.lineEdit_1.setEnabled(True)
        self.showFileList()
    def showFileList(self):
        if self.sourcefile == None:
            current = self.sourcefolder + '/*'
        else:
            current = self.sourcefile            
        self.listWidget.clear()
        for x in glob.glob(current):
            self.listWidget.addItem(os.path.basename(x))                       
    def setSourceFile(self): 
        self.sourcefile = self.sourcefolder + self.lineEdit_1.text()
        self.label_1.setText(self.sourcefile)
        self.showFileList()
    def selectitem(self, item): 
        self.label_1.setText(self.sourcefolder + item.text())
    def finish(): sys.exit()

app = QApplication(sys.argv)
w = MyForm()
sys.exit(app.exec())
