from PySide6.QtWidgets import QMainWindow, QApplication, QFrame, QGridLayout, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface pra Gabriela se localizar")

        # Criação das estruturas básicas

        self.widget_principal = QFrame() # Widget principal onde todas as estruturas serão alocadas
        self.layout_principal = QGridLayout() # Layout do widget principal
        self.widget_principal.setLayout(self.layout_principal) # Setando Layout para o Widget principal

        self.setCentralWidget(self.widget_principal) # Tornando o widget principal como widget central da QMainWindow

        # Criação de estruturas para aportar elementos visuais
        # Cada novo widget secundário é adicionado ao QGridLayout que é o layout principal
        # Os Widgets terciários (botões, por exemplo) são adicionados ao layout do widget secundário

        self.menu_lateral = QFrame() # QFrame para o menu lateral que possui botões estratégicos
        self.layout_menu_lateral = QVBoxLayout()
        self.menu_lateral.setLayout(self.layout_menu_lateral)

        self.layout_principal.addWidget(self.menu_lateral, 0, 0, 3, 1)

        # Botões para o menu lateral

        self.btn_add = QPushButton("Adicone uma nova nota")
        self.layout_menu_lateral.addWidget(self.btn_add)

        self.btn_list = QPushButton("Crie a TO-DO List de hoje")
        self.layout_menu_lateral.addWidget(self.btn_list)
        
        self.btn_stnc = QPushButton("Carregue uma nova frase para aprender algo novo")
        self.layout_menu_lateral.addWidget(self.btn_stnc)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()