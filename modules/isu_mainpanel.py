from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QWidget, QGridLayout,
)


class ISUMainPanel(QWidget):

    def __init__(self):
        super().__init__()
        self.setContentsMargins(2, 2, 2, 2)
        #
        label_appname = QLabel('Application Name')
        self.entry_appname = QLineEdit()
        label_appver = QLabel('Application Version')
        self.entry_appver = QLineEdit()
        label_grpname = QLabel('Application Group')
        self.entry_grpname = QLineEdit()
        label_build = QLabel('Installer Build')
        self.entry_build = QLineEdit()
        #
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        #
        layout.addWidget(label_appname, 0, 0)
        layout.addWidget(self.entry_appname, 0, 1)
        layout.addWidget(label_appver, 1, 0)
        layout.addWidget(self.entry_appver, 1, 1)
        layout.addWidget(label_grpname, 2, 0)
        layout.addWidget(self.entry_grpname, 2, 1)
        layout.addWidget(label_build, 3, 0)
        layout.addWidget(self.entry_build, 3, 1)

    def setContents(self, info: dict):
        self.entry_appname.setText(info['appname'])
        self.entry_appver.setText(info['appver'])
        self.entry_grpname.setText(info['grpname'])
        self.entry_build.setText(info['build'])

    def getContents(self) -> dict:
        info = {
            'appname': self.entry_appname.text(),
            'appver': self.entry_appver.text(),
            'grpname': self.entry_grpname.text(),
            'build': self.entry_build.text(),
        }
        return info
