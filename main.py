import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QStyle,
    QToolBar,
    QToolButton,
)


class ISUtility(QMainWindow):
    entry_dir: QLineEdit = None

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle('utility for Inno Setup Compiler')

    def init_ui(self):
        toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        #
        label_dir = QLabel('base directory')
        toolbar.addWidget(label_dir)
        #
        self.entry_dir = QLineEdit()
        toolbar.addWidget(self.entry_dir)
        #
        button_dir = QToolButton()
        button_dir.setToolButtonStyle(Qt.ToolButtonIconOnly)
        button_dir.setIcon(
            QIcon(self.style().standardIcon(QStyle.SP_DirIcon))
        )
        button_dir.clicked.connect(self.button_dir_clicked)
        toolbar.addWidget(button_dir)
        #
        button_play = QToolButton()
        button_play.setToolButtonStyle(Qt.ToolButtonIconOnly)
        button_play.setIcon(
            QIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        )
        toolbar.addWidget(button_play)

    def button_dir_clicked(self):
        path_dir = QFileDialog.getExistingDirectory(
            self,
            caption='Select Folder',
            dir=os.environ["HOME"],
        )
        self.entry_dir.setText(path_dir)


def main():
    app = QApplication(sys.argv)
    win = ISUtility()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
