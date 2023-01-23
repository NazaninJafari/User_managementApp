from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6 import QtGui
from functools import partial
import database
from take_picture import Camera


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('gestion_utilisateurs.ui', None)
        self.ui.show()       
         
        result = database.getAll()
        
        self.ui.add_Button.clicked.connect(self.add)
        self.ui.show_Button.clicked.connect(self.show_data)
        self.ui.change_Button.clicked.connect(self.change_data)
        self.ui.label.setStyleSheet('background-image:url(others/bg_image.png)')
    
    def add(self):
        self.new_window = Add()
        result = database.getAll()

    def show_data(self):
        self.new_window2 = Show()
        result = database.getAll()
    
    def change_data(self):
        self.change_window3 = Change()

class Add(QWidget):
    def __init__(self):
        super(Add, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('users.ui')
        self.ui.show()

        self.ui.photo_Button.setIcon(QtGui.QIcon('others/camera.png'))
        self.ui.photo_Button.setIconSize(QSize(65, 65))

        self.ui.photo_Button.clicked.connect(self.camera)
        self.ui.save_Button.clicked.connect(self.addnewuser)
        self.ui.cancel_Button.clicked.connect(self.close_window)

    def addnewuser(self):
        name = self.ui.Name_lineEdit.text()
        family = self.ui.family_lineEdit.text()
        codeD = self.ui.codeD_lineEdit.text()
        Bdate = self.ui.DN_lineEdit.text()

        database.add(name, family , codeD, Bdate)

        self.ui.Name_lineEdit.setText('')  
        self.ui.family_lineEdit.setText('')    
        self.ui.codeD_lineEdit.setText('')
        self.ui.DN_lineEdit.setText('')

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Message')
        msg_box.setText('Il a été ajouté avec succès')
        msg_box.exec()        
        

    def camera(self):

        name = self.ui.Name_lineEdit.text()
        family = self.ui.family_lineEdit.text()
        codeD = self.ui.codeD_lineEdit.text()
        Bdate = self.ui.DN_lineEdit.text()

        if name=='' or family== '' or codeD=='' or Bdate=='':
            msg_box = QMessageBox()
            msg_box.setText('Error! remplisez tous les fileds svp!')
            msg_box.exec_()

        else:    
            self.pic = Camera(codeD)

    def close_window(self):
        self.ui.close()           

class Show(QWidget):
    def __init__(self):
        super(Show,self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('showData.ui')
        self.ui.show()

        result = database.getAll()
        for i in range(len(result)):
            name_lable = QLabel()
            name_lable.setStyleSheet('background-color: cadetblue')
            family_lable = QLabel()
            family_lable.setStyleSheet('background-color: cadetblue')
            pic_btn = QPushButton()

            name_lable.setText(result[i][0])
            family_lable.setText(result[i][1])
            pic_btn.setIcon(QtGui.QIcon(f"faces_image/{str(result[i][2])}.jpg"))
            pic_btn.setIconSize(QSize(65, 65))

            self.ui.gridLayout.addWidget(name_lable, i, 0)
            self.ui.gridLayout.addWidget(family_lable, i, 1)           
            self.ui.gridLayout.addWidget(pic_btn, i, 2)

class Change(QWidget):
    def __init__(self):
        super(Change, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('changeInfo.ui')
        self.ui.show()

        self.ui.name_lineEdit1.isReadOnly()
        self.ui.family_lineEdit1.isReadOnly()
        self.ui.icode_lineEdit1.isReadOnly()
        self.ui.dn_lineEdit1.isReadOnly()

        self.ui.search_Button.clicked.connect(self.search_info)
    
    def search_info(self):

        flag = 0
        code = self.ui.getcode_lineEdit.text()
        result = database.getAll()
        for i in range(len(result)):
            if str(code) == str(result[i][2]):
                flag = 1
                self.ui.name_lineEdit1.setText(result[i][0])
                self.ui.family_lineEdit1.setText(result[i][1])
                self.ui.icode_lineEdit1.setText(str(result[i][2]))
                self.ui.dn_lineEdit1.setText(result[i][3])

        if flag == 0:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Error!!')
            msg_box.setText(" N'existe pas! Veuillez saisir le code d'identification correct")
            msg_box.exec()        

        self.ui.savechange_Button.clicked.connect(self.savechange) 

    def savechange(self):

        name = self.ui.name_lineEdit1.text()
        family = self.ui.family_lineEdit1.text()
        codeD = self.ui.icode_lineEdit1.text()
        Bdate = self.ui.dn_lineEdit1.text()
        database.update_info(codeD,name,family,Bdate)

        self.ui.close()

app = QApplication([])
window = Main()
app.exec_()