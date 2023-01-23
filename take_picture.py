import cv2
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import QPixmap,QImage
from PySide6 import QtGui

class Camera(QWidget):
    def __init__(self, id):
        super(Camera, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('takepic.ui')
        self.ui.show()

        self.id = id
        
        self.ui.filter1_btn.clicked.connect(partial(self.take_pic, 1)) #1
        self.ui.filter1_btn.setIcon(QtGui.QIcon('others/camera.png'))
        self.ui.filter2_btn.clicked.connect(partial(self.take_pic, 2)) #2
        self.ui.filter2_btn.setIcon(QtGui.QIcon('others/camera.png'))
        self.ui.filter3_btn.clicked.connect(partial(self.take_pic, 3)) #3
        self.ui.filter3_btn.setIcon(QtGui.QIcon('others/camera.png'))
        self.ui.filter4_btn.clicked.connect(partial(self.take_pic, 4)) #4
        self.ui.filter4_btn.setIcon(QtGui.QIcon('others/camera.png'))
        self.ui.filter5_btn.clicked.connect(partial(self.take_pic, 5)) #5
        self.ui.filter5_btn.setIcon(QtGui.QIcon('others/camera.png'))
        self.ui.filter6_btn.clicked.connect(partial(self.take_pic, 6)) #6
        self.ui.filter6_btn.setIcon(QtGui.QIcon('others/camera.png'))
        self.ui.filter7_btn.clicked.connect(partial(self.take_pic, 7)) #7
        self.ui.filter7_btn.setIcon(QtGui.QIcon('others/camera.png'))
        self.ui.filter8_btn.clicked.connect(partial(self.take_pic, 8)) #8
        self.ui.filter8_btn.setIcon(QtGui.QIcon('others/camera.png'))
        self.ui.filter9_btn.clicked.connect(partial(self.take_pic, 9)) #9
        self.ui.filter9_btn.setIcon(QtGui.QIcon('others/camera.png'))

        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        camera = cv2.VideoCapture(0)

        while True:
            
            ret , self.frame = camera.read()
            if not ret:
                break
            
            self.frame = cv2.resize(self.frame, (180,180))

            faces = face_detector.detectMultiScale(self.frame, 1.3)
            for x,y,w,h in faces:
                rect_face = self.frame[y:y+h , x:x+w]
                self.pointy = y
                self.pointx = x
                self.w = w
                self.h = h  

            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            blure_frame = Filters(self.frame).blur()
            img1 = QImage(blure_frame, blure_frame.shape[1], blure_frame.shape[0], QImage.Format_RGB888)
            pixmap1 = QPixmap.fromImage(img1)
            self.ui.label_blurfiltre.setPixmap(pixmap1)

            flip_frame = Filters(self.frame).flip()
            img2 = QImage(flip_frame, flip_frame.shape[1], flip_frame.shape[0], QImage.Format_RGB888)
            pixmap2 = QPixmap.fromImage(img2)
            self.ui.label_flipfiltre.setPixmap(pixmap2)

            pink_frame = Filters(self.frame).pink()
            img3 = QImage(pink_frame, pink_frame.shape[1], pink_frame.shape[0], QImage.Format_RGB888)
            pixmap3 = QPixmap.fromImage(img3)
            self.ui.label_pinkfiltre.setPixmap(pixmap3)

            spring_frame = Filters(self.frame).spring()
            img4 = QImage(spring_frame, spring_frame.shape[1], spring_frame.shape[0], QImage.Format_RGB888)
            pixmap4 = QPixmap.fromImage(img4)
            self.ui.label_springfiltre.setPixmap(pixmap4)

            cool_frame = Filters(self.frame).cool()
            img5 = QImage(cool_frame, cool_frame.shape[1], cool_frame.shape[0], QImage.Format_RGB888)
            pixmap5 = QPixmap.fromImage(img5)
            self.ui.label_coolfiltre.setPixmap(pixmap5)

            hot_frame = Filters(self.frame).hot()
            img6 = QImage(hot_frame, hot_frame.shape[1], hot_frame.shape[0], QImage.Format_RGB888)
            pixmap6 = QPixmap.fromImage(img6)
            self.ui.label_hotfiltre.setPixmap(pixmap6)

            ocean_frame = Filters(self.frame).ocean()
            img7 = QImage(ocean_frame, ocean_frame.shape[1], ocean_frame.shape[0], QImage.Format_RGB888)
            pixmap7 = QPixmap.fromImage(img7)
            self.ui.label_oceanfiltre.setPixmap(pixmap7)

            summer_frame = Filters(self.frame).summer()
            img8 = QImage(summer_frame, summer_frame.shape[1], summer_frame.shape[0], QImage.Format_RGB888)
            pixmap8 = QPixmap.fromImage(img8)
            self.ui.label_summerfiltre.setPixmap(pixmap8)

            turbo_frame = Filters(self.frame).turbo()
            img9 = QImage(turbo_frame, turbo_frame.shape[1], turbo_frame.shape[0], QImage.Format_RGB888)
            pixmap9 = QPixmap.fromImage(img9)
            self.ui.label_turbofiltre.setPixmap(pixmap9)  

            key = cv2.waitKey(1)
            if key == 27: #Esc
                break

            cv2.waitKey(1)     
    
    def take_pic(self,num):
                
        if num == 1:
            self.image = Filters(self.frame).blur()
                
        elif num == 2:
            self.image = Filters(self.frame).flip()

        elif num == 3:
            self.image = Filters(self.frame).pink()

        elif num == 4:
            self.image = Filters(self.frame).spring()

        elif num == 5:
            self.image = Filters(self.frame).cool()

        elif num == 6:
            self.image = Filters(self.frame).hot()
        
        elif num == 7:
            self.image = Filters(self.frame).ocean()

        elif num == 8:
            self.image = Filters(self.frame).summer()

        elif num == 9:
            self.image = Filters(self.frame).turbo()    

        #save face_image
        cv2.imwrite(f'faces_image/{str(self.id)}.jpg', self.image[self.pointy : self.pointy+self.h , self.pointx : self.pointx+self.w])

        msg_box = QMessageBox()
        msg_box.setWindowTitle('Message')
        msg_box.setText('photo a été ajouté avec succès')
        msg_box.exec()

        #self.ui.close()
 

class Filters():
    def __init__(self,frame):
        self.frame = frame

    def blur(self):
        blur_frame = cv2.blur(self.frame, (5, 5)) 
        return blur_frame

    def flip(self):
        flip_frame = cv2.flip(self.frame, 0)  
        return flip_frame

    def pink(self):
        pink_frame = cv2.applyColorMap(self.frame, cv2.COLORMAP_PINK)
        return pink_frame        

    def spring(self):
        spring_frame = cv2.applyColorMap(self.frame, cv2.COLORMAP_SPRING) 
        return spring_frame           

    def cool(self):
        cool_frame = cv2.applyColorMap(self.frame, cv2.COLORMAP_COOL) 
        return cool_frame


    def hot(self):
        hot_frame = cv2.applyColorMap(self.frame, cv2.COLORMAP_HOT) 
        return hot_frame

    def ocean(self):
        ocean_frame = cv2.applyColorMap(self.frame, cv2.COLORMAP_OCEAN)
        return ocean_frame

    def summer(self): 
        summer_frame = cv2.applyColorMap(self.frame, cv2.COLORMAP_SUMMER)
        return summer_frame


    def turbo(self):
        turbo_frame = cv2.applyColorMap(self.frame, cv2.COLORMAP_TURBO)
        return turbo_frame