# -*- coding: utf-8 -*-
# Version 0.9 GUI
import os

from PyQt5.QtWidgets import (QFileDialog, QWidget, QMainWindow, QVBoxLayout,
                             QLabel, QLineEdit, QPushButton, QApplication,
                             QMessageBox, qApp, QComboBox, QHBoxLayout, QGroupBox)
from PyQt5.QtCore import (Qt, QDir, pyqtSlot)

"""
Разработал студент БНТУ Колосов А.А
"""
container = {0: ["py", "pyw"],
             1: ["cpp"],
             2: ["cs"],
             3: ["js"],
             4: ["php"],
             5: ["java"]}

encoding = {0: "utf-8",
            1: "cp1251",
            2: "utf-8",
            3: "utf-8",
            4: "utf-8",
            5: "cp1251"}

names = ("Python",
         "C++",
         "C#",
         "JavaScript",
         "PHP",
         "Java")


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.lang = 0
        self.path = QDir.currentPath()
        self.save_path = QDir.currentPath()
        self.ui()

    def ui(self):

        style_box = """QGroupBox{
        border: 2px solid green;
        border-color:rgb(128,0,0);
        }"""

        self.group_one = QGroupBox(self)

        self.group_one.setStyleSheet(style_box)

        self.group_two = QGroupBox(self)

        self.group_two.setStyleSheet(style_box)

        self.file_dialog = QFileDialog()

        style = """QPushButton{
                            border-radius: 5px;
                            border: 2px solid black;
                            background-color: rgb(230,230,230);
                            font: 13px Arial italic;
                            }
                            QPushButton:hover{
                            border-radius: 5px;
                            border-color: rgb(0,128,0);
                            background-color: rgb(210,210,210)}
                            QPushButton:pressed{
                            border-radius: 5px;
                            border-color: rgb(0,128,0);
                            background-color: rgb(240,240,240);
                            }"""

        self.f_choice = QComboBox(self)
        self.f_choice.activated[int].connect(self.comboFac_active)
        self.f_choice.addItems(names)

        vbox_main = QVBoxLayout()

        self.lineEd_choice = QLineEdit(self)
        self.lineEd_choice.setReadOnly(True)

        self.lineEd_name = QLineEdit(self)

        self.lineEd_save = QLineEdit(self)
        self.lineEd_save.setReadOnly(True)

        self.button = QPushButton("Apply", self)
        self.button.clicked.connect(self.write_source_codes)
        self.button.setDisabled(False)
        self.button.setStyleSheet(style)

        self.file_btn_choice = QPushButton(" ... ", self)
        self.file_btn_choice.clicked.connect(self.file_choice_clicked)
        self.file_btn_choice.setStyleSheet(style)

        self.file_btn_save = QPushButton(" ... ", self)
        self.file_btn_save.clicked.connect(self.file_save_clicked)
        self.file_btn_save.setStyleSheet(style)

        self.title_lab = QLabel("<b><center>MakeYourLabEasy<center><b>", self)
        self.title_lab.setToolTip("Designed by KolosovAA")
        self.title_lab.setStyleSheet("QLabel{font: 15px Arial;}")

        self.directory_choice_lab = QLabel("<center>Выберите папку с исходными кодами:<center>", self)

        self.directory_save_lab = QLabel("<center>Выберите папку для сохранения:<center>", self)

        self.file_name_lab = QLabel("<center>Введите имя:<center>", self)

        vbox1 = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.directory_choice_lab, alignment=Qt.AlignVCenter | Qt.AlignHCenter)
        hbox1.addWidget(self.file_btn_choice, alignment=Qt.AlignRight)
        vbox1.addLayout(hbox1)
        vbox1.addWidget(self.lineEd_choice)

        vbox2 = QVBoxLayout()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.directory_save_lab, alignment=Qt.AlignVCenter | Qt.AlignHCenter)
        hbox2.addWidget(self.file_btn_save, alignment=Qt.AlignRight)
        vbox2.addLayout(hbox2)
        vbox2.addWidget(self.lineEd_save)

        self.group_one.setLayout(vbox1)

        self.group_two.setLayout(vbox2)

        vbox_main.addWidget(self.f_choice)
        vbox_main.addWidget(self.title_lab)
        vbox_main.addSpacing(10)
        vbox_main.addWidget(self.file_name_lab)
        vbox_main.addWidget(self.lineEd_name)
        vbox_main.addSpacing(5)
        vbox_main.addWidget(self.group_one)
        vbox_main.addSpacing(15)
        vbox_main.addWidget(self.group_two)
        vbox_main.addSpacing(10)
        vbox_main.addWidget(self.button)

        self.setLayout(vbox_main)
        self.setMaximumSize(500, 500)

    @pyqtSlot()
    def file_choice_clicked(self):

        file = self.file_dialog.getExistingDirectory(directory=self.path)
        style_box = """QGroupBox{
                border: 2px solid green;
                }"""
        self.group_one.setStyleSheet(style_box)
        file = file.replace("/", "\\")
        if os.path.exists(file):
            self.path = file

        self.lineEd_choice.setText(self.path)

    @pyqtSlot()
    def file_save_clicked(self):
        file = self.file_dialog.getExistingDirectory(directory=self.save_path)
        style_box = """QGroupBox{
                        border: 2px solid green;
                        }"""
        self.group_two.setStyleSheet(style_box)
        file = file.replace("/", "\\")
        if os.path.exists(file):
            self.save_path = file

        self.lineEd_save.setText(self.save_path)

    def comboFac_active(self, text):
        self.lang = text

    def get_run_name(self):
        return os.path.basename(__file__)

    def get_formated_name(self, one):
        x = ""
        for i in range(len(one) - 1):
            x += one[i] + "."
        return x

    def get_file_name(self):
        name = self.lineEd_name.text()
        if not name:
            name = "BaseName"
        return name

    def get_path(self, path=os.getcwd()):
        if os.path.exists(path):
            return path

        elif not len(path):
            return os.getcwd()

        else:
            return None

    def write_source_codes(self):
        name = self.get_file_name()

        if not self.path:
            print("Error: Путь не существует")
            return None
        files = os.listdir(self.path)
        progs = self.get_all_source_files(files)
        try:
            with open(self.save_path + "\\" + name + ".txt", "w", encoding=encoding[self.lang]) as file:
                print(name)
                for prog in progs:
                    file.write("Файл {0}\n\n{1}\n\n".format(prog,
                                                            self.read_code(prog)
                                                            )
                               )
        except Exception as msg:
            print(msg)

    def get_all_source_files(self, files):
        sources_list = []
        for file in files:
            one = file.split(".")
            if not os.path.isdir(file) and one[-1] in container[self.lang] and self.get_run_name() != file:
                if len(one) == 2:
                    sources_list.append(".".join([one[0], one[-1]]))
                else:
                    sources_list.append("".join([self.get_formated_name(one), one[-1]]))
        return sources_list

    def read_code(self, prog):
        with open(self.path + "\\" + prog, "r", encoding=encoding[self.lang]) as file:
            return file.read()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = Main()
        self.setCentralWidget(self.widget)

        menu = self.menuBar()

        m1 = menu.addMenu("Help")

        action = m1.addAction("Справка...", self.help_info)

        action = m1.addAction("About PyQt5...", qApp.aboutQt)
        self.setMaximumSize(500, 500)

    def help_info(self):
        QMessageBox.about(self, "О программе",
                          "<center>Тебе надоело оформлять отчёты?<center><br>"
                          "Тогда моя программа тебе поможет.<br>"
                          "<b>Всё</b>, что тебе нужно сделать - это всего лишь<br> "
                          "вставить путь к папке с файлами Python, C#, C++, JavaScript<br><br>"
                          "Листинг исходных кодов появится в выбранной папке")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(250, 200)
    window.setWindowTitle("Easy Lab")
    window.setStyleSheet("""QLineEdit:hover{border-radius:4px;
                            border-color:rgb(0,128,0);
                            background-color:rgb(220,220,220);}

                            QLineEdit{background: white;
                            font:11px Arial;
                            border: 2px solid grey;
                            border-radius:4px;}
                            QMainWindow{background-color: rgb(235, 237, 235);}

                            """)
    window.show()
    sys.exit(app.exec_())
