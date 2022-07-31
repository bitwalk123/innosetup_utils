from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QStyle,
    QToolBar,
    QToolButton,
)


class ISUToolBar(QToolBar):
    dirClicked = Signal()
    playClicked = Signal()
    fileClicked = Signal()

    def __init__(self):
        super().__init__()
        label_dir = QLabel('base directory')
        self.addWidget(label_dir)
        # Entry
        self.entry_dir = QLineEdit()
        self.addWidget(self.entry_dir)
        # Dir button
        button_dir = QToolButton()
        button_dir.setToolButtonStyle(Qt.ToolButtonIconOnly)
        button_dir.setIcon(
            QIcon(self.style().standardIcon(QStyle.SP_DirIcon))
        )
        button_dir.setToolTip('select application root directory(folder).')
        button_dir.clicked.connect(self.dirClicked.emit)
        self.addWidget(button_dir)
        # Play button
        button_play = QToolButton()
        button_play.setToolButtonStyle(Qt.ToolButtonIconOnly)
        button_play.setIcon(
            QIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        )
        button_play.setToolTip('start generating iss file for Inno Setup.')
        button_play.clicked.connect(self.playClicked.emit)
        self.addWidget(button_play)
        # File button
        button_file = QToolButton()
        button_file.setToolButtonStyle(Qt.ToolButtonIconOnly)
        button_file.setIcon(
            QIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        )
        button_file.setToolTip('load predefined contents in JSON format.')
        button_file.clicked.connect(self.fileClicked.emit)
        self.addWidget(button_file)

    def get_entry(self) -> str:
        return self.entry_dir.text()

    def set_entry(self, path: str):
        self.entry_dir.setText(path)
