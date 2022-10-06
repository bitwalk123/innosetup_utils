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
        label_license = QLabel('License File')
        self.entry_license = QLineEdit()
        # Layout
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        # place widgets on the layout
        layout.addWidget(label_appname, 0, 0)
        layout.addWidget(self.entry_appname, 0, 1)
        layout.addWidget(label_appver, 1, 0)
        layout.addWidget(self.entry_appver, 1, 1)
        layout.addWidget(label_grpname, 2, 0)
        layout.addWidget(self.entry_grpname, 2, 1)
        layout.addWidget(label_build, 3, 0)
        layout.addWidget(self.entry_build, 3, 1)
        layout.addWidget(label_license, 4, 0)
        layout.addWidget(self.entry_license, 4, 1)

    def setContents(self, conf: dict):
        self.entry_appname.setText(conf['appname'])
        self.entry_appver.setText(conf['appver'])
        self.entry_grpname.setText(conf['grpname'])
        self.entry_build.setText(conf['build'])
        # License
        if 'license' in conf.keys():
            self.entry_license.setText(conf['license'])

    def getContents(self) -> dict:
        conf = {
            'appname': self.entry_appname.text(),
            'appver': self.entry_appver.text(),
            'grpname': self.entry_grpname.text(),
            'build': self.entry_build.text(),
        }
        file_license = self.entry_license.text().strip()
        if len(file_license) > 0:
            conf['license'] = file_license
        return conf
