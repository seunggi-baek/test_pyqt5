import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5 import uic, QtCore
import shelve, re

class MyForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("membership.ui", self)
        
        self.userInput = {
            'name': self.lineEdit_name,
            'id': self.lineEdit_id,
            'pw1': self.lineEdit_pw1,
            'pw2': self.lineEdit_pw2            
        } # iteration
        self.lenInfo = {
            'name': {'minLen':2, 'maxLen':20},
            'id': {'minLen':3, 'maxLen':20},
            'pw1': {'minLen':8, 'maxLen':20},
        }
        self.errMsg = {
            'title': '오류메세지',
            'name': f"이름길이 {self.lenInfo['name']['minLen']} ~ {self.lenInfo['name']['maxLen']}글자",
            'id': f"이름길이 {self.lenInfo['id']['minLen']} ~ {self.lenInfo['id']['maxLen']}글자",
            'pw1': f"이름길이 {self.lenInfo['pw1']['minLen']} ~ {self.lenInfo['pw1']['maxLen']}글자",
            'id_dup': '아이디가 존재함',
            'pw13c': '패스워드 숫자/영문자/특수문자 모두 포함',
            'pw2': '처음 입력한 암호와 다름'
        }
        self.infoMsg = {
            'title': '상태 메세지',
            'success': '회원 가입 완료'
        }
        
        # 버튼 포커싱 비활성화 처리
        #self.ui.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        
        # Enter 입력시 포커싱 이동 (직접 객체 지정, 포커싱 인덱스, iteration 이용)
        for x in self.userInput.values():
            x.returnPressed.connect(self.focusNextChild)

        self.init_object()            
        # with shelve.open('members') as data:
        #     data['imbgirl'] = {
        #         'name':'Julie Yoon',
        #         'id': 'imbgirl',
        #         'pw1': 'abc123**',
        #         'pw2': 'abc123**'
        #     }
        #     print(data['imbgirl'])
        
        #self.lineEdit_name.returnPressed.connect(self.lineEdit_id.setFocus)
        #self.lineEdit_name.returnPressed.connect(self.focusNextChild)
        #self.lineEdit_id.returnPressed.connect(self.focusNextChild)
        #self.lineEdit_pw1.returnPressed.connect(self.focusNextChild)
        #self.lineEdit_pw2.returnPressed.connect(self.focusNextChild)
        
        self.ui.show()
    
    def init_object(self):
        for x in self.userInput.values():
            x.setText("")
        self.currInfo = dict.fromkeys(('name', 'id', 'pw1', 'pw2'), None)
        self.newMember = dict.fromkeys(('name', 'id', 'pw1', 'pw2'), None)
        self.ui.pushButton.setEnabled(False)

    def check_twice_enter(self, target):
        print(target)
        value = self.userInput[target].text()
        if len(value) == 0 or value == self.currInfo[target] : return None
        print(target + ' step2')
        self.currInfo[target] = value
        return value
    def show_errMessage(self, target, errmsg):
        QMessageBox.critical(self, self.errMsg['title'], errmsg)
        self.newMember[target] = None
        self.userInput[target].setFocus()
        if target == 'pw2':
            self.userInput[target].setText("")
    def check_length(self, target, value):
        if len(value) >= self.lenInfo[target]['minLen'] and \
           len(value) <= self.lenInfo[target]['maxLen']:
               self.newMember[target] = value
        else:
            self.show_errMessage(target, self.errMsg[target])
        
        
    def slot_checkName(self): 
        target = 'name'
        value =  self.check_twice_enter(target)
        if value == None: return
        self.check_length(target, value)
        self.pushButton.setEnabled(None not in self.newMember.values()) # 비정상 - None
    def slot_checkId(self):
        target = 'id'
        value =  self.check_twice_enter(target)
        if value == None: return
        with shelve.open('members') as data:
            try: # 중복 아이디 있음
                temp = data[value]
                self.show_errMessage(target, self.errMsg['id_dup'])
            except: # 중복 아이디 없음
                #import traceback
                #print(traceback.format_exc())
                self.check_length(target, value)
        self.pushButton.setEnabled(None not in self.newMember.values())
    def slot_checkPw1(self):
        target = 'pw1'
        value =  self.check_twice_enter(target)
        if value == None: return
        if re.search(r'[0-9]', value) and re.search(r'[a-zA-Z]', value) and re.search(r'[!@#$%^&*()_+]', value):
            self.check_length(target, value)
        else:
            self.show_errMessage(target, self.errMsg['pw13c'])
        self.pushButton.setEnabled(None not in self.newMember.values())
    def slot_checkPw2(self):
        target = 'pw2'
        value =  self.check_twice_enter(target)
        if value == None: return
        if self.newMember['pw1'] == value:
            self.newMember[target] = value
        else:
            self.show_errMessage(target, self.errMsg[target])
        self.pushButton.setEnabled(None not in self.newMember.values())
    def slot_membership(self): 
        print(self.newMember)
        if self.newMember['pw1'] == self.newMember['pw2']:
            with shelve.open('members') as data:
                data[self.newMember['id']] = self.newMember
            self.init_object()
            QMessageBox.information(self, self.infoMsg['title'], self.infoMsg['success'])
        else:
            self.show_errMessage('pw2', self.errMsg['pw2'])
    
app = QApplication(sys.argv)
w = MyForm()
sys.exit(app.exec())    