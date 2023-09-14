from PySide6.QtWidgets import QMainWindow, QApplication, QFrame, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface")

        # Criação das estruturas básicas

        self.widget_principal = QFrame() # Widget principal onde todas as estruturas serão alocadas
        self.layout_principal = QGridLayout() # Layout do widget principal
        self.widget_principal.setLayout(self.layout_principal) # Setando Layout para o Widget principal

        self.setCentralWidget(self.widget_principal) # Tornando o widget principal como widget central da QMainWindow


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()