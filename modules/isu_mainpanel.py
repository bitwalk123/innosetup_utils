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
        lab_appname = Label('Application Name')
        self.ent_appname = Entry()
        lab_appver = Label('Application Version')
        self.ent_appver = Entry()
        lab_grpname = Label('Application Group')
        self.ent_grpname = Entry()
        lab_build = Label('Installer Build')
        self.ent_build = Entry()
        lab_license = Label('License File')
        self.ent_license = Entry()

        # Layout
        layout = GridLayout()
        self.setLayout(layout)

        # Place widgets on the layout
        layout.addWidget(lab_appname, 0, 0)
        layout.addWidget(self.ent_appname, 0, 1)
        layout.addWidget(lab_appver, 1, 0)
        layout.addWidget(self.ent_appver, 1, 1)
        layout.addWidget(lab_grpname, 2, 0)
        layout.addWidget(self.ent_grpname, 2, 1)
        layout.addWidget(lab_build, 3, 0)
        layout.addWidget(self.ent_build, 3, 1)
        layout.addWidget(lab_license, 4, 0)
        layout.addWidget(self.ent_license, 4, 1)

    def setContents(self, conf: dict):
        self.ent_appname.setText(conf['appname'])
        self.ent_appver.setText(conf['appver'])
        self.ent_grpname.setText(conf['grpname'])
        self.ent_build.setText(conf['build'])
        # License
        if 'license' in conf.keys():
            self.ent_license.setText(conf['license'])

    def getContents(self) -> dict:
        conf = {
            'appname': self.ent_appname.text(),
            'appver': self.ent_appver.text(),
            'grpname': self.ent_grpname.text(),
            'build': self.ent_build.text(),
        }
        file_license = self.ent_license.text().strip()
        if len(file_license) > 0:
            conf['license'] = file_license
        return conf
