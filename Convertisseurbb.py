from PyQt5.QtWidgets import QMainWindow,QApplication,QVBoxLayout,QPushButton,QLineEdit,QLabel,QHBoxLayout,QComboBox,QWidget,QFrame,QAction,QStackedWidget,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt
from code2 import numeration
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conversion_view = True
        self.table_view = False
        self.size = (100,100,450,450)
        self.move(0,0)
        self.title = "Convertisseur de base en base"
        self.setWindowTitle(self.title)
        self.setGeometry(self.size[0],self.size[1],self.size[2],self.size[3])
        self.setStyleSheet("QMainWindow {background-color: #8d9b96}")

        self.main_widget = QStackedWidget()

        self.init_menu()
        self.conversion_ui()
        self.table_ui()

        self.show_current_wind()
        self.setCentralWidget(self.main_widget)
        self.show()

    def init_menu(self):
        mainmenu = self.menuBar()
        file_menu = mainmenu.addMenu("File")
        show_menu = mainmenu.addMenu("Show")
        
        exit_action = QAction(QIcon("images/exit.png"),"Exit",self)
        exit_action.setShortcut("Ctrl+E")
        exit_action.setToolTip("Exit opened window")
        exit_action.setStatusTip("Exit opened window")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        table_action = QAction(QIcon("images/tables.png"),"Tables",self)
        table_action.setShortcut("Ctrl+T")
        table_action.setToolTip("Show tables of conversion")
        table_action.setStatusTip("Show tables of conversion")
        table_action.triggered.connect(self.show_table)
        show_menu.addAction(table_action)

        conversion_action = QAction("Conversion",self)
        conversion_action.setShortcut("Ctrl+C")
        conversion_action.setToolTip("Show conversion")
        conversion_action.setStatusTip("Show conversion")
        conversion_action.triggered.connect(self.show_conversion)
        show_menu.addAction(conversion_action)


    def conversion_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)

        title = QLabel("Convertisseur de base en base ")
        title.setFont(QFont("Sanserif",20))
        title.setStyleSheet('color:white')
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        nb_widget = QHBoxLayout()
        self.number = QLineEdit("Entre ton nombre")
        self.number.setAlignment(Qt.AlignCenter)
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
        self.base.addItem("ASCII")
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
        self.conversion.addItem("ASCII")
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

        self.conversion_widget = QWidget()
        self.conversion_widget.setLayout(main_layout)
        self.main_widget.addWidget(self.conversion_widget)
        
        
    def table_ui(self):
        table_layout = QVBoxLayout()
        
        row = 1
        main_table = QTableWidget(row,4)
        main_table.setHorizontalHeaderItem(0,QTableWidgetItem("Décimal"))
        main_table.setHorizontalHeaderItem(1,QTableWidgetItem("Hexadécimal"))
        main_table.setHorizontalHeaderItem(2,QTableWidgetItem("Binaire"))
        main_table.setHorizontalHeaderItem(3,QTableWidgetItem("ASCII"))
        for i in range(len(numeration.ASCII_l)):
            row += 1 
            nb = numeration(str(i),"decimal")
            main_table.setItem(i,0,QTableWidgetItem("{}".format(i)))
            main_table.setItem(i,1,QTableWidgetItem("{}".format(nb.hexadecimal())))
            main_table.setItem(i,2,QTableWidgetItem("{}".format(nb.binaire())))
            main_table.setItem(i,3,QTableWidgetItem("{}".format(nb.ASCII())))
            main_table.setRowCount(row)
        

        table_layout.addWidget(main_table)

        self.table_widget = QWidget()
        self.table_widget.setLayout(table_layout)
        self.main_widget.addWidget(self.table_widget)

    def show_current_wind(self):
        if self.conversion_view == True:
            self.conversion_widget.setVisible(True)
            self.table_widget.setVisible(False)
        elif self.table_view == True:
            self.table_widget.setVisible(True)
            self.conversion_widget.setVisible(False)

    def show_table(self):
        self.table_view = True
        self.conversion_view = False
        self.show_current_wind()

    def show_conversion(self):
        self.table_view = False
        self.conversion_view = True
        self.show_current_wind()

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
            
        elif conversion == "ASCII":
            resultat = str(nb.ASCII())
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