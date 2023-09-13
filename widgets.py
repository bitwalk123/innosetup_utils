from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QStyle,
    QToolBar,
    QToolButton,
    QWidget,
)


class Entry(QLineEdit):
    def __init(self):
        super().__init__()


class GridLayout(QGridLayout):
    def __init(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)


class Label(QLabel):
    def __init(self, title_label: str):
        super().__init__(title_label)


class ToolBar(QToolBar):
    def __init(self):
        super().__init__()


class ToolButtonIcon(QToolButton):
    def __init__(self, name_icon: str):
        super().__init__()
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        icon_std = getattr(QStyle.StandardPixmap, name_icon)
        self.setIcon(QIcon(self.style().standardIcon(icon_std)))


class Widget(QWidget):
    def __init(self):
        super().__init__()
        self.setContentsMargins(2, 2, 2, 2)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
