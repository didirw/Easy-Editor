#создай тут фоторедактор Easy Editor!
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,QWidget,QRadioButton,
    QLabel,QVBoxLayout,QHBoxLayout,QMessageBox,
    QGroupBox,QPushButton,QButtonGroup,QListWidget,QFileDialog
    )
import os
from PIL import Image,ImageOps,ImageFilter
from PyQt5.QtGui import QPixmap
workdir = ''

class ImageProcessor():
    def __init__ (self):
        self.filename = None
        self.Image = None
        self.dir = None
        self.save_dir = 'Modified/'



    def loadImage(self,filename):
        self.filename =filename
        self.dir =workdir
        image_path  =os.path.join(self.dir,self.filename)
        self.image =Image.open(image_path)
    def showImage(self,path):
        pixmapimage = QPixmap(path) 
        label_width, label_height= bth_foto.width(), bth_foto.height() 
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        bth_foto.setPixmap(scaled_pixmap) 
        bth_foto.setVisible(True)
        
    def  save_Image(self):
        path =os.path.join(workdir,self.save_dir)
        if not (
            os.path.isdir(path)
        ):
            os.mkdir(path)
        image_path = os.path.join(path,self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = ImageOps.grayscale(self.image)
        self.save_Image()
        image_path = os.path.join(
            workdir,self.save_dir,self.filename
        )
        self.showImage(image_path)

    def left(self):
        self.image = self.image.rotate(270)
        self.save_Image()
        image_path = os.path.join(
            workdir,self.save_dir,self.filename
        )
        self.showImage(image_path)
    def right(self):
        self.image = self.image.rotate(90)
        self.save_Image()
        image_path = os.path.join(
            workdir,self.save_dir,self.filename
        )
        self.showImage(image_path)
    def miror(self):
        self.image = ImageOps.mirror(self.image)
        self.save_Image()
        image_path = os.path.join(
            workdir,self.save_dir,self.filename
        )
        self.showImage(image_path)
    def saharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_Image()
        image_path = os.path.join(
            workdir,self.save_dir,self.filename
        )
        self.showImage(image_path)

workimage = ImageProcessor()
def choseWorkdir():
    global workdir
    workdir ='a'
    workdir = QFileDialog.getExistingDirectory()
def filter(files,extensions):
    result =[]
    for filnname in files:
        for ext in extensions:
            if filnname.endswith(ext):
                result.append(filnname)
                break
    return result

def showFilenamesList():
    choseWorkdir()
    extensions = ['.png','.jpg','.jpeg','.gif','.bmp']
    files =os.listdir(workdir)
    files =filter(files,extensions)
    btn_list.clear()
    btn_list.addItems(files)


def ShowChosenImage():
    if btn_list.currentRow() >= 0:
        filename = btn_list.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir,filename)
        workimage.showImage(image_path)




app =QApplication([])
window =QWidget()
window.resize(700,500)

l_1gh =QHBoxLayout()
l_2h =QHBoxLayout()
l_3v =QVBoxLayout()
l_4v =QVBoxLayout()

btn_folder =QPushButton('папка')
btn_left =QPushButton('лево')
btn_right = QPushButton('Право')
btn_miror =QPushButton('зерколо')
btn_sharpen = QPushButton('Резкость')
btn_bw = QPushButton('Ч/Б')
btn_list = QListWidget()
bth_foto =QLabel('картинка')

l_1gh.addLayout(l_3v)
l_1gh.addLayout(l_4v)
# l_4v.addLayout(l_2h)
window.setLayout(l_1gh)
l_3v.addWidget(btn_folder)
l_3v.addWidget(btn_list)
l_4v.addWidget(bth_foto)
l_2h.addWidget(btn_left)
l_2h.addWidget(btn_right)
l_2h.addWidget(btn_miror)
l_2h.addWidget(btn_sharpen)
l_2h.addWidget(btn_bw)
l_4v.addLayout(l_2h)




btn_sharpen.clicked.connect(workimage.saharpen)
btn_miror.clicked.connect(workimage.miror)
btn_left.clicked.connect(workimage.left)
btn_right.clicked.connect(workimage.right)
btn_bw.clicked.connect(workimage.do_bw)
btn_folder.clicked.connect(showFilenamesList)
btn_list.currentRowChanged.connect(ShowChosenImage)
window.show()
app.exec()


















































































































































