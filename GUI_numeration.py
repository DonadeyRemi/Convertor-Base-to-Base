from PyQt5.QtWidgets import QMainWindow,QApplication,QVBoxLayout,QPushButton,QLineEdit,QLabel,QHBoxLayout,QComboBox,QWidget,QFrame
from PyQt5.QtGui import QIcon,QFont
from code import numeration
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.size = (0,30,400,400)
        self.move(0,0)
        self.title = "Convertisseur de base en base"
        self.setWindowTitle(self.title)
        #self.setWindowIcon(QIcon("images/M_icon.png"))
        self.setGeometry(self.size[0],self.size[1],self.size[2],self.size[3])
        self.setStyleSheet("QMainWindow {background-color: #8d9b96}")

        ui = self.init_ui()
        ui_layout = QWidget()
        ui_layout.setLayout(ui)
        self.setCentralWidget(ui_layout)
        self.show()


    def init_ui(self):
        main_layout = QVBoxLayout()

        title = QLabel("Convertisseur de base en base ")
        title.setFont(QFont("Sanserif",20))
        title.setStyleSheet('color:#0101DF')
        main_layout.addWidget(title)

        nb_widget = QHBoxLayout()
        self.number = QLineEdit("Entre ton nombre")
        self.number.setStyleSheet('color:#472318')
        self.number.setFont(QFont("Sanserif",15))
        nb_widget.addWidget(self.number)
        
        self.base = QComboBox()
        self.base.setFont(QFont("Sanserif",15))
        self.base.setStyleSheet('color:#113527')
        self.base.addItem("binaire")
        self.base.addItem("decimal")
        self.base.addItem("hexadecimal")
        nb_widget.addWidget(self.base)
        main_layout.addLayout(nb_widget)


        conv = QLabel("Convertir en :")
        conv.setFont(QFont("Sanserif",20))
        conv.setStyleSheet('color:#0101DF')
        main_layout.addWidget(conv)

        self.conversion = QComboBox()
        self.conversion.setFont(QFont("Sanserif",15))
        self.conversion.setStyleSheet('color:#113527')
        self.conversion.addItem("binaire")
        self.conversion.addItem("decimal")
        self.conversion.addItem("hexadecimal")
        main_layout.addWidget(self.conversion)

        convertir = QPushButton("Convertir")
        convertir.setFont(QFont("Sanserif",15))
        convertir.setStyleSheet('color:red')
        convertir.pressed.connect(self.convertir)
        main_layout.addWidget(convertir)

        self.resultat = QLabel("Résultat")
        self.resultat.setFont(QFont("Sanserif",20))
        self.resultat.setStyleSheet('color:#0101DF')
        main_layout.addWidget(self.resultat)
        
        return main_layout

    def convertir(self):
        number = self.number.text()
        base = self.base.currentText()
        conversion = self.conversion.currentText()
        
        if base == "decimal":
            number = int(number)
        elif base == "hexadecimal":
            number = number
        elif base == "binaire":
            number1 = list(number)
            number = list()
            for i in number1:
                bit = int(i)
                number.append(bit)
        
        nb = numeration(number,base)
        if conversion == "hexadecimal":
            self.resultat.setText(str(nb.hexadecimal()))
        elif conversion == "binaire":
            self.resultat.setText(str(nb.binaire()))
        elif conversion == "decimal":
            self.resultat.setText(str(nb.decimal()))
        

if __name__ == '__main__':
    App = QApplication(sys.argv)
    wind = Window()
    sys.exit(App.exec())