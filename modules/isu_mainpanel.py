from widgets import (
    Entry,
    GridLayout,
    Label,
    Widget,
)


class ISUMainPanel(Widget):
    def __init__(self):
        super().__init__()

        # Label and Entry
        label_appname = Label('Application Name')
        self.entry_appname = Entry()
        label_appver = Label('Application Version')
        self.entry_appver = Entry()
        label_grpname = Label('Application Group')
        self.entry_grpname = Entry()
        label_build = Label('Installer Build')
        self.entry_build = Entry()
        label_license = Label('License File')
        self.entry_license = Entry()

        # Layout
        layout = GridLayout()
        self.setLayout(layout)

        # Place widgets on the layout
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
