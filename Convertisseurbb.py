from PyQt5.QtWidgets import QMainWindow,QApplication,QVBoxLayout,QPushButton,QLineEdit,QLabel,QHBoxLayout,QComboBox,QWidget,QFrame
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
from code2 import numeration
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.size = (100,100,400,400)
        self.move(0,0)
        self.title = "Convertisseur de base en base"
        self.setWindowTitle(self.title)
        self.setGeometry(self.size[0],self.size[1],self.size[2],self.size[3])
        self.setStyleSheet("QMainWindow {background-color: #8d9b96}")

        ui = self.init_ui()
        ui_layout = QWidget()
        ui_layout.setLayout(ui)
        self.setCentralWidget(ui_layout)
        self.show()


    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)

        title = QLabel("Convertisseur de base en base ")
        title.setFont(QFont("Sanserif",20))
        title.setStyleSheet('color:white')
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        nb_widget = QHBoxLayout()
        self.number = QLineEdit("Entre ton nombre")
        self.number.setStyleSheet('color:#6B4B0F')
        self.number.setFont(QFont("Sanserif",15))
        self.number.textChanged.connect(self.convertir)
        nb_widget.addWidget(self.number)
        
        self.base = QComboBox()
        self.base.setFont(QFont("Sanserif",15))
        self.base.setStyleSheet('color:#6B4B0F')
        self.base.addItem("binaire")
        self.base.addItem("decimal")
        self.base.addItem("hexadecimal")
        self.base.currentTextChanged.connect(self.convertir)
        nb_widget.addWidget(self.base)
        main_layout.addLayout(nb_widget)


        conv = QLabel("Convertir en :")
        conv.setFont(QFont("Sanserif",20))
        conv.setStyleSheet('color:white')
        conv.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(conv)

        self.conversion = QComboBox()
        self.conversion.setFont(QFont("Sanserif",15))
        self.conversion.setStyleSheet('color:#6B4B0F')
        self.conversion.addItem("binaire")
        self.conversion.addItem("decimal")
        self.conversion.addItem("hexadecimal")
        self.conversion.currentTextChanged.connect(self.convertir)
        main_layout.addWidget(self.conversion)

        convertir = QPushButton("Convertir")
        convertir.setFont(QFont("Sanserif",15))
        convertir.setStyleSheet('color:#8d9b96')
        convertir.pressed.connect(self.convertir)
        main_layout.addWidget(convertir)

        self.resultat = QLabel("Résultat")
        self.resultat.setFont(QFont("Sanserif",20))
        self.resultat.setStyleSheet('color:white')
        self.resultat.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.resultat)
        
        return main_layout

    def convertir(self):
        number = self.number.text()
        base = self.base.currentText()
        conversion = self.conversion.currentText()
        
        nb = numeration(number,base)
        if conversion == "hexadecimal":
            resultat = str(nb.hexadecimal())
            if resultat == "None":
                self.resultat.setText("Vérifier expression")
                self.resultat.setStyleSheet('color:red')
            else:
                self.resultat.setText(resultat)
                self.resultat.setStyleSheet('color:white')
        elif conversion == "binaire":
            resultat = str(nb.binaire())
            if resultat == "None":
                self.resultat.setText("Vérifier expression")
                self.resultat.setStyleSheet('color:red')
            else:
                self.resultat.setText(resultat)
                self.resultat.setStyleSheet('color:white')
        elif conversion == "decimal":
            resultat = str(nb.decimal())
            if resultat == "None":
                self.resultat.setText("Vérifier expression")
                self.resultat.setStyleSheet('color:red')
            else:
                self.resultat.setText(resultat)
                self.resultat.setStyleSheet('color:white')
        

if __name__ == '__main__':
    App = QApplication(sys.argv)
    wind = Window()
    sys.exit(App.exec())