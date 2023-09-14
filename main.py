from PySide6.QtWidgets import QMainWindow, QApplication, QFrame, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6 import QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface pra Gabriela se localizar")

        # Criação das estruturas básicas

        self.widget_principal = QFrame() # Widget principal onde todas as estruturas serão alocadas
        self.layout_principal = QGridLayout() # Layout do widget principal
        self.widget_principal.setLayout(self.layout_principal) # Setando Layout para o Widget principal

        # Métricas para algumas colunas do QGridLayout
        #self.layout_principal.setColumnStretch(0, 0)  # Evita o alongamento da coluna 0
        #self.layout_principal.setColumnStretch(1, 0)  # Evita o alongamento da coluna 1
        #self.layout_principal.setColumnMinimumWidth(0, 100)

        self.setCentralWidget(self.widget_principal) # Tornando o widget principal como widget central da QMainWindow

        # Criação de estruturas para aportar elementos visuais
        # Cada novo widget secundário é adicionado ao QGridLayout que é o layout principal
        # Os Widgets terciários (botões, por exemplo) são adicionados ao layout do widget secundário

        self.menu_lateral = QFrame() # QFrame para o menu lateral que possui botões estratégicos
        self.menu_lateral.setFrameShape(QFrame.Box)

        self.layout_menu_lateral = QVBoxLayout()
        self.menu_lateral.setLayout(self.layout_menu_lateral)

        self.layout_principal.addWidget(self.menu_lateral, 1, 0, 3, 1)

        # Botões para o menu lateral

        self.btn_add = QPushButton("Add")
        self.layout_menu_lateral.addWidget(self.btn_add)

        self.btn_list = QPushButton("To do")
        self.layout_menu_lateral.addWidget(self.btn_list)
        
        self.btn_stnc = QPushButton("News")
        self.layout_menu_lateral.addWidget(self.btn_stnc)

        self.barra_nome = QFrame() # Frame superior para colocar nome do app desktop
        self.barra_nome.setFrameShape(QFrame.Box)
        self.layout_barra_nome = QHBoxLayout()
        self.barra_nome.setLayout(self.layout_barra_nome)

        self.layout_principal.addWidget(self.barra_nome, 0, 0, 1, 3)

        # Botões para a barra superior

        self.btn_Gabriela = QPushButton("Essa é a intertface que a Gabriela usa pra não se perder")
        self.layout_barra_nome.addWidget(self.btn_Gabriela)

    






if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()