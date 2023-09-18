from PySide6.QtWidgets import (
    QMainWindow, QApplication, QFrame, QGridLayout,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QStackedWidget, QSpacerItem,
    QSizePolicy, QWidget,QLabel,
    QTextEdit, QFormLayout
)

from PySide6.QtGui import QIcon, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface pra Gabriela se localizar")
        self.setMouseTracking(True) 

        # Criação das estruturas básicas

        self.widget_principal = QFrame() # Widget principal onde todas as estruturas serão alocadas
        self.widget_principal.setStyleSheet("QFrame { border: 1px solid white; }")
        self.layout_principal = QGridLayout() # Layout do widget principal
        self.widget_principal.setLayout(self.layout_principal) # Setando Layout para o Widget principal
        self.widget_principal.setStyleSheet("background-color: rgb(220,220,220); ")

        # Métricas para algumas colunas do QGridLayout
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.layout_principal.setSpacing(0)
        self.layout_principal.setColumnStretch(0, 0)  # Evita o alongamento da coluna 0

        self.setCentralWidget(self.widget_principal) # Tornando o widget principal como widget central da QMainWindow

        # Criação de QSpacerItem para melhorar a disposição dos Widgets
        self.spacer_vertical = QSpacerItem(0, 0, QSizePolicy.Ignored, QSizePolicy.Expanding)
        self.spacer_horizontal = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Ignored)

        # Criação de estruturas para aportar elementos visuais
        # Cada novo widget secundário é adicionado ao QGridLayout que é o layout principal
        # Os Widgets terciários (botões, por exemplo) são adicionados ao layout do widget secundário

        # QFrame para o menu lateral que possui botões estratégicos
        self.menu_lateral = QFrame() 
        self.menu_lateral.setFrameShape(QFrame.Box)
        self.menu_lateral.setStyleSheet("QFrame { border: 1px solid white; border-top: none; border-right: none; }")
        self.menu_lateral.setFixedWidth(50)

        self.layout_menu_lateral = QVBoxLayout()
        self.menu_lateral.setLayout(self.layout_menu_lateral)

        self.layout_principal.addWidget(self.menu_lateral, 1, 0, 3, 1)

        # Botões para o menu lateral + estilo para botões

        self.button_style = """
            QPushButton {
                border: 1px solid white;
                background-color: white;
                padding-top: 3px;
                padding-right: 5px;
                padding-bottom: 3px;
                padding-left: 5px;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #FFDAB9;
                color:white;
            }
        """

        self.btn_files = QPushButton()
        self.icon_files = QIcon("images/pasta.png")
        self.btn_files.setIcon(self.icon_files)
        self.btn_files.setStyleSheet(self.button_style)
        self.btn_files.setCursor(Qt.PointingHandCursor)
        self.layout_menu_lateral.addWidget(self.btn_files)

        self.btn_list = QPushButton("B")
        self.btn_list.setStyleSheet(self.button_style)
        self.btn_list.setCursor(Qt.PointingHandCursor)
        self.layout_menu_lateral.addWidget(self.btn_list)
        
        self.btn_stnc = QPushButton("C")
        self.btn_stnc.setStyleSheet(self.button_style)
        self.btn_stnc.setCursor(Qt.PointingHandCursor)
        self.layout_menu_lateral.addWidget(self.btn_stnc)

        self.layout_menu_lateral.addSpacerItem(self.spacer_vertical)

        # Frame superior para colocar nome do app desktop
        self.barra_nome = QFrame() 
        self.barra_nome.setFrameShape(QFrame.Box)
        self.barra_nome.setStyleSheet("QFrame { border: 1px solid white; }")
        self.barra_nome.setFixedHeight(50)
        self.layout_barra_nome = QHBoxLayout()
        self.barra_nome.setLayout(self.layout_barra_nome)

        self.layout_principal.addWidget(self.barra_nome, 0, 0, 1, 3)

        # Botões para a barra superior

        self.btn_Gabriela = QPushButton()
        self.icon_gabiapp = QIcon('images/flores.png')
        self.btn_Gabriela.setIcon(self.icon_gabiapp)
        self.btn_Gabriela.setStyleSheet(self.button_style)
        self.layout_barra_nome.addSpacerItem(self.spacer_horizontal)
        self.layout_barra_nome.addWidget(self.btn_Gabriela)
        self.layout_barra_nome.addSpacerItem(self.spacer_horizontal)

        # Frame que será situado logo abaixo da barra superior para servir de cabeçalho para outros widgets e também possuirá uma barra de pesquisa

        self.barra_pesquisa = QFrame()
        self.barra_pesquisa.setFrameShape(QFrame.Box)
        self.barra_pesquisa.setStyleSheet("QFrame { border: 1px solid white; border-top: none; border-bottom: none; }")
        self.barra_pesquisa.setFixedHeight(50)
        self.layout_pesquisa = QHBoxLayout()
        self.barra_pesquisa.setLayout(self.layout_pesquisa)

        self.layout_principal.addWidget(self.barra_pesquisa, 1, 1, 1, 2)

        # Botões e caixa de pesquisa para a barra de pesquisa

        self.caixa_pesquisa = QLineEdit()
        self.caixa_pesquisa.setPlaceholderText("Pesquisar")
        self.caixa_pesquisa.setStyleSheet('''
            QLineEdit {border-radius: 5px; color: black;
            background-image: url(images/lupa.png);
            background-position: left; background-repeat: no-repeat;
            padding-left: 20px; background-color: white;}
            QLineEdit::placeholder { text-align: center; }
        ''')
        self.layout_pesquisa.addWidget(self.caixa_pesquisa)

        self.layout_pesquisa.addSpacerItem(self.spacer_horizontal)
        self.layout_pesquisa.addSpacerItem(self.spacer_horizontal)

        # Widget para conter QStackedWidget que receberá outros widgets que se alternam no mesmo espaço

        self.area_trabalho = QFrame()
        self.area_trabalho.setFrameShape(QFrame.Box)
        self.area_trabalho.setStyleSheet("QFrame { border: 1px solid white; }")
        self.layout_area_trabalho = QVBoxLayout()
        self.area_trabalho.setLayout(self.layout_area_trabalho)

        # Criação de um QStackedWidget para poder inserir widgets que vão dividir o mesmo plano
        self.stacked_area_trabalho = QStackedWidget()
        self.stacked_area_trabalho.setStyleSheet("QStackedWidget { border: none; } ")
        self.layout_area_trabalho.addWidget(self.stacked_area_trabalho)

        self.layout_principal.addWidget(self.area_trabalho, 2, 1, 2, 2)

        self.widget_atividades = QWidget() # Widget onde vou insirir frames para editar textos, criar to-do lists e adicionar conteúdos interessantes
        #self.widget_atividades.setStyleSheet("border: none; ")
        self.layout_widget_atividades = QGridLayout()
        self.widget_atividades.setLayout(self.layout_widget_atividades)
        self.stacked_area_trabalho.insertWidget(0, self.widget_atividades)

        self.frame_conteudo = QFrame()
        self.frame_conteudo.setFixedHeight(50)
        self.frame_conteudo.setStyleSheet("border: none; ")
        self.layout_frame_conteudo = QVBoxLayout()
        self.frame_conteudo.setLayout(self.layout_frame_conteudo)
        self.layout_widget_atividades.addWidget(self.frame_conteudo, 0, 0, 1, 3)

        self.label_conteudo = QLabel("Viver é a coisa mais rara do mundo. A maioria das pessoas apenas existe. - Oscar Wilde")
        self.layout_frame_conteudo.addWidget(self.label_conteudo)

        self.frame_notes = QFrame()
        self.layout_frame_notes = QVBoxLayout()
        self.frame_notes.setLayout(self.layout_frame_notes)
        self.layout_widget_atividades.addWidget(self.frame_notes, 1, 0, 2, 2)

        self.create_notes = QTextEdit()
        self.create_notes.setPlaceholderText("Digite aqui o que precisa")
        self.layout_frame_notes.addWidget(self.create_notes)

        self.frame_checklist = QFrame()
        self.layout_frame_checklist = QVBoxLayout()
        self.frame_checklist.setLayout(self.layout_frame_checklist)
        self.layout_widget_atividades.addWidget(self.frame_checklist, 1, 2, 2, 1)
        
        self.frame_to_do = QFrame()
        self.form_to_do = QFormLayout()
        self.frame_to_do.setLayout(self.form_to_do)
        self.layout_frame_checklist.addWidget(self.frame_to_do)

        self.frame_botoes = QFrame()
        self.frame_botoes.setStyleSheet(self.button_style)
        self.frame_botoes.setFixedHeight(80)
        self.layout_frame_botoes = QHBoxLayout()
        self.frame_botoes.setLayout(self.layout_frame_botoes)
        self.layout_frame_checklist.addWidget(self.frame_botoes)

        self.add_activity = QPushButton()
        self.icon_add = QIcon("images/adicionar.png")
        self.add_activity.setIcon(self.icon_add)
        self.add_activity.setStyleSheet(self.button_style)
        self.add_activity.setCursor(Qt.PointingHandCursor)

        self.exclude_activity = QPushButton()
        self.icon_exclude = QIcon("images/excluir.png")
        self.exclude_activity.setIcon(self.icon_exclude)
        self.exclude_activity.setStyleSheet(self.button_style)
        self.exclude_activity.setCursor(Qt.PointingHandCursor)

        self.change_activity = QPushButton()
        self.icon_change = QIcon("images/editar.png")
        self.change_activity.setIcon(self.icon_change)
        self.change_activity.setStyleSheet(self.button_style)
        self.change_activity.setCursor(Qt.PointingHandCursor)


        self.layout_frame_botoes.addWidget(self.add_activity)
        self.layout_frame_botoes.addWidget(self.exclude_activity)
        self.layout_frame_botoes.addWidget(self.change_activity)



if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()